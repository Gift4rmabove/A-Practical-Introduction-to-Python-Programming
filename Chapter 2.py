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
