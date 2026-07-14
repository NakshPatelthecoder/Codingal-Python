class Employee:

    def __init__(self):
        print("Employee Created")

    def __delete__(self):
        print("Destructor called")

def  Create_obj():
    print("Making object")
    obj = Employee()
    print("Function End")
    return obj 

print("Calling Create_obj() function")
obj = Create_obj()
print("Programme END")
del obj