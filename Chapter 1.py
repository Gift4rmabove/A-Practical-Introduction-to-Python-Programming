# Getting Started
# Exersice 1.8



# 1. Print a box like the one below
'''
*******************
*******************
*******************
*******************
'''

y = 4
for i in range(y):  # therefore the for loop is columns you want to print
    print('*' * 10)



# 2. Print a box like the one below.
'''
*******************
*                 *
*                 *
*******************
'''

y = 2
print('*' * 10)
for i in range(y):
    print('*',' ' * 6, '*')
print('*' * 10)



# 3. Print a triangle like the one below.
'''
*
**
***
****
'''

y = 4
n = 1
for i in range(y):
    print('*' * n)
    n = n + 1



# 4. Write a program that computes and prints the result of (512 − 282) / (47 · 48 + 5), It is roughly 0.1017.

x = 512 - 282
y = 47 * 48 + 5
round(x / y, 4)



# 5. Ask the user to enter a number. Print out the square of the number, but use the sep optional argument to print it out in a full sentence that ends in a period. Sample output is shown below.
'''
Enter a number: 5
The square of 5 is 25.
'''

x = eval(input('enter a number to power by 2'))
print(f'the power of {x} is {x ** 2}')



# 6. Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x, each separated by three dashes, like below.
'''
Enter a number: 7
7---14---21---28---35
'''

x = eval(input('enter a value'))
y = 1

for i in range(4):
    print(x * y, end='---')
    y = y + 1
print(x * y)



# 7. Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram.

kg = eval(input('whats your weight in kilograms?'))
print('your weight in pounds is', kg * 2.2)



# 8. Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the three numbers and print out the values of total and average.

x = eval(input('enter first value'))
y = eval(input('enter second value value'))
z = eval(input('enter third value'))

total = x + y + z
average = total / 3
print(f'the total is {total} and the average is {average}')



# 9. A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and the percent tip they want to leave. Then print both the tip amount and the total bill with the tip included. 

meal_cost = eval(input('whats the price of the meal?'))
tip = eval(input('whats the tip in percentage?'))

tip_amount = meal_cost * tip
total = meal_cost + tip_amount

print(f'the tip amount is R{tip_amount} and the bill total is R{total}')
