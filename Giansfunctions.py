# Gian Fiecconi
# April 20, 2023
# This is the algorithm for our RPG game


# Import random for RNG
import random


# Return type: 1 string for outcomedamage, gold taken 
# Parameters: 1 int for health, 1 int for gold
# Purpose: Have the player attack an enemy
# Define attach(enemy) function
# Determine enemy based on RNG
# Calculate (rng) damage done by player
# Calculate (rng) damage taken by enemy
# Print outcome of damage
# Loop until enemy/player is defeated
# Reward or punish player
def attack(player_health, tgold):
    # Declare variables
    monster_health = 15
    # Determine enemy based on RNG
    enemies = ["jaguar", "alligator", "deer", "bear"]
    
    # Loop until enemy or player is defeated
    while monster_health > 0:
        enemy = random.choice(enemies)
        # Calculate (rng) damage done by player
        player_attack = random.randint(5, 15)
        monster_health -= player_attack
        
        # Check if enemy is defeated
        if monster_health <= 0:
            reward = random.randint(10, 50)
            tgold += reward
            print("\nYou defeated the " + enemy + " and gained " + str(reward) + " gold!")
        
        # Calculate (rng) damage taken by enemy
        enemy_attack = random.randint(5, 15)
        player_health -= enemy_attack
        
        # Check if player is defeated
        if player_health <= 0:
            print("\nYou were defeated by the " + enemy + "!")
        
        # Print outcome of damage
        print("\nYou attacked the " + enemy + " and did " + str(player_attack) + " damage.")
        print("\nThe " + enemy + " attacked you and did " + str(enemy_attack) + " damage.\n")
    
    # Should never get here, but just in case:
    return player_health, tgold




# Return type: 1 int for choice
# Parameters: player health
# Purpose: Heal the player by "resting"
# Define rest function
# Reset player_health upon interacting
def rest(thealth, tgold):
    #Declare and initialize variables
    tchoice = 0
    tnew_gold = 0
    print("Now you're resting. You see a few things around you that you can interact with...")
    print("1. Rest on the bed")
    print("2. Search the room")

    while tchoice != 1 and tchoice != 2:
        try:
            tchoice = int(input("What do you want to do? "))
            if tchoice == 1:
                thealth = 100
                print("You lie down on the bed and rest for a while, feeling rejuvenated!")
            elif choice == 2:
                tnew_gold = random.randint(1, 10)
                tgold += tnew_gold
                print("You search the room and find " + str(tnew_gold) + " gold coins!")
            else:
                print("Invalid choice. Please type a number (1 or 2)")
        except:
            print("Please type a number not a word.")

    return thealth, tgold


