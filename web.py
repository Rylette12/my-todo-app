import streamlit as st
import functions
todolist = functions.get_todolist()


def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todolist.append(todo)
    functions.write_todolist(todolist)


st.title("My To-do App")
st.subheader("this is my app")
st.write("this is to increase my productivity")

for index, todo in enumerate(todolist):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todolist.pop(index)
        functions.write_todolist(todolist)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


print("hello")
st.session_state
