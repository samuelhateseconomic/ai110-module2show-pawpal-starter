from pawpal_system import Owner, Scheduler

owner = Owner("Jordan")

mochi = owner.add_pet("Mochi", "cat")
mochi.add_task("Feeding",       10, "high",   frequency="daily")
mochi.add_task("Grooming",      20, "low",    frequency="weekly")

biscuit = owner.add_pet("Biscuit", "dog")
biscuit.add_task("Morning walk", 30, "high",   frequency="daily")
biscuit.add_task("Medication",    5, "high",   frequency="daily")
biscuit.add_task("Fetch",        15, "medium", frequency="as_needed")

scheduler = Scheduler(owner.get_all_tasks())
schedule = scheduler.generate_schedule()

print(f"=== Today's Schedule for {owner.owner_name} ===\n")
for i, task in enumerate(schedule, start=1):
    print(f"  {i}. [{task.priority.upper():6}] {task.title:<20} {task.duration_minutes} min  |  {task.frequency}")

print(f"\n{scheduler.explain_reasoning()}")
