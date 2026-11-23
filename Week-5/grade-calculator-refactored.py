def grade_finder(i_grade):
    
    if grade >= 90:
        print(f'Your grade of {grade} is an A.')
    elif grade < 90 and grade >= 80:
        print(f'Your grade of {grade} is a B.')
    elif grade < 80 and grade >= 70:
        print(f'Your grade of {grade} is a C.')
    elif grade < 70 and grade >= 60:
        print(f'Your grade of {grade} is a D.')
    else:
        print(f'Your grade of {grade} is a F.')


print('This program is a simple grade calculator for a class. We will take 5 grades and determine the grade for the class.')
g1 = int(input('Enter your first grade for the class: '))
g2 = int(input('Enter your second grade for the class: '))
g3 = int(input('Enter your third grade for the class: '))
g4 = int(input('Enter your fourth grade for the class: '))
g5 = int(input('Enter your fifth grade for the class: '))
grade = (g1 + g2 + g3 + g4 + g5) / 5

grade_finder(grade)
