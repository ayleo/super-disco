import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title('My To-Do App')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.write(f"Removed {todo}")
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Add a new todo", placeholder="Enter a new todo", on_change=add_todo, key="new_todo")
