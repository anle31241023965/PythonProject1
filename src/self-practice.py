# name = input("What's your name? ")
# print("Hello,", name, "! Welcome!")
#
# n = int(input("How old are you? "))
# print(f"{name} is {n} years old.")
#
# x,y = input("What's your weight hay height? ").split()
# print(f"Your weight is {x} kilograms.")
# print(f"Your height is {y} centimeters.")

# s = 'Hello World'
# print(s[11::-1])

# ex2 = str(input('Enter the string: '))
# freq = {}
# for a in ex2:
#     if a in freq:
#         freq[a] += 1
#         print(ex2.replace('{}','$'))
#     else:
#         freq[a] = 1
#         print(freq)

# number = int(input('Enter a number: '))
# if number > 0:
#     print(f'The number {number} is greater than 0.')
# else:
#     print(f'The number {number} is not a positive number.')
# print('This code will be executed.')

if __name__ == '__main__':
    import random
    print('The computer thinks a number between 1 and 10.')
    com_num = random.randint(1,10)
    your_num = int(input('Enter your number: '))
    if 1 > your_num > 10:
        print('Out of range')
    else:
        if your_num == com_num:
            print('Correct.')
        else:
            print('Incorrect')
