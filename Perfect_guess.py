import random

num=random.randint(1,100)

user_input=input("Guess the number between 1-100\n")
guesses=0
while user_input!=num:
    try:
        user_input=int(user_input)
    except:
        print("Please enter a valid value")
        user_input=input("Enter the number between 1-100\n")
        continue
    guesses+=1
    if num>user_input:
        user_input=int(input("Enter  a larger number\n"))
    elif num<user_input:
        user_input=int(input("Enter a smaller number\n"))
if num==user_input :
    guesses+=1
    print("You guessed the right number.")
    print("Number of guesses :",guesses)