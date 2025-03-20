import socket
import threading
import json
import time
from datetime import datetime, timedelta
import dbus
from .api import APIHandler
from .calendar_manager import CalendarManager

class ExerciseDaemon:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except Exception as e:
            print(f"Failed to bind socket: {e}")
            raise
        self.calendar = CalendarManager()
        self.api = APIHandler(self.calendar)
        self.clients = []
        self.running = True
        self.notification_thread = threading.Thread(target=self.check_notifications)
        self.notification_thread.daemon = True
        self.notification_thread.start()

    def handle_client(self, client_socket):
        self.clients.append(client_socket)
        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                response = self.api.handle_request(json.loads(data))
                client_socket.send(json.dumps(response).encode())
            except json.JSONDecodeError:
                client_socket.send(json.dumps({"error": "Invalid JSON request"}).encode())
            except Exception as e:
                client_socket.send(json.dumps({"error": str(e)}).encode())
                break
        self.clients.remove(client_socket)
        client_socket.close()

    def check_notifications(self):
        try:
            bus = dbus.SessionBus()
            notifications = bus.get_object("org.freedesktop.Notifications", "/org/freedesktop/Notifications")
            notify_interface = dbus.Interface(notifications, "org.freedesktop.Notifications")
        except dbus.exceptions.DBusException as e:
            print(f"Failed to connect to DBus: {e}")
            return

        while self.running:
            try:
                self.calendar.load_from_json()
                now = datetime.now().date()
                reference_date = self.calendar.get_reference_date()
                # Oblicz bieżącą dobę względem reference_date
                days_since_reference = (now - reference_date).days + 1
                current_day = str(days_since_reference)
                current_time = datetime.now().strftime("%H:%M")
                plan = self.calendar.get_plan()
                if current_day in plan and current_time in plan[current_day]:
                    description = plan[current_day][current_time]
                    self.send_notification(notify_interface, current_day, current_time, description)
            except Exception as e:
                print(f"Error in notification check: {e}")
            time.sleep(60)

    def send_notification(self, notify_interface, day, time, description):
        try:
            notify_interface.Notify(
                "Exercise Planner",
                0,
                "calendar",
                f"Ćwiczenie - Doba {day}",
                f"{time}: {description}",
                [],
                {"desktop-entry": "exercise_planner"},
                5000
            )
        except Exception as e:
            print(f"Notification error: {e}")

    def run(self):
        print(f"Daemon running on {self.host}:{self.port}")
        while True:
            try:
                client_socket, addr = self.server.accept()
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket,)
                )
                client_thread.start()
            except Exception as e:
                print(f"Error accepting client: {e}")

if __name__ == "__main__":
    daemon = ExerciseDaemon()
    daemon.run()
