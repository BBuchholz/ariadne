from deprecated import SimpleTask, ComplexTask

print("these next steps should all throw an error and get caught properly, if it does not, its not working yet, we'll move them to an error catching block when its confirmed that they throw errors (this is a quick and dirty Red Green Test from TDD principles)")
print("")
print("If this script ends with 'An unexpected error occurred' it means they weren't caught properly")

# NONSTRING TASK VIOLATION
task_violation_name = "NONSTRING"
print("")
try:
    print(f"trying {task_violation_name} task violation...")
    some_list = ["string", "list", "not supported"]
    nonstring_task1 = SimpleTask(some_list)
    

except ValueError as e:
    print(f"A ValueError was properly caught: {e}")

print("")

# EMPTY TASK VIOLATION
task_violation_name = "EMPTY"
print("")
try:
    print(f"trying {task_violation_name} task violation...")
    
    empty_task = SimpleTask("")
    empty_task.show_details()

except ValueError as e:
    print(f"A ValueError was properly caught: {e}")

print("")


# WHITESPACE TASK VIOLATION
task_violation_name = "WHITESPACE"
print("")
try:
    print(f"trying {task_violation_name} task violation...")
    whitespace_task = ComplexTask(" ")
    whitespace_task.show_details()
    
except ValueError as e:
    print(f"A ValueError was properly caught: {e}")

print("")

# APOSTROPHE TASK VIOLATION
task_violation_name = "APOSTROPHE"
print("")
try:
    print(f"trying {task_violation_name} task violation...")
    nonalphanumeric_task1 = ComplexTask("Apostrophe's Breakage")
    nonalphanumeric_task1.show_details()
    
except ValueError as e:
    print(f"A ValueError was properly caught: {e}")

print("")

# PUNCTUATION TASK VIOLATION
task_violation_name = "PUNCTUATION"
print("")
try:
    print(f"trying {task_violation_name} task violation...")
    nonalphanumeric_task2 = ComplexTask("No Punctuation!! Cuz They Might Become Slip Titles!!!")
    nonalphanumeric_task2.show_details()
    
except ValueError as e:
    print(f"A ValueError was properly caught: {e}")

print("")

try:
    nonalphanumeric_task2 = ComplexTask("No Punctuation!! Cuz They Might Become Slip Titles!!!")
    nonalphanumeric_task2.show_details()
    print("if you can read this, they aren't failing properly")
except ValueError as e:
    print(f"A ValueError occured: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {type(e).__name__} – {e}")
