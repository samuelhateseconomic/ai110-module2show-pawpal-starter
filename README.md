# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors 

what does it mean "the most important scheduling behaviors"?

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```

  1. [HIGH  ] Feeding              10 min  |  daily
  2. [HIGH  ] Morning walk         30 min  |  daily
  3. [HIGH  ] Medication           5 min  |  daily
  4. [MEDIUM] Fetch                15 min  |  as_needed
  5. [LOW   ] Grooming             20 min  |  weekly

Schedule (high → low priority):
- Feeding (high priority, 10 min)
- Morning walk (high priority, 30 min)
- Medication (high priority, 5 min)
- Fetch (medium priority, 15 min)
- Grooming (low priority, 20 min)
```
# Notice: There is no exact schedule time like 9 AM or any time in a day but only the amonut of time for the activities.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Time sorting | `Scheduler.sort_by_time()` | Sorts tasks by HH:MM string; unscheduled tasks go last (sentinel "99:99") |
| Auto time assignment | `Scheduler.assign_times()` | Window-filling: anchors divide the day into gaps; floating tasks fill each gap priority-first |
| Filtering by pet / status | `Owner.get_all_tasks(pet_name, status)` | Keyword filters; omit either to return all pets or all statuses |
| Recurring task filter | `Scheduler.filter_recurring(day_of_week)` | daily always included; weekly only on Monday; as_needed excluded |
| Conflict detection | `Scheduler.detect_conflicts()` | Interval overlap (same-pet vs cross-pet labels) + budget overflow check |
| Recurring auto-renewal | `Pet.complete_task(title)` | Marks task complete and appends next occurrence using `timedelta(days=1)` or `timedelta(weeks=1)` |
| Duplicate guard | `Owner.add_pet()`, `Pet.add_task()` | Silently returns the existing object instead of creating a duplicate |

### Sorting — `Scheduler.sort_by_time()`

Tasks carry a `start_time` string in `"HH:MM"` format. Python's `sorted()` with a lambda key sorts these lexicographically, which works correctly because the format is zero-padded and fixed-width (`"09:00" < "10:00"`). Tasks with no time yet receive the sentinel `"99:99"` so they sort to the end without crashing.

### Auto time assignment — `Scheduler.assign_times()`

The scheduler separates tasks into two groups:

- **Anchors** — tasks the owner pinned to a fixed time (e.g. a vet appointment at 10:00). These are immovable.
- **Floating** — tasks with no preset time. These are sorted by priority (high → medium → low), then by shortest-first within each priority tier.

Anchors divide the day into time windows (e.g. `[09:00–10:00]` and `[11:00–21:00]`). Each floating task is placed in the **first window where it fits**. This ensures gaps before anchor tasks are used before spilling tasks to later slots.

### Filtering — `Owner.get_all_tasks(pet_name=None, status=None)`

Returns tasks from all pets by default. Pass `pet_name="Mochi"` to see only one pet's tasks, `status="pending"` to exclude completed tasks, or both to combine the filters. Used by `app.py` to build the task table and by `Scheduler` to get a fresh task list before scheduling.

### Conflict detection — `Scheduler.detect_conflicts()`

Runs two checks after times are assigned:

1. **Interval overlap**: for every pair of timed tasks, checks `a_start < b_end and b_start < a_end`. Labels the warning `[SAME PET]` or `[CROSS PET]` so the owner can tell at a glance whether one pet has a double-booking or two pets need attention at the same time.
2. **Budget overflow**: sums all pending task durations and compares to `day_end − day_start`. Reports how many minutes over budget the day is.

Returns an empty list when the schedule is clean.

### Recurring tasks — `Pet.complete_task(title)` + `Task.next_occurrence()`

When the owner marks a task complete, `complete_task()` calls `next_occurrence()` on it. That method uses Python's `timedelta` to compute the next due date:

```python
timedelta(days=1)   # for frequency="daily"  → tomorrow
timedelta(weeks=1)  # for frequency="weekly" → same day next week
```

`timedelta` handles month and year boundaries automatically (e.g. January 31 + 1 day = February 1). The new task is appended to the pet's task list with `completion_status="pending"` so it shows up in the next schedule automatically.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
