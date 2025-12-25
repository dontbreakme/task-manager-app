import json
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Task:
    title: str
    description: str
    due_date: str  # YYYY-MM-DD


class TaskManager:
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_from_file()

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        self.save_to_file()

    def delete_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_to_file()

    def save_to_file(self) -> None:
        data = [asdict(task) for task in self.tasks]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self) -> None:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.tasks = [Task(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
