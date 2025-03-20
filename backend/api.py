class APIHandler:
    def __init__(self, calendar_manager):
        self.calendar = calendar_manager
        self.handlers = {
            "add_exercise": self.add_exercise,
            "get_plan": self.get_plan,
            "export_plan": self.export_plan
        }

    def handle_request(self, request):
        action = request.get("action")
        if action in self.handlers:
            return self.handlers[action](request.get("data", {}))
        return {"error": "Invalid action"}

    def add_exercise(self, data):
        day = data.get("day")
        hour = data.get("hour")
        description = data.get("description")
        file_path = data.get("file_path", "/opt/exercise_planner/plans/exercise_plan.json")
        self.calendar.add_exercise(day, hour, description)
        return {"status": "success"}

    def get_plan(self, data):
        return {"plan": self.calendar.get_plan()}

    def export_plan(self, data):
        file_path = data.get("file_path", "/opt/exercise_planner/plans/exercise_plan.json")
        try:
            self.calendar.export_to_json(file_path)
            return {"status": "success"}
        except Exception as e:
            return {"error": str(e)}
