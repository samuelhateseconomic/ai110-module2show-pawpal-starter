# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
At first, I follow the three core actions: 
1. add/edit pets
2. add/edit tasks
3. Schedule a Plan
to build a three classes following as:
1. Pet
2. Task
3. Daily Schedule
And my UML design looks like after I reinforced it with Claude code and visualize it through mermaid.live:
classDiagram
    class Pet {
        -name: string
        -breed: string
        -age: int
        -owner_name: string
        -available_start_time: str
        -available_end_time: str
        +add_pet(name, breed, age, owner_name, start, end) void
        +edit_pet(name, breed, age, owner_name, start, end) void
        +get_availability() tuple
    }
    
    class Task {
        -task_id: int
        -name: string
        -duration_min: int
        -priority: str (HIGH/MEDIUM/LOW)
        -category: str
        +add_task(name, duration, priority, category) int
        +edit_task(task_id, name, duration, priority, category) void
        +get_priority() str
    }
    
    class DailySchedule {
        -pet: Pet
        -tasks: list[Task]
        -scheduled_items: list[dict]
        -date: str
        +generate_schedule(pet, tasks) list
        +get_schedule() list[dict]
        +explain_reasoning() str
    }
    
    DailySchedule --> Pet: uses constraints from
    DailySchedule --> Task: arranges

- What classes did you include, and what responsibilities did you assign to each?
I believe my UML on top does included the answer for this question.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
NOT YET. 
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

chore: add class skeletons from UML
