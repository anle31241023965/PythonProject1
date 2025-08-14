# NUMBER EXERCISE 2
# 2. The radius of a circle is 30 meters.
radius = int(input("Enter the radius of a circle: "))

# a) Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 2 * math.pi * radius

# b) Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = math.pi * math.pow(radius, 2)

# c) Take radius as user input and calculate the area.
print(f"Area of circle is {area_of_circle:.1f}.")
print(f"Circum of circle is {circum_of_circle:.1f}")
