import json
from datetime import datetime

class CalendarManager:
    def __init__(self):
        self.plan = {}
        self.reference_date = datetime.now().date()  # Domyślna data odniesienia to dzisiaj

    def add_exercise(self, day, hour, description):
        if day not in self.plan:
            self.plan[day] = {}
        self.plan[day][hour] = description

    def get_plan(self):
        return self.plan

    def get_reference_date(self):
        return self.reference_date

    def export_to_json(self, file_path):
        try:
            with open(file_path, "w") as f:
                json.dump({
                    "reference_date": self.reference_date.strftime("%Y-%m-%d"),
                    "plan": self.plan
                }, f, indent=2)
        except Exception as e:
            raise Exception(f"Failed to export to {file_path}: {e}")

    def load_from_json(self, file_path="/opt/exercise_planner/plans/exercise_plan.json"):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                self.reference_date = datetime.strptime(data["reference_date"], "%Y-%m-%d").date()
                self.plan = data["plan"]
        except FileNotFoundError:
            # Jeśli plik nie istnieje, zachowujemy domyślną datę odniesienia i pusty plan
            pass
        except Exception as e:
            print(f"Error loading plan from {file_path}: {e}")
