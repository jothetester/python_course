import math
# Addition
print("Enter add_num1 : ")
num1 = input()
print("Enter add_num2 : ")
num2 = input()
result = int(num1) + int(num2)
print(" Result is : ", result)

# Subtraction
print("Enter sub_num1 : ")
num1 = input()
print("Enter sub_num2 : ")
num2 = input()
result = int(num1) - int(num2)
print(" Result is : ", result)


# Print the area of a rectangle
# Area of a triangle 1/2 * Base * Height
# Print area of a circle where r = 3cm. import math and use math.pi * r **2
area_circle = math.pi*3**2
area_circle_using_pow = math.pi*pow(3, 2)
area_circle_using_pow_round = round(math.pi*pow(3, 2), 3)
print("area of a circle is: ", area_circle)
print("area of a circle using pow: ", area_circle_using_pow)
print("area of a circle using pow and rounding to 3 digits: ", area_circle_using_pow_round)