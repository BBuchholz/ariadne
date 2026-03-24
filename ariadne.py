from abc import ABC, abstractmethod
import re

# Component -> Task
class Task(ABC):
    def __init__(self, description):
        self.description = description

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self.validate_description(value)
        self._description = value

    def validate_description(self, value):
        if not isinstance(value, str):
            raise ValueError(f"description must be a string! RECEIVED: {value}")
        value = value.strip()
        if not value:
            raise ValueError(f"description must not be empty or whitespace! RECEIVED: {value}")

    @abstractmethod
    def show_details(self):
        pass


# Leaf -> SimpleTask
class SimpleTask(Task):
    def show_details(self):
        print(f"- [ ] {self.description}")

# Composite -> ComplexTask
class ComplexTask(Task):
    def __init__(self, description):
        super().__init__(description)
        self.child_tasks = []

    def add_task(self, task): 
        self.child_tasks.append(task)

    def validate_description(self, value):
        super().validate_description(value)
        if re.search(r'[^a-zA-Z0-9\s]', value):
            raise ValueError("String contains characters other than alphanumeric and spaces.")

    def show_details(self):
        print(f"- [ ] {self.description}")
        for child_task in self.child_tasks:
            child_task.show_details()


# Usage
if __name__ == '__main__':

    simple_task1 = SimpleTask("Simple Task 1")
    complex_task1 = ComplexTask("Complex Task 1")
    complex_task1.add_task(simple_task1)
    complex_task1.show_details()

    print("")
    print("TODO: make current indent change when tasks get added to each other and update show_details method to reflect current indent for a given task")
    print("")