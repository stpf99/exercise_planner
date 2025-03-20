import sys
import json
import socket
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QPushButton, QLineEdit, QComboBox, QLabel)
from PyQt6.QtCore import Qt

class ExercisePlannerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercise Planner")
        self.client = None
        self.connect_to_daemon()
        self.init_ui()

    def connect_to_daemon(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(('localhost', 5000))
        except ConnectionRefusedError:
            print("Nie można połączyć się z daemonem. Uruchom go najpierw!")
            sys.exit(1)

    def init_ui(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()

        # Ścieżka do pliku JSON
        path_layout = QHBoxLayout()
        self.path_input = QLineEdit("/opt/exercise_planner/plans/exercise_plan.json")
        path_layout.addWidget(QLabel("Ścieżka pliku JSON:"))
        path_layout.addWidget(self.path_input)

        # Inputs
        input_layout = QHBoxLayout()
        self.day_combo = QComboBox()
        self.day_combo.addItems([str(i) for i in range(1, 31)])
        self.hour_input = QLineEdit("9:00")
        self.desc_input = QLineEdit()
        input_layout.addWidget(QLabel("Doba:"))
        input_layout.addWidget(self.day_combo)
        input_layout.addWidget(QLabel("Godzina:"))
        input_layout.addWidget(self.hour_input)
        input_layout.addWidget(QLabel("Opis:"))
        input_layout.addWidget(self.desc_input)

        # Buttons
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Dodaj ćwiczenie")
        export_btn = QPushButton("Eksportuj plan")
        add_btn.clicked.connect(self.add_exercise)
        export_btn.clicked.connect(self.export_plan)
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(export_btn)

        layout.addLayout(path_layout)
        layout.addLayout(input_layout)
        layout.addLayout(btn_layout)
        widget.setLayout(layout)

    def send_request(self, request):
        try:
            self.client.send(json.dumps(request).encode())
            response = self.client.recv(1024).decode()
            if not response:
                raise ValueError("Received empty response from daemon")
            return json.loads(response)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return {"error": "Invalid response from daemon"}
        except Exception as e:
            print(f"Request error: {e}")
            return {"error": str(e)}

    def add_exercise(self):
        request = {
            "action": "add_exercise",
            "data": {
                "day": int(self.day_combo.currentText()),
                "hour": self.hour_input.text(),
                "description": self.desc_input.text(),
                "file_path": self.path_input.text()
            }
        }
        response = self.send_request(request)
        print(response)
        if response.get("status") == "success":
            self.export_plan()

    def export_plan(self):
        request = {
            "action": "export_plan",
            "data": {"file_path": self.path_input.text()}
        }
        response = self.send_request(request)
        print(response)

def run_gui():
    app = QApplication(sys.argv)
    window = ExercisePlannerGUI()
    window.show()
    sys.exit(app.exec())
