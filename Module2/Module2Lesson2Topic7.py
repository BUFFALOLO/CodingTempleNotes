def to_be_defined():
    pass

to_be_defined() # No output and no error

#

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

print("The script continues")

#

for i in range(5):
    pass

print("Loop completed!")

#

class FutureImplementation:
    def method_one(self):
        pass

    def method_two(self):
        pass

obj = FutureImplementation()
obj.method_one() # No output and no error

#

value = 10

if value > 5:
    pass # will implement this later
else:
    print("Value is not greater than 5.")


