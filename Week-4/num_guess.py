from random import randrange

rand_num = randrange(101)
guess = ''
print(rand_num)
while guess != rand_num:
    guess = int(input("What is your next guess? "))

    if guess == rand_num:
        print("You win!")
        break
    elif guess < rand_num:
        print("Too low.")
    elif guess > rand_num:
        print("Too high.")
