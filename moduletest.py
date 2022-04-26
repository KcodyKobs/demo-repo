# #call function from previous file
# from modules import calculate_area_of_circle


# print(calculate_area_of_circle(6))
import math

num1= float(input('enter your first value'))
num2= float(input('enter your second value'))


abs= math.fabs(num1)
floor= math.floor(num2)

print(abs,' is the absolute value of', num1)
print(floor,' is the floor value of', num2)