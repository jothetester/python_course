"""
Excercise : F = C * 9/5 + 32
https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-1-create-a-function-in-python
"""


def celcius_to_fahrenheit(celcius):
    fah = (celcius * 9 / 5) + 32
    return fah

for c in range(37, 100):
    f = celcius_to_fahrenheit(c)
    print("When c is %s, f is %s :" % (c, f))

"""
Returning Multiple Value
"""
def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    division = num1 / num2
    # return four values
    return add, sub, multiply, division

# read four return values in four variables
a, b, c, d = arithmetic(10, 2)

print("Addition: ", a)
print("Subtraction: ", b)
print("Multiplication: ", c)
print("Division: ", d)
"""
Scope Resolution
"""
enclosed_variable = 10
def function1():
    # local variable
    loc_var = 10
    print("Value is :", loc_var)
    for i in range(0,5):
        loc_var += i
    print(i)


def function2():
    print("Value is :", loc_var)
    print(enclosed_variable)

function1()
function2()