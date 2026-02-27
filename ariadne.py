from abc import ABC, abstractmethod

# Component -> Task
class Task(ABC):
    @abstractmethod
    def show_details(self):
        pass

    def current_indent(self):
        pass

# Leaf -> SimpleTask
class SimpleTask(Task):
    def __init__(self, description):
        self.description = description

    def show_details(self):
        print(f"- [ ] {self.description}")

# Composite -> ComplexTask
class ComplexTask(Task):
    def __init__(self, description):
        self.description = description
        self.child_tasks = []

    def add_task(self, task): 
        self.child_tasks.append(task)

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

    print("TODO: make current indent change when tasks get added to each other and update show_details method to reflect current indent for a given task")
