print('This is a program which will take a number you provide and build out a multiplication table up to another number you provide')

base_num = int(input('What number would you like to see a multiplication table of? '))
range_num = int(input('What number would you like to see the table go up to? ')) + 1

for i in range(range_num):
    print(f'{base_num} + {i} = {base_num + i}')
