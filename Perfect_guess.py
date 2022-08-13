import random

num=random.randint(1,100)

user_input=int(input("Guess the number between 1-100\n"))
guesses=0
while user_input!=num:
    guesses+=1
    if num>user_input:
        user_input=int(input("Enter  a larger number\n"))
    elif num<user_input:
        user_input=int(input("Enter a smaller number\n"))
if num==user_input :
    guesses+=1
    print("You guessed the right number.")
    print("Number of guesses :",guesses)