from abc import ABC, abstractmethod

# Component -> Task
class Task(ABC):
    def __init__(self, description):
        self.description = description

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("description must be a string")
        value = value.strip()
        if not value:
            raise ValueError("description must not be empty or whitespace")
        self._description = value

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
    print("these next steps should all throw and error, if it does not, its not working yet, we'll move them to an error catching block when its confirmed that they throw errors (this is a quick and dirty Red Green Test from TDD principles)")
    print("")
    print("If this script ends with 'An unknown error occurred' it means they weren't caught properly")
    print("")
    try:
        empty_task1 = SimpleTask("")
        empty_task1.show_details()
        empty_task2 = ComplexTask(" ")
        empty_task2.show_details()
        nonalphanumeric_task1 = ComplexTask("Apostrophe's Breakage")
        nonalphanumeric_task1.show_details()
        nonalphanumeric_task2 = ComplexTask("No Punctuation!! Cuz They Might Become Slip Titles!!!")
        nonalphanumeric_task2.show_details()
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} – {e}")
    except:
        print("An unknown error occurred")
