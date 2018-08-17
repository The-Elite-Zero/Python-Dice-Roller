#------------------------------------------------------------------------------
# Imports

import random
import os

#------------------------------------------------------------------------------
# Dice Rolling Simulator
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#
# This program simulates rolling dice, and is designed (currently) to run on 
# linux based operating systems, however can be modified to work on Windows if
# necessary. 
# (Only the clear screen function needs to be changed -- Lines 58, 64)
#
#------------------------------------------------------------------------------
# Program could be shortened within the 'rolling dice portion' by creating one
# function and performing rolls with parameters for specific dice.


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def Menu():
    
    '''
    Menu() is designed to take input from user, and pass it along to the dice
    rolling function afterward, while checking for input error (non-digits)
    from the user and catching them.
    '''
    
    print_menu() # Calls Menu for formatted printing
    
    print("What size dice would you like to roll?")
    user_choice = raw_input(">> ")
    
    try:
        user_choice = int(user_choice)    
    except: print('\n')
    
    if user_choice in range(1, 9):
        print("\nHow many times would you like to roll?")
        roll_number = raw_input(">> ")  

        try:
            roll_number = int(roll_number)
        except: print('\n')      
           
        if isinstance(roll_number, int):
            dice_choice(user_choice, roll_number)
            
        else:
            print("Sorry, that is an invalid input, try any number.")
            os.system('clear') # Linux clear screen
            #os.system('cls') # Windows clear screen
            Menu()
            
    else:
        print("Sorry, that is an invalid input, try numbers 1-8.")
        os.system('clear') # Linux clear screen
        #os.system('cls') # Windows clear screen
        Menu()  
        
    # Possible Try-Except Scenario?

#------------------------------------------------------------------------------

def roll_again():
    
    '''
    This is designed to repeat the menu to continue rolling if necessary or
    exit if not necessary.
    '''
    
    choice = raw_input("Would you like to roll again? (y/n): ").lower()
    yes = {'y', 'Y', 'yes', 'Yes'}
    no = {'n', 'N', 'no', 'No'}
    
    if choice in yes:
        Menu()
    elif choice in no:
        exit
    else:
        print("\n")
        print("You must make a choice of y, Y, yes, Yes, n, N, no or No.")
        print("\n")

        roll_again()        

#------------------------------------------------------------------------------

def roll_d20(rolls):
    
    print("\n")
    print("Rolling d20, ", rolls, " time(s)")
    print("\n")
    roll_list = []
    
    # Pushes roll onto the back of a list for addition and printing
    for x in range (0, rolls):
        roll_list.append(random.randint(1,20))
    
    print("Total: ", sum (roll_list))
    print("\n")
    print("Your rolls are: ", roll_list)
    
    del roll_list
    roll_again()        

   
#------------------------------------------------------------------------------
    
def roll_d12(rolls):
    
    print("\n")
    print("Rolling d12, ", rolls, " time(s)")
    print("\n")
    roll_list = []
    
    for x in range (0, rolls):
        roll_list.append(random.randint(1,12))
    
    print("Total: ", sum (roll_list))
    print("\n")
    print("Your rolls are: ", roll_list)
    
    del roll_list
    roll_again()        

    
#------------------------------------------------------------------------------

def roll_d10(rolls):
    
    print("\n")
    print("Rolling d10, ", rolls, " time(s)")
    print("\n")
    roll_list = []
    
#------------------------------------------------------------------------------
