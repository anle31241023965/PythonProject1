#PYTHON IF... ELSE STATEMENT EXERCISE

        # 1. Write a program to check a person is eligible for voting or not (accept age from user)
ex1 = int(input('Enter your age: '))
if ex1 >= 18:
    print('You are eligible for voting.')
else:
    print('You are not eligible for voting.')

        # 2. Write a program to check whether a number entered by user is even or odd.
ex2 = int(input('Enter a number: '))
if ex2 % 2 == 1:
    print(f'The number {ex2} is odd.')
else:
    if ex2 == 0:
        print(f'The number {ex2} is neither even nor odd.')
    elif ex2 % 2 == 0:
        print(f'The number {ex2} is even.')

        # 3. Write a program to check whether a number is divisible by 7 or not.
ex3 = int(input('Enter a number: '))
if ex3 % 7 == 0:
    print(f'The number {ex3} is divisible by 7.')
else:
    print(f'The number {ex3} is not divisible by 7.')

        # 4. Write a program to check the last digit of a number (entered by user) is divisible by 3 or not.
ex4 = input('Enter a number: ')
ex4_last_num = int(ex4[-1])
if ex4_last_num % 3 == 0:
    print(f'The last digit of the number {ex4} is divisible by 3.')
else:
    print(f'The last digit of the number {ex4} is not divisible by 3.')

        # 5. Write a Python program to guess a number between 1 and 9.
import random
print('The computer will guess a number from 1 to 9.')
ex5_com_num = random.randint(1,9)
ex5_your_num = int(input('You guess a number from 1 to 9: '))
if ex5_com_num == ex5_your_num:
    print('Correct.')
else:
    print('Incorrect.')

        # 6. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday and so on.
ex6 = int(input('Enter a number from 1 to 7: '))
if 5 <= ex6 <= 7:
    if ex6 == 5:
        print('Friday')
    elif ex6 == 6:
        print('Saturday')
    else:
        print('Sunday')
elif 1 <= ex6 < 5:
    if ex6 <= 3:
        if ex6 == 1:
            print('Monday')
        elif ex6 == 2:
            print('Tuesday')
        else:
            print('Wednesday')
    else:
        print('Thursday')
else:
    print('Invalid number.')