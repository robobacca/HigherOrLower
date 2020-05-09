import random
numbers = list(range(101))[1:]
print('Welcome to the game or Higher or Lower')
print('Here\'s how it works:\n'
      '- You input a number\n'
      '- Computer will generate a random number and you guess if it\'s higher or lower(bonus if the numbers are equal!)\n'
      '- If you get it correct, you win!')
num1 = int(input('Please type a number between 1 and 100 : '))
num2 = random.choice(numbers)
guess = str(input('is it higher or lower?\n'))
if num1 > int(num2):
    if guess == 'higher':
        print('Sorry, you lose')
    elif guess == 'lower':
        print('Congrats, you win!')
    else:
        print('Wrong input,please try again')
elif num1 < int(num2):
    if guess == 'higher':
        print('Congrats, you win!')
    elif guess == 'lower':
        print('Sorry, you lose')
    else:
        print('Wrong input,please try again')
elif num1 == int(num2):
    print('Amazing! You are a master of guessing!')
else:
    print('Wrong input,please try again')
