"""
Path: src/shardhana/__main__.py
Created: 2026-02-08 (0.0.1.post3 — runnable GUI entrypoint)
Updated: 2026-09-15 (0.0.2 — 실제 Windows 콘솔(cmd.exe)을 창에 임베드, Laude)
Updated: 2026-09-24 (0.0.3 — Windows Terminal 위임 문제만 최소 수정, Laude)

이번 목표: 새 터미널 엔진을 만들지 않는다. 기존 Windows 콘솔을
Shardhana 창 안에 그대로 끼워 넣는다 (Win32 SetParent 방식).
사람이 직접 조작하는 진짜 콘솔 — AI 연결/자동 명령 실행 없음.

[0.0.3 수정 — 딱 이것만 고침]
0.0.2 배포 EXE에서 샤드하나 창과 터미널 창이 따로 떴던 원인: Windows 11의
"기본 터미널 앱"이 Windows Terminal로 위임돼 있으면, cmd.exe를 그냥
CREATE_NEW_CONSOLE로 띄워도 실제 창은 cmd.exe의 PID가 아니라
WindowsTerminal.exe 소유의 별도 창(class=CASCADIA_HOSTING_WINDOW_CLASS)으로
뜬다. 기존 코드는 cmd.exe의 PID + class="ConsoleWindowClass"로만 창을
찾아서 이 경우 영영 못 찾고 조용히 포기했다 (검은 화면 + 별도 터미널 창).
고친 것은 딱 두 곳: ① cmd.exe 대신 conhost.exe로 감싸서 실행해 그 위임을
우회하고, ② conhost.exe의 자식으로 뜨는 cmd.exe 창도 찾을 수 있도록
_find_console_window의 매칭 조건에 "부모가 spawned pid인 경우"를 추가.
그 외 임베딩/스타일/종료 처리 로직은 0.0.2와 동일하게 유지했다.

[2026-09-24 작업 기록 — 0.0.3 시험 배포]
- 목표: 0.0.2 배포 EXE에서 샤드하나와 터미널이 별도 창으로
  실행되는 문제를 개선한다.
- 변경: conhost.exe를 통해 콘솔을 실행하고, 창 탐색 대상을
  실행한 프로세스의 자식 프로세스까지 확장했다.
- 사용자 관찰: 실행 직후 두 창이 따로 나타났다가 약 3~4초 후
  터미널이 샤드하나 창 안에 결합되는 현상을 확인했다.
- 이번 빌드: 위 현상을 알려진 미해결 사항으로 남기고
  0.0.3 시험 배포를 진행한다.
- 다음 과제: 결합 지연의 원인을 확인하고, 시작할 때 별도 창이
  노출되는 현상을 개선한다.
- 검증 범위: 현재 PC에서의 관찰이며, 다른 환경과 GitHub에서
  내려받은 배포 EXE의 동작은 별도로 확인해야 한다.
  
"""

import sys
import subprocess
import threading
import time
import tkinter as tk
from typing import Optional

