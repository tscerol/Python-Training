def name_gen(f_name, m_name, l_name):
    return f_name.title() + ' ' + m_name.title() + ' ' + l_name.title()


print("Welcome to the name formatter. This program will make sure your name is properly formatted with capitalizations.")
first_name = input('Input your first name: ')
middle_name = input('Input your middle name: ')
last_name = input('Input your last name: ')
full_name = name_gen(first_name,middle_name,last_name) 
print(f'Your formatted full name is {full_name}.')
