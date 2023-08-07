from guizero import App, Text, TextBox, PushButton, ListBox

def add_task():
    task = input_box.value
    if task:
        task_list.append(task)
        input_box.clear()

def remove_task():
    selectedd_value = task_list.value
    if selectedd_value:
        task_list.remove(task_list.value)

app = App("ToDo App", bg="yellow")

message = Text(app, text="Add your daily task", color="red")
task_list = ListBox(app, items=[], width=100, height=100)
input_box = TextBox(app, width=30)
add_button = PushButton(app, add_task, text="Add Task")
remove_btn = PushButton(app, remove_task, text="Remove Task")

app.display()