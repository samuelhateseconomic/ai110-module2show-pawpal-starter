import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown("Plan your pet's day — add a pet, add tasks, and generate a schedule.")

st.divider()

st.subheader("Owner & Pet Setup")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Set Owner & Pet"):
    # vault check: create Owner only if not yet in session_state,
    # or if the owner name changed
    if "owner" not in st.session_state or st.session_state.owner.owner_name != owner_name:
        st.session_state.owner = Owner(owner_name)

    # always add the pet when this button is clicked
    pet = st.session_state.owner.add_pet(pet_name, species)
    st.session_state.current_pet = pet
    st.success(f"Owner '{owner_name}' and pet '{pet_name}' are ready!")

st.markdown("### Tasks")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    if "current_pet" not in st.session_state:
        st.warning("Set an owner and pet first.")
    else:
        st.session_state.current_pet.add_task(task_title, int(duration), priority)
        st.success(f"Task '{task_title}' added!")

if "owner" in st.session_state:
    all_tasks = st.session_state.owner.get_all_tasks()
    if all_tasks:
        st.write("Current tasks:")
        st.table([
            {"title": t.title, "duration_minutes": t.duration_minutes, "priority": t.priority}
            for t in all_tasks
        ])
    else:
        st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    if "owner" not in st.session_state or not st.session_state.owner.get_all_tasks():
        st.warning("Add an owner, pet, and at least one task first.")
    else:
        scheduler = Scheduler(st.session_state.owner.get_all_tasks())
        st.text(scheduler.explain_reasoning())
