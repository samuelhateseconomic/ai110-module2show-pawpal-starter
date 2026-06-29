from pawpal_system import Owner, Scheduler

owner = Owner("Jordan")

mochi = owner.add_pet("Mochi", "cat")
biscuit = owner.add_pet("Biscuit", "dog")

# Anchor: Vet visit pinned to 10:00 (60 min) -> ends 11:00
# Floating tasks should fill 09:00-10:00 first, then spill to 11:00+
mochi.add_task("Vet visit",     60, "high",   frequency="as_needed", start_time="10:00")
mochi.add_task("Feeding",       10, "high",   frequency="daily")       # should fill 09:00 window
mochi.add_task("Grooming",      20, "low",    frequency="weekly")      # low — goes after 11:00

biscuit.add_task("Medication",   5, "high",   frequency="daily")       # should fill 09:00 window
biscuit.add_task("Morning walk", 30, "high",  frequency="daily")       # should fill 09:00 window
biscuit.add_task("Play session", 20, "low",   frequency="as_needed")   # low — goes after 11:00

print("=== Window-filling schedule ===")
print("  Anchor: Vet visit pinned at 10:00 (ends 11:00)")
print("  Windows: [09:00-10:00] and [11:00-21:00]\n")

result = Scheduler(owner.get_all_tasks()).schedule()

for t in result.tasks:
    tag = "(anchor)" if t.title == "Vet visit" else ""
    print(f"  {t.start_time} | [{t.priority.upper():6}] {t.title:<20} {t.duration_minutes} min  {tag}")

if result.conflicts:
    print("\nConflicts:")
    for c in result.conflicts:
        print(f"  ! {c}")
else:
    print("\nNo conflicts detected.")
