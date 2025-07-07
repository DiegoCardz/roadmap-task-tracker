#%%
from .utils import printv, logger
from datetime import datetime as dt
import json

#%%
class Task():
    __max_id = 0
    tasks = {}
    
    def __init__(self, description):
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
        self.append()
    
    @classmethod
    def _next_id_(cls):
        cls.__max_id += 1
        return cls.__max_id
    
    @classmethod
    def get_tasks(cls):
        try:
            with open('tasks.json', 'r') as file:
                cls.tasks = json.load(file)
        except Exception as e:
            cls.tasks = {}
            printv(f"[Warning] {e}")
            
    @classmethod
    def get_max_id(cls):
        try: 
            cls.__max_id = max([int(x) for x in cls.tasks.keys()])
        except Exception as e:
            printv(f"[Warning] {e}")
            cls.__max_id = 0
    
    @property
    def id(self):
        return self.__id
    
    @property
    def as_dict(self):
        return {
            'id': self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
    
    def append(self):
        self.__class__.tasks[self.id] = {
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
    
    @classmethod
    def export_to_file(cls, path='tasks.json'):
        with open(path, 'w') as file:
            json.dump(cls.tasks, file, indent=4)

Task.get_tasks()
Task.get_max_id()