import math

# 1. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# a) Add num_one and num_two and assign the value to a variable total
total = num_one + num_one
# b) Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# c) Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
# d) Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# e) Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
# f) Calculate num_one to the power of num_two and assign the value to a variable exp
exp = pow(num_one, num_two)
# g) Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = math.floor(division)
# h) Print all above varaibles
print(f"{num_one}+{num_two}={total}")
print(f"{num_one}-{num_two}={diff}")
print(f"{num_one}*{num_two}={product}")
print(f"{num_one}/{num_two}={division}")
print(f"{num_one}%{num_two}={remainder}")
print(f"{num_one}pow{num_two}={exp}")
print(f"{num_one}floor{num_two}={floor_division}")

# 2. The radius of a circle is 30 meters.
r = int(input("Enter the radius of a circle: "))

# a) Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 2 * math.pi * r

# b) Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = math.pi * math.pow(r, 2)

# c) Take radius as user input and calculate the area.
print("Area of circle: {:.2f}".format(area_of_circle))
print("Circum of circle: {:.2f}".format(circum_of_circle))

