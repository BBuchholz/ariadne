import re

class FileNameValidator():

    def validate_potential_name(self, value):
        if re.search(r'[^a-zA-Z0-9\s]', value):
            raise ValueError("String contains characters other than alphanumeric and spaces.")


class Task():
    def __init__(self, description):
        self.description = description
        self.indent_factor = 0
        self.child_tasks = []

    def add_task(self, task): 
        task.indent_factor = self.indent_factor + 1
        self.child_tasks.append(task)

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

    def show_details(self):
        tab_prefix = "\t" * self.indent_factor 
        print(f"{tab_prefix}- [ ] {self.description}")
        for child_task in self.child_tasks:
            child_task.show_details()


# Usage
if __name__ == '__main__':

    task1 = Task("Task 1")
    task2 = Task("Task 2")
    task2.add_task(task1)
    task2.show_details()

    print("")
    print("TODO: make current indent change when tasks get added to each other and update show_details method to reflect current indent for a given task")
    print("")