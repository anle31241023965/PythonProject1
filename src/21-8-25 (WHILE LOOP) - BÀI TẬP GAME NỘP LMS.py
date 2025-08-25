        # 1. Guess The Number Game:
        # - we will generate a random number with the help of randint() function from 1 to 100 and ask the user to guess it.
import random
while True:
    ex1 = random.randint(1,100)
    print('The computer chooses a number from 1 to 100.')
    ex1_try = 0
    win = False
    while ex1_try < 5:
        ex1_guess = int(input(f'Chance {ex1_try + 1}: '))
        ex1_try += 1
        # - After every guess, the user will be told if the number is above or below the randomly generated number.
        if ex1_guess < ex1:
            print('Your guessing number is smaller than mine.')
        elif ex1_guess > ex1:
            print('Your guessing number is bigger than mine.')
        # - The user will win if they guess the number maximum five attempts.
        else:
            print('Congratulation! You are correct!')
            win = True
            break
        if not win:
            print('You are out of chances. THe correct number is ', ex1)
        # - Ask the user to stop or continue playing again.
    ex1_choice = input('Do you want to play again? (y/n): ')
    if ex1_choice.lower() != 'y':
        print('Thank you for playing.')
        break

        # 2. Write a game that simulate rolling a pair of dice.
import random
while True:
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    ex2_total = dice_1 + dice_2
        # - If the sum of two faces is greater than 5 → “Tài”
    if ex2_total > 5:
        ex2_result = 'tài'
        # - Otherwise → “Xỉu”
    else:
        ex2_result = 'xỉu'
        # - User ask for guessing “Tài” or “Xỉu”
    ex2_guess = input('Tài hay Xỉu?: ').strip().lower()
        # - Match the results
    print(f'Kết quả: {dice_1} + {dice_2} = {ex2_total}')
    if ex2_guess == ex2_result:
        print('Đúng.')
    else:
        print('Sai.')
        # - After one turn, ask user for continue playing game.
    ex2_choice = input('Chơi tiếp? (y/n): ')
    if ex2_choice.lower() != 'y':
        print('Cảm ơn đã chơi.')
        break

        # - **** Extend the game by asking the user to enter an amount of money, then continue playing until the user runs out of money or the user stops playing. Statistics of results.
import random
money = int(input('Type your money: '))

while money > 0:
    print(f'\nBạn đang có {money} VNĐ.')
    bet = int(input('Bạn muốn cược bao nhiêu? '))

    if bet > money:
        print('Bạn không đủ tiền.')
        continue

    guess = input('Bạn đoán Tài hay Xỉu? ').strip().lower()
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2

    print(f'Kết quả là: {dice1} + {dice2} = {total}.')

    if total > 5:
        result = 'tài'
    else:
        result = 'xỉu'

    if guess == result:
        print('Bạn thắng.')
        money += bet
    else:
        print('Bạn thua.')
        money -= bet

    if money <= 0:
        print('Bạn đã hết tiền. Trò chơi kết thúc.')
        break

    choice = input('Bạn có muốn chơi tiếp không? (y/n): ')
    if choice.lower() != 'y':
        break

