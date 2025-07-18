import streamlit as st
import functions

todos = functions.get_todos()

# Add to-do's
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my to-do app")
st.write("This is app is to increase your productivity")

# Complete to-do's
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")




