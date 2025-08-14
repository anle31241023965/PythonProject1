# OPERATORS EXERCISE
# 1. Write a program that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
import math
from ctypes import c_int16

base = float(input('Enter the base: '))
height = float(input('Enter the height: '))
area_triangle = 0.5 * base * height
print(f'The area of this triangle is {area_triangle:.2f}')

# 2. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input('Enter the side a: '))
b = float(input('Enter the side b: '))
c = float(input('Enter the side c: '))
perimeter_triangle = a * b * c
print(f'The perimeter of this triangle is {perimeter_triangle:.2f}')

# 3. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input('Enter the length: '))
width = float(input('Enter the width: '))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f'The area of the rectangle is {area_rectangle:.2f}.\nThe perimeter of the rectangle is {perimeter_rectangle:.2f}.')

# 4. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input('Enter the radius: '))
area_circle = math.pi * radius * radius
        #radius * radius = radius ** 2
circumference = 2 * math.pi * radius
print(f'The area of the circle is {area_circle:.2f}.\nThe circumference of the circle is {circumference:.2f}.')

# 5. Calculate the slope, x-intercept and y-intercept of y = 2x - 2 ; y = 1/2x + 1
            # y = 2x-2
    # slope = (y2-y1)/(x2-x1)
x1, y1 = 1, 0  # y1 = 2*1 -2 = 0
x2, y2 = 3, 4  # y2 = 2*3 -2 = 4
rise, run = y2 - y1, x2 - x1
slope = rise / run
print(f'The slope of y = 2x - 2 is {slope:n}.')

    # x-intercept is (x;y) = (?;0)
y = 0
x = (y+2)/2
print(f'The x-intercept of y = 2x - 2 is the point ({x:n},{y:n}).')

    # y-intercept is (x;y) = (0;?)
x = 0
y = 2*x - 2
print(f'The y-intercept of y = 2x - 2 is the point ({x:n},{y:n}).')

            # y = 1/2x + 1
    # slope = (y2-y1)/(x2-x1)
x1, y1 = 2, 2           # y1 = 1/2*2 +1 = 0
x2, y2 = 6, 4           # y2 = 1/2*3 +1 = 4
rise, run = y2 - y1, x2 - x1
slope = rise / run
print(f'The slope of y = (1/2)x + 1 is {slope:n}.')

    # x-intercept is (x;y) = (?;0)
y = 0
x = (y-1)*2
print(f'The x-intercept of y = (1/2)x + 1 is the point ({x:n},{y:n}).')

    # y-intercept is (x;y) = (0;?)
x = 0
y = (1/2)*x + 1
print(f'The y-intercept of y = (1/2)x + 1 is the point ({x:n},{y:n}).')

# 6. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# 7. Compare the slopes in tasks 8 and 9.

# 8. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# 9. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

# 10. Use and operator to check if 'on' is found in both 'python' and 'dragon’

# 11. “I hope this course is not full of jargon.” Use in operator to check if jargon is in the sentence.

# 12.

# 13. Find the length of the text python and convert the value to float and convert it to string.

# 14. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

# 15. Writs a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

# 16. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.
