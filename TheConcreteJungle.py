# Andrea Guillen
# April 2, 2023
# This is the main function for our RPG game

#import functions
import random
from time import sleep
from Andreafunctions import display_menu, DispSceneInfo
from Giansfunctions import attack, rest
from Samsfunctions import CalculateScore, CheckStats, ReadHighScore

# Define main function
def main():
    
    # Declare and initialize variables ; health, money, damage
    gold = itemChoice = invCount = onionCount = frogCount = potionCount = 0
    # Declare and initialize constants ; enemy type, items
    play_again = "yes"
    # String for users name, user choices
    user_name = menu_choice = ""

    # Display intro
    print(f"\n{'*' * 40:^60}\n")
    print('Welcome to "The Concrete Forest!"'.center(60)) #center
    print(f"\n{'*'* 40:^60}\n")
    
    # Prompt user for name
    user_name = input("Hello Ricky the raccoon! Enter your new name here: ").capitalize()
    
    # Display menu options
    while play_again == "yes":
        health = 100
        StagesCleared = 0
        # If user picks play
        menu_choice = display_menu()
        if menu_choice == 1:
            # Introduce the world
            sleep(1)
            print(f"Hey {user_name} the racoon, you're sadly lost in the jungle")
            sleep(.2)
            print("In order to find your way back home you are given choices with different paths to take")
            sleep(.2)
            print("Along the way you might find food to keep you going or items that can either help or hurt you\n")
            sleep(.2)
            print("Good luck!\n\n")
            
            # Lay out scene for player
            print("As you step forward, you see a path leading into a dense forest. The air is thick with the scent of pine and you can hear the sound of rustling leaves in the wind.")
            print("You take your first steps into the forest, ready for adventure.\n")
            # Game progress is loop of the following
            while StagesCleared <= 4:
                if health > 0:
                    # Provide player with choice
                    print()
                    print("What do you want to do?")
                    print("1. Explore")
                    print("2. Shop")
                    print("3. Rest")
                    print("4. Check Stats")
                    print("5. Check Scene")
                    print("6. Quit")
                    action_choice = input("Enter your choice: ")
                    print()
                    # Switch scene based on player choice
                    if action_choice == "1":
                        if StagesCleared == 0:
                            print("You continue down the path, ready to explore the forest. As you walk, you come across a river blocking your path.")
                            # Give player an obstacle
                            print("What do you want to do?")
                            print("1. Try to cross the river")
                            print("2. Follow the river upstream")
                            obstacle_choice = input("Enter your choice: ")
                            print()
                            
                            # Swtich scene
                            if obstacle_choice == "1":
                                print("""You try to cross the river, but the current is too strong and you're swept downstream.
    You manage to grab onto a nearby branch and pull yourself ashore, but you're soaking wet and your health has decreased. At least you found an onion and added it to your inventory!""")
                                invCount += 1
                                onionCount += 1
                                health -= 10
                                StagesCleared += 1
                                
                            elif obstacle_choice == "2":
                                print("You follow the river upstream and come across a bridge. You found a frog and added it to your inventory. You cross the bridge safely and continue on your journey.")
                                invCount += 1
                                frogCount += 1
                                StagesCleared += 1
                                
                        elif StagesCleared == 1:
                            print("You come across an enemy!")
                            print("1. Fight?")
                            print("2. RUN!")
                            fighting_choice = input("Enter your choice: ")
                            
                            # Swtich scene
                            if fighting_choice == "1":
                                attackFunc = attack(health, gold)
                                StagesCleared += 1
                                
                            elif fighting_choice == "2":
                                print("You try to run away from the rabid squirell but it pounces on you scratching you up!")
                                health -= 25
                                StagesCleared += 1
                                
                            #Display Scene info
                            DispSceneInfo(user_name, StagesCleared)
                            
                        elif StagesCleared == 2:
                            print("""You find yourself lost in a dense forest and stumble upon a hidden cave. Inside,
    you find a mysterious object that glows with an eerie light. You hear strange whispers in your head, and you must decide whether to touch the object or leave it alone.""")
                            print("1. Touch the object?")
                            print("2. Leave now!")
                            obstacle_choice2 = input("Enter your choice: ")
                            # Swtich scene
                            if obstacle_choice2 == "1":
                                print(f"Touching the object the voice proclaims 'AH {user_name} YOU'VE MADE THE RIGHT DECISION FREEING ME, HERE IS A TOKEN OF MY GRATITUDE.")
                                gold += 250
                                StagesCleared += 1
                            elif obstacle_choice2 == "2":
                                print(f"Walking past the orb you hear '{user_name} i've always known you were a loser' this hurts your pride. But you now have one more frog in your inventory")
                                #Calculate new stats
                                invCount += 1
                                frogCount += 1
                                health -= 10
                                StagesCleared += 1
                                
                            #Display scene info 
                            DispSceneInfo(user_name, StagesCleared)
                            
                        elif StagesCleared == 3:
                            print("""You hear a loud roar and turn to see a massive dragon flying towards you.
    You realize that you have accidentally wandered into its territory, and you must decide whether to stand your ground and fight or run for your life.""")
                            print("1. Fight the dragon.?")
                            print("2. Run for your life!")
                            fighting_choice2 = input("Enter your choice: ")
                            # Swtich scene
                            if fighting_choice2 == "1":
                                print("Foolishly you taunt the dragon and ready yourself for a fight. The dragon swoops down a swallows you whole.")
                                #Calculate new stats
                                health -= 100
                                StagesCleared += 1
                                
                            elif fighting_choice2 == "2":
                                print("Cautionslly you sneak past the dragon with as little as a peep")
                                StagesCleared += 1
                            #Display Scene info
                            DispSceneInfo(user_name, StagesCleared)
                                
                        elif StagesCleared == 4:
                            print("""You come across a treacherous mountain pass that is notorious for deadly rockslides.
    You must navigate through the pass and avoid falling rocks, or risk being buried alive.""")
                            print("1. Try to navigate through the pass.")
                            print("2. Find an alternate route.")
                            obstacle_choice3 = input("Enter your choice: ")
                            # Swtich scene
                            if obstacle_choice == "1":
                                print("You brace yourself for the sprint through the mountainside, luckily you make it through the other side unharmed")
                                StagesCleared += 1
                            elif obstacle_choice == "2":
                                print("Searching for another path around you slip down the side injuring your leg")
                                health -= 50
                            StagesCleared += 1
                            
                            #Display scene info
                            DispSceneInfo(user_name, StagesCleared)
                            
                        elif action_choice == "6":
                            print("Sadly you died!")
                    
                        
                        
                    elif action_choice == "2":
                        print("You come across a small village and decide to check out the shops. As you enter the first shop, you're greeted by the shopkeeper.")
                        # Wait for play action
                        print("What do you want to do?")
                        print("1. Buy a potion")
                        print("2. Sell some items")
                        shop_choice = input("Enter your choice: ")
                        
                        # Swtich scene
                        if shop_choice == "1":
                            print("You buy a potion and add it to your inventory.")
                            invCount += 1
                            potionCount += 1
                            gold -= 10
                        elif shop_choice == "2":
                            print("You sell some items and make some extra gold.")
                            gold += 20

                    #Action Choice 3
                    elif action_choice == "3":
                        # call rest function
                        # Downtime
                        resting = rest(health, gold)
                                            
                    elif action_choice == "4":
                        CheckStats(invCount,health,gold)
                        # Downtime;
                    elif action_choice == "5":
                        DispSceneInfo(user_name, StagesCleared)
                        
                    elif action_choice == "6":
                        print("Thanks for playing!")
                        break
                    
                    else:
                        print("Invalid choice. Please try again.")
                        
                    
                else:
                    print("Oh looks like your health is at or less than 0, therefore, your life has been terminated")
                    break
                #calculate score
                score = CalculateScore(StagesCleared)

                #make the high scores file 
                with open("high_scores.txt", "w") as outfile:
                    print(f"\nName: {user_name}", file = outfile)
                    print(f"Score: {score}\n", file = outfile)
                    
            
                        
        # Else if user picks rules display the rules
        elif menu_choice == 2:
            print("""The Rules Are: The rules are: you have to go through each scene to gain points,
but be careful as there could be an enemy around the corner ready to attack! Fend off the enemy and conquer the obstacles in your path to gain points!""")
        # Else if user picks High score to beat display such
        elif menu_choice == 3:
            HighScore = ReadHighScore()
            print(f"\nThe High score is: {HighScore}\n") #import from outfile
            
        # Else user picked QUIT the game, display sad outro
        else:
            print(f"\nYou will be missed {user_name} the raccoon... :(")

        play_again = input("\nThat was a nice game! do you want to play again? (yes or no): ").lower()

    # Display outro
    print(f"\n\nThanks for trying to escape The Concrete Jungle!")


    
# Call main function
main()




