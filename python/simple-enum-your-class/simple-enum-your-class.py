from enum import Enum, IntEnum, StrEnum, auto

# ------------------------------ Enum class -------------------------------
# 1. Define the Enum class
class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

    # You can also use auto() to automatically assign incremental integers
    AMBER = auto()


# 2. Accessing Enum members
print(TrafficLight.RED)  # Output: TrafficLight.RED
print(TrafficLight.RED.name)  # Output: RED
print(TrafficLight.RED.value)  # Output: 1

# 3. Comparing Enum members
current_light = TrafficLight.GREEN
if current_light == TrafficLight.GREEN:
    print("Go!")

# 4. Iterating through all members
for light in TrafficLight:
    print(f"Name: {light.name}, Value: {light.value}")

# --------------------------- IntEnum Class Example --------------------------
# 1. Define the IntEnum class
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

# 2. Direct comparison with integers (No need for .value!)
task_priority = 3

if task_priority == Priority.HIGH:
    print("This task needs immediate attention.")  # This will print

# 3. Mathematical and relational operations
print(Priority.HIGH > Priority.LOW)  # Output: True
print(Priority.MEDIUM + 5)          # Output: 7

# 4. Usage in sorting
priorities = [Priority.HIGH, Priority.LOW, Priority.MEDIUM]
print(sorted(priorities))

# -------------------- StrEnum Class Example ---------------------------
# 1. Define the StrEnum class
class HttpMethod(StrEnum):
    GET = "GET"
    POST = "POST"

    # auto() automatically assigns the lowercase version of the name as the value
    DELETE = auto()


# 2. Direct comparison with strings (No need for .value!)
request_method = "GET"

if request_method == HttpMethod.GET:
    print("Fetching data...")  # This will print

# 3. Usage anywhere a string is required
print(f"Sending a {HttpMethod.POST} request.")  # Output: Sending a POST request.
print(HttpMethod.DELETE.lower())  # Output: delete (Inherits all string methods)

