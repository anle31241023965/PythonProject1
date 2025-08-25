# FOR LOOP EXERCISE

        # 1. write a program that prints numbers from 1 to 10
for ex1 in range(1,11):
    print(ex1)

        # 2. Write a program to calculate the sum of numbers in a range from 1 to n (n is entered from the keyboard)
ex2 = n = int(input('Enter a number: '))
i = 0
for j in range(1, n + 1):
    i += j
else:
    print(f'The sum of number is {i}.')

        # 3. Write a program to calculate the sum of even (/odd) numbers in a range from 1 to n (n is entered from the keyboard)
ex3 = m = int(input('Enter a number: '))
ex3_even = 0
ex3_odd = 0
for b in range(1, m+1):
    if b % 2 == 0:
        ex3_even += b
    else:
        ex3_odd += b
print(f'The sum of even number is {ex3_even}.')
print(f'The sum of odd number is {ex3_odd}.')

        # 4. Write a program to check how many vowels are in a string entered from the keyboard.
ex4 = input('Enter the string: ')
ex4_vowels = 'aieouAIEOU'
ex4_count = 0
for c in ex4:
    if c in ex4_vowels:
        ex4_count += 1
print('The number of vowels in the string is: ', ex4_count)

        # 5. Write a program to count the number of words in a sentence the user enters.
ex5 = input('Enter the string: ')
ex5_words = ex5.split()
ex5_count = 0
for d in ex5_words:
    ex5_count += 1
print('The number of words in the string is: ', ex5_count)

        # 6. Write a program that implements a game as the following description:
        # 6.1. The computer generates a random number from 1 to 100
import random
ex6 = random.randint(1,100)
print('The computer chooses a number from 1 to 100.')
        # 6.2. The user was asked to guess
for e in range(1,1000):
    ex6_guess = int(input('Your guessing number is: '))
        # 6.3. match the user-guessing number to the generated number
    if ex6_guess == ex6:
        print('Congratulation! You have it correct!')
        break
    elif ex6_guess < ex6:
        print('Your number is lower than mine!')
    else:
        print('Your number is higher than mine!')

        # 7. The user can only guess five times.
import random
ex7 = random.randint(1,100)
print('The computer chooses a number from 1 to 100. You have 5 chances to guess!')
for f in range(5):
    ex7_guess = int(input(f'Chance {f+1}: '))
    if ex7_guess == ex7:
        print('Congratulation! You have it correct!')
        break
    elif ex7_guess < ex7:
        print('Your number is lower than mine!')
    else:
        print('Your number is higher than mine!')
else:
    print('You are out of chance. The bumber ')