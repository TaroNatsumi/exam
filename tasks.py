import json

def get_data_task():
    try:
        with open(r'D:\SHOXRUX\Foundation\BUTCAMP\Python\Exam\2 - modul\tasks.json', 'r') as f:
            tasks: list = json.load(f)
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        with open(r'D:\SHOXRUX\Foundation\BUTCAMP\Python\Exam\2 - modul\tasks.json', 'w') as f:
            json.dump([], f, indent=4)
            return []

class Task:

    def __init__(self, taskname, expires):
        self.taskname = taskname
        self.expires = expires

    def append_to_json(self, user_id):
        tasks = get_data_task()
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) != 0 else 1,
            'taskname': self.taskname,
            'task_text': self.expires,
            "owner": user_id,
        }
        tasks.append(task)
        with open(r'D:\SHOXRUX\Foundation\BUTCAMP\Python\Exam\2 - modul\tasks.json', 'w') as f:
            json.dump(tasks, f, indent=4)
        print('Successfully added')