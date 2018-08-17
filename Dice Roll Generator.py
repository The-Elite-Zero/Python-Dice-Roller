#------------------------------------------------------------------------------
# Dice Rolling Simulator
#
# 5/28/2018 - Winston Wedgeworth
#
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Imports

import random
import os

#------------------------------------------------------------------------------
#
# This program simulates rolling dice, and is designed (currently) to run on 
# linux based operating systems, however can be modified to work on Windows if
# necessary. 
# (Only the clear screen function needs to be changed -- Lines 58, 64)
#
#------------------------------------------------------------------------------
# Notes
#
# Program could be shortened within the 'rolling dice portion' by creating one
# function and performing rolls with parameters for specific dice.
#
# Done - 6/1/2018 - Winston Wedgeworth III
#
# Look into Menu() for issue with recalling Menu() and "any number"
#
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
        user_choice = int(user_choice) # Conversion   
    except: print('\n')
    
    if user_choice in range(1, 9):
        print("\nHow many times would you like to roll?")
        roll_number = raw_input(">> ")  

        try:
            roll_number = int(roll_number) # Conversion
        except: print('\n')      
           
        if isinstance(roll_number, int):
            dice_choice(user_choice, roll_number)
            
        else:
            print("Sorry, that is an invalid input, try a number.")
            os.system('clear') # Linux clear screen
            #os.system('cls') # Windows clear screen
            Menu() # Retry
            
    else:
        print("Sorry, that is an invalid input, try numbers 1-8.")
        os.system('clear') # Linux clear screen
        #os.system('cls') # Windows clear screen
        Menu() # Retry

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

def roll_dice(name, dice_size, rolls):
    
    print("\n")
    print("Rolling ", name, " ", rolls, " time(s)")
    print("\n")
    roll_list = []
    
    # Pushes roll onto the back of a list for addition and printing
    for x in range (0, rolls):
        roll_list.append(random.randint(1, dice_size))
        
    # Prints dice roll totals and numbers rolled
    print("Total: ", sum (roll_list))
    print("\n")
    print("Your rolls are: ", roll_list)
        
    del roll_list
    roll_again() 

#------------------------------------------------------------------------------

def dice_choice(dice, amount):
    
    if dice == 1:
        roll_dice('d20', 20, amount)
    elif dice == 2:
        roll_dice('d12', 12, amount)
    elif dice == 3:
        roll_dice('d10', 10, amount)
    elif dice == 4:
        roll_dice('d8', 8, amount)
    elif dice == 5:
        roll_dice('d6', 6, amount)
    elif dice == 6:
        roll_dice('d4', 4, amount)
    elif dice == 7:
        roll_dice('d2', 2, amount)      
    elif dice == 8:
        roll_dice('d100', 100, amount)       
    else: 
        print("Fail Programmer, Fail!!!")
    
#------------------------------------------------------------------------------ 

def print_menu():
    
    menu = """
    1: d20
    2: d12
    3: d10
    4: d8
    5: d6
    6: d4
    7: d2
    8: d100
    """
     
    print(menu)
    
Menu()

#------------------------------------------------------------------------------
