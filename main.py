"""
Shardhana 1D FEM / HEM Demo
GUI Seed v0.1 — 2026/04/05
Minimal three-panel PySide6 window.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit,
    QGroupBox
)


class ShardhanaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shardhana 1D FEM / HEM Demo")
        self.setMinimumSize(900, 500)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # --- Left Panel: Input ---
        left_group = QGroupBox("Input")
        left_layout = QVBoxLayout(left_group)
        left_layout.setSpacing(6)

        fields = [
            ("Number of Nodes",    "4"),
            ("Number of Elements", "3"),
            ("Total Length",       "1.0"),
            ("Young's Modulus (E)","210e9"),
            ("Area (A)",           "0.01"),
            ("Applied Force (F)",  "1000"),
        ]

        self.inputs = {}
        for label_text, default in fields:
            row = QWidget()
            row_layout = QVBoxLayout(row)
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(2)
            row_layout.addWidget(QLabel(label_text))
            edit = QLineEdit(default)
            row_layout.addWidget(edit)
            left_layout.addWidget(row)
            self.inputs[label_text] = edit

        left_layout.addStretch()

        # --- Middle Panel: Actions ---
        mid_group = QGroupBox("Actions")
        mid_layout = QVBoxLayout(mid_group)
        mid_layout.setSpacing(10)

        btn_build = QPushButton("Build Model")
        btn_run   = QPushButton("Run Analysis")

        btn_build.setMinimumHeight(40)
        btn_run.setMinimumHeight(40)

        btn_build.clicked.connect(self.on_build_model)
        btn_run.clicked.connect(self.on_run_analysis)

        mid_layout.addStretch()
        mid_layout.addWidget(btn_build)
        mid_layout.addWidget(btn_run)
        mid_layout.addStretch()

        # --- Right Panel: Output ---
        right_group = QGroupBox("Output")
        right_layout = QVBoxLayout(right_group)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        right_layout.addWidget(self.output)

        # Add panels to main layout
        main_layout.addWidget(left_group, 2)
        main_layout.addWidget(mid_group, 1)
        main_layout.addWidget(right_group, 3)

        # Startup message
        self.log("Program started.")

    def log(self, message: str):
        self.output.append(message)

    def on_build_model(self):
        self.log("Build Model clicked.")

    def on_run_analysis(self):
        self.log("Run Analysis clicked.")


def main():
    app = QApplication(sys.argv)
    window = ShardhanaWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()