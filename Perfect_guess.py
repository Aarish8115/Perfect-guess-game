import random

a=random.randint(1,100)

b=int(input("Guess the number between 1-100\n"))
guesses=0
while b!=a:
    guesses+=1
    if a>b:
        b=int(input("Enter  a larger number\n"))
    elif a<b:
        b=int(input("Enter a smaller number\n"))
if a==b :
    guesses+=1
    print("You guessed the right number.")
    print("Number of guesses :",guesses)