if sys.platform == "win32":
    import ctypes
    from ctypes import wintypes

    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    GWL_STYLE = -16
    WS_CAPTION = 0x00C00000
    WS_THICKFRAME = 0x00040000
    WS_BORDER = 0x00800000
    WS_DLGFRAME = 0x00400000
    WS_SYSMENU = 0x00080000
    WS_MINIMIZEBOX = 0x00020000
    WS_MAXIMIZEBOX = 0x00010000
    SWP_FRAMECHANGED = 0x0020
    SWP_NOZORDER = 0x0004
    SWP_NOACTIVATE = 0x0010

    TH32CS_SNAPPROCESS = 0x00000002

    class _PROCESSENTRY32(ctypes.Structure):
        _fields_ = [
            ("dwSize", wintypes.DWORD),
            ("cntUsage", wintypes.DWORD),
            ("th32ProcessID", wintypes.DWORD),
            ("th32DefaultHeapID", ctypes.POINTER(ctypes.c_ulong)),
            ("th32ModuleID", wintypes.DWORD),
            ("cntThreads", wintypes.DWORD),
            ("th32ParentProcessID", wintypes.DWORD),
            ("pcPriClassBase", ctypes.c_long),
            ("dwFlags", wintypes.DWORD),
            ("szExeFile", ctypes.c_char * 260),
        ]

    def _get_parent_pid(pid: int) -> Optional[int]:
        """conhost.exe로 감싸 실행하면 실제 콘솔 창은 그 자식인 cmd.exe가
        갖고 있어서, 부모 pid도 확인해야 창을 찾을 수 있다."""
        snap = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
        if snap == -1:
            return None
        try:
            entry = _PROCESSENTRY32()
            entry.dwSize = ctypes.sizeof(_PROCESSENTRY32)
            if kernel32.Process32First(snap, ctypes.byref(entry)):
                while True:
                    if entry.th32ProcessID == pid:
                        return entry.th32ParentProcessID
                    if not kernel32.Process32Next(snap, ctypes.byref(entry)):
                        break
            return None
        finally:
            kernel32.CloseHandle(snap)

    def _find_console_window(pid: int, timeout: float = 5.0) -> Optional[int]:
        """주어진 프로세스(pid) 또는 그 자식 프로세스의 콘솔 창(hwnd)을 찾는다.
        창은 프로세스 시작 직후 바로 생기지 않을 수 있어 잠깐 폴링한다."""
        result = {"hwnd": None}
        EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

        def _callback(hwnd, lparam):
            owner_pid = wintypes.DWORD()
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(owner_pid))
            if owner_pid.value == pid or _get_parent_pid(owner_pid.value) == pid:
                class_name = ctypes.create_unicode_buffer(256)
                user32.GetClassNameW(hwnd, class_name, 256)
                if class_name.value == "ConsoleWindowClass":
                    result["hwnd"] = hwnd
                    return False  # 찾았으면 열거 중단
            return True

        proc_enum = EnumWindowsProc(_callback)
        deadline = time.time() + timeout
        while time.time() < deadline and not result["hwnd"]:
            user32.EnumWindows(proc_enum, 0)
            if not result["hwnd"]:
                time.sleep(0.1)
        return result["hwnd"]

    def _strip_chrome(hwnd_console: int) -> None:
        """콘솔 창의 제목표시줄/테두리를 없애서 Frame 안에 자연스럽게 붙게 한다."""
        style = user32.GetWindowLongW(hwnd_console, GWL_STYLE)
        style &= ~(
            WS_CAPTION | WS_THICKFRAME | WS_BORDER | WS_DLGFRAME
            | WS_SYSMENU | WS_MINIMIZEBOX | WS_MAXIMIZEBOX
        )
        user32.SetWindowLongW(hwnd_console, GWL_STYLE, style)
        user32.SetWindowPos(
            hwnd_console, 0, 0, 0, 0, 0,
            SWP_FRAMECHANGED | SWP_NOZORDER | SWP_NOACTIVATE,
        )

    def _resize_console(hwnd_console: int, width: int, height: int) -> None:
        if width > 0 and height > 0:
            user32.MoveWindow(hwnd_console, 0, 0, width, height, True)


class EmbeddedConsole:
    """cmd.exe(또는 powershell.exe)를 새 콘솔로 띄운 뒤, 그 창을 지정한
    tkinter Frame 안에 Win32 SetParent로 끼워 넣는다. Windows 전용."""

    def __init__(self, parent_frame: tk.Frame, shell: str = "cmd.exe"):
        self.parent_frame = parent_frame
        self.shell = shell
        self.process: Optional[subprocess.Popen] = None
        self.hwnd: Optional[int] = None

        if sys.platform != "win32":
            tk.Label(
                parent_frame,
                text="이 콘솔 임베드 기능은 현재 Windows 전용입니다.",
                fg="red",
            ).pack(padx=10, pady=10)
            return

        parent_frame.bind("<Configure>", self._on_resize)
        threading.Thread(target=self._launch_and_embed, daemon=True).start()

    def _launch_and_embed(self) -> None:
        # cmd.exe를 곧바로 띄우면 Windows Terminal이 기본 터미널로
        # 설정된 환경에서 별도 창(WindowsTerminal.exe 소유)으로 열려버려
        # 못 찾는다. conhost.exe로 감싸면 그 위임을 우회한다.
        self.process = subprocess.Popen(
            ["conhost.exe", self.shell],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        hwnd = _find_console_window(self.process.pid)
        if hwnd is None:
            return  # 콘솔 창을 못 찾음 — 조용히 포기 (다음 단계에서 오류 표시 보강 가능)

        def _embed():
            self.hwnd = hwnd
            parent_hwnd = self.parent_frame.winfo_id()
            user32.SetParent(hwnd, parent_hwnd)
            _strip_chrome(hwnd)
            self._on_resize()

        self.parent_frame.after(0, _embed)

    def _on_resize(self, event=None) -> None:
        if self.hwnd:
            _resize_console(
                self.hwnd,
                self.parent_frame.winfo_width(),
                self.parent_frame.winfo_height(),
            )

    def terminate(self) -> None:
        if self.process and self.process.poll() is None:
            self.process.terminate()


def main():
    root = tk.Tk()
    root.title("Shardhana 0.0.3")
    root.geometry("900x600")

    label = tk.Label(root, text="Hello Shardhana !!!")
    label.pack(padx=20, pady=(20, 5))

    terminal_frame = tk.Frame(root, bg="black")
    terminal_frame.pack(fill="both", expand=True, padx=15, pady=(5, 15))

    console = EmbeddedConsole(terminal_frame, shell="cmd.exe")

    def on_close():
        console.terminate()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()


if __name__ == "__main__":
    main()