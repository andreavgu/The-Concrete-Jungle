# Andrea Guillen
# April 2, 2023
# This is my own functions for our RPG game



# Return type: 1 int for choice
# Parameters: none
# Purpose: Display menu of choices 1) Play, 2) Rules, 3) Scores, 4) Quit
# and get users choice
# Define display_menu function
def display_menu():
    # Declare and initialize int variable for choice
    choice = 0
    # Display menu 1) Play 2) Rules 3) High score 4) Quit
    print("1) Play\n2) Rules\n3) High Score\n4) Quit")
    
    # Get users menu choice and validate it
    while choice < 1 or choice > 4:
        try:
            choice = int(input("\nPlease enter your choice here: "))
            if choice == 1:
                print("You chose PLAY. Okay get ready to start!...\n")
            elif choice == 2:
                print("You chose RULES. Okay Rules coming...")
                print()
            elif choice == 3:
                print("You chose HIGH SCORES. Okay High Score coming")
            elif choice == 4:
                print("You chose QUIT. Oh okay... :(")
            else:
                print("Please enter a number from 1-4 only")
        except:
            print("Please enter a number only")
    
    
    # Return choice
    return choice

# Return type: none
# Parameters: 1 str for name, 1 int for moves they have made
# Purpose: Display Scene info user is in (moves they did)
# Define DispSceneInfo function
def DispSceneInfo(tname, tStagesCleared):
    #Display moves they have done so far by name
    print(f"\nOkay {tname} so far you have cleared {tStagesCleared} stages")
    print("You're almost there, keep going!\n")


        
    
    
    












