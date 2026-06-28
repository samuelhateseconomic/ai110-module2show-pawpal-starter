from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str  # "low", "medium", "high"


@dataclass
class Pet:
    pet_name: str
    species: str  # "dog", "cat", "other"
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, title: str, duration_minutes: int, priority: str) -> None:
        pass


class Owner:
    def __init__(self, owner_name: str):
        self.owner_name = owner_name


class Scheduler:
    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def generate_schedule(self) -> None:
        pass
