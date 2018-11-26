# Number 7 Guessing Game

guess = int(input("Guess my  number between 1-9:   "))

count = 1
while (guess <= 9):
    if guess == 7:
        print("Number Guessed is correct")
        print("Total Attempts  = ",count)
        break
    else:
        print("Wrong Guess, Try Again")
        print("Total Attempts  = ",count)
        count= count+1
        print("**************************")
    guess =  int(input("Enter number between 1-9 :  "))    



