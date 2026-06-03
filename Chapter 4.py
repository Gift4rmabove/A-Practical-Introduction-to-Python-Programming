# If Statements
# Exersice 4.5



# 1. Write a program that asks the user to enter a length in centimeters. If the user enters a negative length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length to inches and print out the result. There are 2.54 centimeters in an inch.

length = eval(input('enter a length in centimetres:'))
inches = length / 2.54
inches = round(inches, 2)
x = 0

while length <= 0:
    print('invalid lenght; try again')
    length = eval(input('enter a length in centimetres:'))
    x = x + 1
    if x == 3:
        print('Too many invalid input')
        break

if length > 0:
    print(f'{length} centimetre is {inches} in inches.')



# 2. Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. Your program should convert the temperature to the other unit.

temperature = eval(input('input temperature:'))
units = input('in what units; celsius or fahrenheit?')
units = units.lower()

# my equations are off so i need to fix those in the future
celsius = temperature / (9 / 5 * 32)
fahrenheit = 9 / 5 * temperature + 32

if units[0] == 'c':
    print(f'{temperature} celsius in fahrenheit is {fahrenheit}')
elif units[0] == 'f':
    print(f'{temperature} fahrenheit in celsius is {celsius}')
else:
    print('invalid input')



# 3. Ask the user to enter a temperature in Celsius. The program should print a message based on the temperature:

temperature_in_celsius = eval(input('enter temperature in celsius:'))

if temperature_in_celsius < -273.15:
    print('temperature is invald; due to being absolute zero')
elif temperature_in_celsius == -273.15:
    print('temperature at absolute zero')
elif temperature_in_celsius < 0:
    print('temperature is below freezing')
elif temperature_in_celsius == 0:
    print('freezing point')
elif temperature_in_celsius < 100:
    print('temperature is at normal range')
elif temperature_in_celsius == 100:
    print('temperature is at boiling point')
else:
    print('temperature above boiling point')



# 4. Write a program that asks the user how many credits they have taken. If they have taken 23 or less, print that the student is a freshman. If they have taken between 24 and 53, print that they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

name = input('whats your name?')
credits = eval(input('how many credits have you taken?'))

while credits <= 0:
    print('invalid value; try again')
    credits = eval(input('how many credits have you taken?'))

if credits <= 23:
    print(f'{name}, you a freshman')
elif credits <= 53:
    print(f'{name}, you a sophomore')
elif credits <= 83:
    print(f'{name}, you a senior')
else:
    print(f'thats a lie {name}; you sure.')



# 5. Generate a random number between 1 and 10. Ask the user to guess the number and print a message based on whether they get it right or not.

from random import randint
random_number = randint(1, 10)
guess_random_number = eval(input('guess any number between 1 - 10:'))

if random_number == guess_random_number:
    print(f'your guess was correct; {random_number} = {guess_random_number}')
else:
    print(f'incorrect; {random_number} != {guess_random_number}')




# 6. A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a program that asks the user how many items they are buying and prints the total cost.

number_of_items = eval(input(('how many items have you bought?')))

while number_of_items <= 0:
    print('you have to buy a item first')
    number_of_items = eval(input(('how many items have you bought?')))

if number_of_items <= 10:
    print(f'your total amount is,', number_of_items * 12)
elif number_of_items <= 99:
    print(f'your total amount is,', number_of_items * 10)
else:
    print(f'your total amount is,', number_of_items * 7)




# 7. Write a program that asks the user for two numbers and prints Close if the numbers are within .001 of each other and Not close otherwise.

x = eval(input('enter value in float'))
y = eval(input('enter value in float'))
absolute_value = abs(x - y)

if absolute_value <= .001:
    print('close')
else:
    print('not close')



# 8. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. Write a program that asks the user for a year and prints out whether it is a leap year or not.

#import calender
import calendar

# user input year
user_year = int(input('input year(yyyy)'))

# check if year is leap
if calendar.isleap(user_year):
    print(f'{user_year} is a leap year.')
else:
    print(f'{user_year} is not a leap year')



# 9. Write a program that asks the user to enter a number and prints out all the divisors of that number. [Hint: the % operator is used to tell if a number is divisible by something. See Section 3.2.]

v = eval(input('enter a value'))
print(f'finding the divisors of {v}:')

for y in range(1, v):
    if v % y == 0:
        print(f'{y} * {v // y} = {v}')



# 10. Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them whether they got it right or wrong and what the correct answer is.
'''
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.
'''

from random import randint

i = 0
score = 0
while i < 10:
    x = randint(1, 10)
    y = randint(1, 10)
    q = x * y
    z = eval(input(f'whats the answer for {x} * {y}?'))

    if z == q:
        print(f'correct. {x} * {y} = {q}')
        score = score + 1
        print()
    else:
        print(f'the answer is not {z}')
        print(f'{x} * {y} = {q}')
        print()
    i = i + 1
print('game comple')
print(f'you got {score} / 10 correct')
print(f'{(score / 10) * 100}%')




# 11.

# 12.

# 13. Write a program that lets the user play Rock-Paper-Scissors against the computer. There should be five rounds, and after those five rounds, your program should print out who won and lost or that there is a tie.

player_one = 0    # the user is player one
player_two = 0    # the computer is player two
player_one_score = 0
player_two_score = 0

rock = [1, 'r', 'rock']
paper = [2, 'p', 'paper']
scissors = [3, 's', 'scissors', 'scissor']

rounds = 0
print('ROCK, PAPER, SCISSORS SHOOT!!!')
print('________________________________________________________________________')
print()
from random import randrange
while rounds < 5:
    player_one =input('rock, paper, scissors shoot')
    player_two = randrange(1, 4)
    
    # if the game is a tie
    if player_one in rock and player_two in rock:
        print('both chose rock')
        print('its a draw')
        print()
        rounds += 1
    elif player_one in paper and player_two in paper:
        print('both chose paper')
        print('its a drawer')
        print()
        rounds += 1
    elif player_one in scissors and player_two in scissors:
        print('both chose rock')
        print('its a draw')
        print()
        rounds += 1

    # if player_one wins
    elif player_one in rock and player_two in scissors:
        print('player one chose rock and computer chose scissors')
        print('player one wins')
        print()
        player_one_score += 1
        rounds += 1
    elif player_one in paper and player_two in rock:
        print('player one chose paper and computer chose rock')
        print('player one wins')
        print()
        player_one_score += 1
        rounds += 1
    elif player_one in scissors and player_two in paper:
        print('player one chose scissors and computer chose paper')
        print('player one wins')
        print()
        player_one_score += 1
        rounds += 1
    
    # if player_two wins
    # be more specific with code (*case sensitive)
    else:
        print('computer won')
        print()
        player_two_score +=1
        rounds += 1
print('________________________________________________________________________')

# the score sheet
if player_one_score == player_two_score:
    print('the game is a tie')
    print(f'player one got {player_one_score} and computer got {player_two_score}')
elif player_one_score >= player_two_score:
    print('player one wins the match')
    print(f'player one got {player_one_score} and computer got {player_two_score}')
else:
    print('the computer wins')
    print(f'player one got {player_one_score} and computer got {player_two_score}')
