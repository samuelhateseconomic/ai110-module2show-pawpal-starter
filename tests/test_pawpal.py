from pawpal_system import Task, Pet


def test_mark_complete_changes_status():
    task = Task(title="Morning walk", duration_minutes=30, priority="high")
    task.mark_complete()
    assert task.completion_status == "complete"


def test_add_task_increases_pet_task_count():
    pet = Pet(pet_name="Mochi", species="cat")
    pet.add_task("Feeding", 10, "high")
    assert len(pet.get_tasks()) == 1
