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
            raise ValueError(f"description must be a string! RECEIVED: {value}")
        value = value.strip()
        if not value:
            raise ValueError(f"description must not be empty or whitespace! RECEIVED: {value}")
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
    print("these next steps should all throw an error and get caught properly, if it does not, its not working yet, we'll move them to an error catching block when its confirmed that they throw errors (this is a quick and dirty Red Green Test from TDD principles)")
    print("")
    print("If this script ends with 'An unknown error occurred' it means they weren't caught properly")
    
    # NONSTRING TASK VIOLATION
    print("")
    try:
        print("trying...")
        some_list = ["string", "list", "not supported"]
        nonstring_task1 = SimpleTask(some_list)
        

    except ValueError as e:
        print(f"A ValueError was properly caught: {e}")
    
    print("")
    
    # EMPTY TASK VIOLATION
    print("")
    try:
        print("trying...")
        
        empty_task = SimpleTask("")
        empty_task.show_details()

    except ValueError as e:
        print(f"A ValueError was properly caught: {e}")
    
    print("")
    
    
    # WHITESPACE TASK VIOLATION
    print("")
    try:
        print("trying...")
        whitespace_task = ComplexTask(" ")
        whitespace_task.show_details()
        
    except ValueError as e:
        print(f"A ValueError was properly caught: {e}")
    
    print("")
    
    
    try:
        nonalphanumeric_task1 = ComplexTask("Apostrophe's Breakage")
        nonalphanumeric_task1.show_details()
        nonalphanumeric_task2 = ComplexTask("No Punctuation!! Cuz They Might Become Slip Titles!!!")
        nonalphanumeric_task2.show_details()
        print("if you can read this, they aren't failing properly")
    except ValueError as e:
        print(f"A ValueError occured: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} – {e}")

