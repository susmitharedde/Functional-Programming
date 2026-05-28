def add(a, b):
    return a + b
def total_sum(*numbers):
    return sum(numbers)
def student_info(**data):
    for key, value in data.items():
        print(key, ":", value)
square = lambda x: x * x
message = "Welcome to Functional Programming"

def display():
    local_msg = "Inside Function"
    print(local_msg)
    print(message)


print("Addition:", add(10, 20))

print("Total Sum:", total_sum(1,2,3,4,5))

student_info(name="Susmitha", branch="ECE", year=4)

print("Square:", square(6))

display()
