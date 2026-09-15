"""
Path: src/shardhana/__main__.py
Created: 2026-02-08 (0.0.1.post3 — runnable GUI entrypoint)
Updated: 2026-09-15 (0.0.2 — 실제 Windows 콘솔(cmd.exe)을 창에 임베드, Laude)

이번 목표: 새 터미널 엔진을 만들지 않는다. 기존 Windows 콘솔을
Shardhana 창 안에 그대로 끼워 넣는다 (Win32 SetParent 방식).
사람이 직접 조작하는 진짜 콘솔 — AI 연결/자동 명령 실행 없음.
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

    def _find_console_window(pid: int, timeout: float = 5.0) -> Optional[int]:
        """주어진 프로세스(pid)의 콘솔 창(hwnd)을 찾는다.
        창은 프로세스 시작 직후 바로 생기지 않을 수 있어 잠깐 폴링한다."""
        result = {"hwnd": None}
        EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

        def _callback(hwnd, lparam):
            owner_pid = wintypes.DWORD()
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(owner_pid))
            if owner_pid.value == pid:
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
        self.process = subprocess.Popen(
            [self.shell],
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
    root.title("Shardhana 0.0.2")
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