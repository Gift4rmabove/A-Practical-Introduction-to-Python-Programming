# Numbers
# Exersice 3.8



# 1. Write a program that generates and prints 50 random integers, each between 3 and 6.

from random import randint

for y in range(50):
    print(randint(3, 6), end=', ')

  

# 2. Write a program that generates a random number, x, between 1 and 50, a random number y between 2 and 5, and computes x^y .

x = randint(1, 5)
y = randint(2, 5)

print(f'{x}^{y} = {x ** y}')



# 3. Write a program that generates a random number between 1 and 10 and prints your name that many times.

for y in range(randint(1, 50)):
    print(y + 1, 'limpho')



# 4. Write a program that generates a random decimal number between 1 and 10 with two decimal places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.

import random

num = round(random.uniform(0, 10), 2)   # uniform function generates a random float between the specified range; in this case between 0 and 10, and we round it to 2 decimal places

print(num)



# 5. Write a program that generates 50 random numbers such that the first number is between 1 and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between 1 and 51.


for y in range(1,50):
    print(f'random values from 1 - {y + 1}:',randint(1, (y + 1)))



# 6. Write a program that asks the user to enter two numbers, x and y, and computes (|x−y|) / (x+y) .


x = eval(input('enter first value'))
y = eval(input('enter second value'))

a = abs(x - y)
b = x + y
print(a / b)



# 7. Write a program that asks the user to enter an angle between −180◦ and 180◦. Using an expression with the modulo operator, convert the angle to its equivalent between 0◦ and 360◦.

angle = int(input("Enter an angle between -180 and 180: "))

# Convert using modulo operator
converted_angle = angle % 360

print("Equivalent angle:", converted_angle)



# 8. Write a program that asks the user for a number of seconds and prints out how many minutes and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the // operator to get minutes and the % operator to get seconds.]

sec = eval(input('enter a number of seconds'))
minutes = sec // 60 # used to get the minutes
seconds = sec % 60  # used to get the ramaining seconds

print(f'{sec} seconds is {minutes} minutes and {seconds} seconds')

# learn to work with exceptions in this problem



# 9. Write a program that asks the user for an hour between 1 and 12 and for how many hours in the future they want to go. Print out what the hour will be that many hours into the future. An example is shown below.

time = eval(input('whats the time currently?'))
alarm = eval(input('how many hours ahead you want your alarm to be?'))

new_hour = (time + alarm) % 12
print(f'so the time is {time} o\' clock and you want your alarm to go of in {alarm} hours time')
print(f'your alarm will go off at {new_hour} o\'clock')




# 10
# (a) One way to find out the last digit of a number is to mod the number by 10. Write a program that asks the user to enter a power. Then find the last digit of 2 raised to that power.

num = eval(input('enter a value with three digits'))
num_squared = num ** 2
retries = 0

# working with exceptions if the output is less than 3
while num_squared < 100:
    print('the output is small try a number greater than 10')
    num = eval(input('enter a value with three digits'))
    retries = retries + 1
    if retries == 3:
        print('learn to read buddy')
        break

if num_squared > 99:
    print(f'the last 2 digits of {num}^2 is {num_squared % 100}')

# (b) One way to find out the last two digits of a number is to mod the number by 100. Write a program that asks the user to enter a power. Then find the last two digits of 2 raised to that power.

num = 16
power = eval(input('enter any power'))
num_squared = num ** power
retries = 0

# working with exceptions if the output is less than 3
while num_squared < 100:
    print('the output is small try a number greater than 10')
    num = eval(input('enter a value with three digits'))
    retries = retries + 1
    if retries == 3:
        print('learn to read buddy')
        break

if num_squared > 99:
    print(f'the last 2 digits of {num}^{power} is {num_squared % 100}')

# (c) Write a program that asks the user to enter a power and how many digits they want. Find the last that many digits of 2 raised to the power the user entered.


default_v = 16
power = eval(input('enter a power'))
lngth_of_last_digits = eval(input('enter the length of last digits'))
length_of_last_digits = 10 ** lngth_of_last_digits

print(f'the last {lngth_of_last_digits} digits of {default_v}^{power} are {(default_v ** power) % length_of_last_digits}')
print(f'{default_v}^{power} = {default_v ** power}')



# 11. Write a program that asks the user to enter a weight in kilograms. The program should convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

kg = eval(input('whats your weight in kilograms?'))
print('your weight in pounds is', round(kg * 2.2, -1))  # rounding off to the nearest 10



# 12. Write a program that asks the user for a number and prints out the factorial of that number.

fact = eval(input('enter a value'))
print(f'the factorial of {fact} is {factorial(fact)}')



# 13. Write a program that asks the user for a number and then prints out the sine, cosine, and tangent of that number.

from math import sin, cos, tan

value = eval(input('enter any value'))
s = sin(value)
c = cos(value)
t = tan(value)

print(f'sine({value}) = {s}')
print(f'cosine({value}) = {c}')
print(f'tangent({value}) = {t}')



# 14. Write a program that asks the user to enter an angle in degrees and prints out the sine of that angle.

from math import sin

angle = eval(input('enter a angle'))
sin(angle)



# 15. Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦ in 15◦ increments. Each result should be rounded to 4 decimal places. Sample output is shown below:
'''
0 --- 0.0 1.0
15 --- 0.2588 0.9659
30 --- 0.5 0.866
...
345 --- -0.2588 0.9659
'''

from math import sin, cos

print(f'increment --- sin() --- cos()')
for y in range(0, 345, 15):
    print(y, round(sin(y), 4), round(cos(y), 4), sep=' --- ')



# 16. Below is described how to find the date of Easter in any year. Despite its intimidating appearance, this is not a hard problem. Note that ⌊x⌋ is the floor function, which for positive numbers just drops the decimal part of the number. For instance ⌊3.14⌋ = 3. The floor function is part of the math module.



# 17. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator, determine how many leap years there have been between 1600 and that year.

x = 0

for y in range(1600, 2026):
    if calendar.isleap(y):
        x += 1
print(f'There are {x} leap year within the 1600 till 2026')



# 18. Write a program that given an amount of change less than $1.00 will print out exactly how many quarters, dimes, nickels, and pennies will be needed to efficiently make that change. [Hint: the // operator may be useful.]



# 19. Write a program that draws “modular rectangles” like the ones below. The user specifies the width and height of the rectangle, and the entries start at 0 and increase typewriter fashion from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5 rectangle and a 4 × 8.

width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

number = 0

for i in range(height):
    for j in range(width):
        print(number % 10, end=" ") # Print the current number modulo 10 to get the last digit, also used to return to 0 after reaching 9

        number += 1
    print() # Move to the next line after each row is printed
