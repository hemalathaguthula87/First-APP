import streamlit as st

st.set_page_config(page_title="To-Do App", page_icon="📝")

st.title("📝 Simple To-Do List App")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add task
new_task = st.text_input("Add a new task")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("Task added!")
    else:
        st.warning("Please type something.")

st.write("## Your Tasks")

# Show tasks
for i, task in enumerate(st.session_state.tasks):
    cols = st.columns([0.1, 0.7, 0.2])
    
    # Checkbox to mark complete
    done = cols[0].checkbox("", value=task["done"], key=f"done_{i}")
    st.session_state.tasks[i]["done"] = done
    
    # Task text
    if done:
        cols[1].markdown(f"~~{task['task']}~~")
    else:
        cols[1].markdown(task["task"])
    
    # Delete button
    if cols[2].button("🗑️ Delete", key=f"delete_{i}"):
        st.session_state.tasks.pop(i)
        st.experimental_rerun()
