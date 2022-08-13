import random # importing the random module

# gets a random number between 1-100
num=random.randint(1,100)

# gets a user input (a number but a string)
user_input=input("Guess the number between 1-100\n")

# number of gusses user takes to gues the number
guesses=0

# while loop to continuously prompt the user to guess a number until he guesses the right number
while user_input!=num:

    # try...except statement for error handling if he dosen't enter a valid value
    try:
        
        # if the user inputs a valid value then convert it to a int from str
        user_input=int(user_input)
    except:

        # to ask the user for a valid value
        print("Please enter a valid value")
        user_input=input("Enter the number between 1-100\n")

        # to skip to the next execution of while for getting a valid value
        # if the user input an invalid value again
        continue

    # number of guesses +1
    guesses+=1

    # if user input is less than the number
    if num>user_input:
        user_input=int(input("Enter  a larger number\n"))

    # if user input is greater than the number
    elif num<user_input:
        user_input=int(input("Enter a smaller number\n"))

# if user guesses the right number 
if num==user_input :

    # number of guesses +1
    guesses+=1

    # to display the result and number of guesses taken
    print("You guessed the right number.")
    print("Number of guesses :",guesses)