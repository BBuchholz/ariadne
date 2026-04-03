from ariadne import Task, FileNameValidator

print("")
try:
    print(f"trying method 'validate_potential_name'...")
    
    task_with_punctuation = Task("REQUIREMENT: Task's needing complexity of representation? some!")
    fnv = FileNameValidator()

    fnv.validate_potential_name(task_with_punctuation.description)

except ValueError as e:
    print(f"A ValueError was properly caught: {e}")

print("")