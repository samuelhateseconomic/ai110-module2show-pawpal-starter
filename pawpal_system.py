from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str               # "high", "medium", "low"
    description: str = ""
    frequency: str = "daily"    # "daily", "weekly", "as_needed"
    completion_status: str = "pending"  # "pending", "complete"

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.completion_status = "complete"

    def mark_incomplete(self) -> None:
        """Reset this task back to pending."""
        self.completion_status = "pending"


@dataclass
class Pet:
    pet_name: str
    species: str  # "dog", "cat", "other"
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, title: str, duration_minutes: int, priority: str,
                 description: str = "", frequency: str = "daily") -> None:
        """Create a Task and append it to this pet's task list."""
        self.tasks.append(Task(title, duration_minutes, priority, description, frequency))

    def get_tasks(self) -> list[Task]:
        """Return all tasks belonging to this pet."""
        return self.tasks


class Owner:
    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.pets: list[Pet] = []

    def add_pet(self, pet_name: str, species: str) -> Pet:
        """Create a Pet, add it to this owner's list, and return it."""
        pet = Pet(pet_name, species)
        self.pets.append(pet)
        return pet

    def get_pets(self) -> list[Pet]:
        """Return all pets belonging to this owner."""
        return self.pets

    def get_all_tasks(self) -> list[Task]:
        """Return a flat list of every task across all pets."""
        return [task for pet in self.pets for task in pet.tasks]


class Scheduler:
    _PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def generate_schedule(self) -> list[Task]:
        """Return tasks sorted from highest to lowest priority."""
        return sorted(self.tasks, key=lambda t: self._PRIORITY_ORDER.get(t.priority, 99))

    def explain_reasoning(self) -> str:
        """Return a human-readable summary of the scheduled task order."""
        schedule = self.generate_schedule()
        if not schedule:
            return "No tasks to schedule."
        lines = [
            f"- {t.title} ({t.priority} priority, {t.duration_minutes} min)"
            for t in schedule
        ]
        return "Schedule (high → low priority):\n" + "\n".join(lines)
