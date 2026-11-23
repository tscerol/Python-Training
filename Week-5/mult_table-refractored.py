def mul_table(b_num, r_num):
    for i in range(r_num):
        print(f'{b_num} + {i} = {b_num + i}')

print('This is a program which will take a number you provide and build out a multiplication table up to another number you provide')

base_num = int(input('What number would you like to see a multiplication table of? '))
range_num = int(input('What number would you like to see the table go up to? ')) + 1

mul_table(base_num, range_num)
