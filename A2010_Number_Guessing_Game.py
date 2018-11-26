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




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    Guess my  number between 1-9:   6
#    Wrong Guess, Try Again
#    Total Attempts  =  1
#    **************************
#    Enter number between 1-9 :  4
#    Wrong Guess, Try Again
#    Total Attempts  =  2
#    **************************
#    Enter number between 1-9 :  7
#    Number Guessed is correct
#    Total Attempts  =  3
