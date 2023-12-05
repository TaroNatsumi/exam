import json
from tasks import Task, get_data_task


def add_task():
    taskname = input('Enter your taskname: ')
    expires = input('Enter your expires(yyyy-mm-dd): ')
    task = Task(taskname, expires)
    task.append_to_json()


def see_task(user_id):
    data = get_data_task()
    for todo in data:
        if todo['owner'] == user_id:
            print(f"Id: {todo['id']}")
            print(f"Text: {todo['text']}")
            print(f"Expires at: {todo['expires']}")


def up_date_task(user_id):
    data = get_data_task()
    see_task(user_id)
    task_id = int(input("Task id: "))
    task_id_is_found = False

    for task in data:
        if task['owner'] == user_id and task['id'] == task_id:
            task_id_is_found = True
            text = input("Text (press Enter to skip): ")
            expires = input("Expires at (yyyy-mm-dd) (press Enter to skip): ")
            task['text'] = text if len(text.strip()) != 0 else task['text']
            task['expires'] = expires if len(expires.strip()) != 0 else task['expires']
            break

    with open(r'D:\SHOXRUX\Foundation\BUTCAMP\Python\Exam\2 - modul\tasks.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Edited successfully" if task_id_is_found else "Incorrect ID")



def delete(user_id):
    data = get_data_task()
    see_task(user_id)
    task_id = int(input("Task id: "))
    task_id_is_found = False

    for task in data:
        if task['owner'] == user_id and task['id'] == task_id:
            task_id_is_found = True
            data.remove(task)
            break

    with open(r'D:\SHOXRUX\Foundation\BUTCAMP\Python\Exam\2 - modul\tasks.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Deleted successfully" if task_id_is_found else "Incorrect ID")
