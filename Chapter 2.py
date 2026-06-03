# For Loops
# Exersice 2.5



# 1. Write a program that prints your name 100 times.

for y in range(100):
    print('limpho', end=' ')



# 2. Write a program to fill the screen horizontally and vertically with your name. [Hint: add the option end='' into the print function to fill the screen horizontally.]

for y in range(20):
    print('limpho ' * 18)



# 3. Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The output should look like the output below.


for y in range(9):
    print(y + 1, 'limpho')



# 4. Write a program that prints out a list of the integers from 1 to 20 and their squares. The output should look like this:

for y in range(1, 20):
    print(f'{y} --- {y ** 2}')



# 5. Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.

for y in range(8, 90, 3):
    print(y, end=', ')



# 6. Write a program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2.

for y in range(100, 1, -2):
    print(y, end=', ')



# 7. Write a program that uses exactly four for loops to print the sequence of letters below.
'''
AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
'''

for y in range(10):
    print('A', end='')
for y in range(10):
    print('B', end='')
for y in range(10):
    print('CD', end='')
print('E', end='')
for y in range(10):
    print('F', end='')  
print('G')



# 8. Write a program that asks the user for their name and how many times to print it. The program should print out the user’s name the specified number of times.

name = input('whats your name?')
num = eval(input('how many times you want to print your name?'))

for y in range(num):
    print(name)



# 9. The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each number thereafter is the sum of the two preceding numbers. Write a program that asks the user how many Fibonacci numbers to print and then prints that many.
'''
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .
'''

for y in range(n):
    print(a, end=', ')
    a, b = b, a + b



# 10. Use a for loop to print a box like the one below. Allow the user to specify how wide and how high the box should be. [Hint: print('*'*10) prints ten asterisks.]
'''
*******************
*******************
*******************
*******************
'''

l = eval(input('how wide do you want the box to be?'))
h = eval(input('how tall you want the box to be?'))

for y in range(h):
    print('* ' * l)



# 11. Use a for loop to print a box like the one below. Allow the user to specify how wide and how high the box should be.
'''
*******************
*                 *
*                 *
*******************
'''

l = eval(input('how wide do you want the box to be?'))
h = eval(input('how tall you want the box to be?'))

print('*' * l)
for y in range(h - 2):
    print('*',' ' * (l - 4), '*')
print('*' * l)



# 12. Use a for loop to print a triangle like the one below. Allow the user to specify how high the triangle should be.
'''
*
**
***
****
'''

t = eval(input('how tall you want the triangle to be?'))

for y in range(t):
    print('*' * (y + 1))



# 13. Use a for loop to print an upside down triangle like the one below. Allow the user to specify how high the triangle should be.
'''
****
***
**
*
'''

t = eval(input('how tall you want the triangle to be?'))

for y in range(t, 0, -1):
    print('*' * y)



# 14. Use for loops to print a diamond like the one below. Allow the user to specify how high the diamond should be.
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''

n = eval(input('input the length of the top hallf of the triangle'))

# the top triangle
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))    # remember that working with the range() function it starts counting at 0
                                                        # therefore if n = 1; then will count only 0 since its considered in the range

# the bottom triangle
for i in range(n - 2, -1, -1):  # the code will start the range from the largest value going down
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))



# 15. Write a program that prints a giant letter A like the one below. Allow the user to specify how large the letter should be.
'''
    *
   * *
  *****
 *     *
*       *
'''

height = int(input("Enter the height of A: "))

for i in range(height):
    for j in range(height * 2):

        # Left and right slant lines
        if j == height - i or j == height + i:
            print("*", end="")

        # Middle horizontal bar
        elif i == height // 2 and height - i < j < height + i:
            print("*", end="")

        else:
            print(" ", end="")
    print()



