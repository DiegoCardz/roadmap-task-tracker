#%%
from .utils import printv, logger
from datetime import datetime as dt
import json

#%%
class Task():
    __max_id = 0
    def __init__(self, description):
        self.get_tasks()
        self.__id = self._next_id_()
        self.description = description
        self.status = 'todo'
        self.createdAt = str(dt.now())
        self.updatedAt = str(dt.now())
        
        printv(f"New instance of 'Task' created:")
        printv("----{"+f"id: {self.id}, "
               f"description: {self.description}, "
               f"status: {self.status}, "
               f"createdAT: {self.createdAt}, "
               f"updatedAt: {self.updatedAt}"+"}")
        self.__class__.tasks.append(self.as_dict)
    
    @classmethod
    def _next_id_(cls):
        cls.__max_id += 1
        return cls.__max_id
    
    @classmethod
    def get_tasks(cls):
        try:
            with open('tasks.json', 'r') as file:
                cls.tasks = json.load(file)
                if isinstance(cls.tasks, list):
                    max_id = max(task.get("id", 0) for task in cls.tasks)
                    cls.__max_id = max_id
                else:
                    cls.__max_id = 0
        except Exception as e:
            cls.tasks = []
            printv(f"[Warning] {e}")
            cls.__max_id = 0
    
    @property
    def id(self):
        return self.__id
    
    @property
    def as_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
    
    def export_to_file(self, path='tasks.json'):
        with open(path, 'w') as file:
            json.dump(self.__class__.tasks, file, indent=4)


# %%
def get_class_Task_started():
    for i in range(5):
        t = Task(f"This is my "
                f"{i+1}{'st' if i==1 else 'nd' if i==2 else 'rd' if i==3 else 'th'} "
                f"task")
        t.as_dict
        t.__class__.tasks
        t.export_to_file()
# %%
