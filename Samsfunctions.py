# Samantha Kavanagh
# April 29th, 2023
# Function for users score, stats, highest score, and collected items


# Return type: 1 int for total score
# Parameters: 1 int for stages cleared
# Purpose: Calculates users total score based on how many stages cleared
# Define function Calculate score
def CalculateScore(StagesCleared):
       # Calculate the score based on stages cleared and enemies encountered
    StageScore = StagesCleared * 100  # Each stage cleared is worth 1000 points

   
    print("\nYour total score is:", StageScore)
    return StageScore



# Return type: none
# Parameters: 1 str for users inventory and name, 3 int for users health, money, and strength
# Purpose: Check the users stats in a game to see their health, money, strength,
# and inventory
# Define CheckStats function
def CheckStats(inventory,health,money):
    #Display users current stats in game
    print("Here are your current stats in the game:")
    print(f"Health: {health}")
    print(f"Gold: ${money}")
    print(f"Inventory: {inventory} items")


# Return type: 1 int for high score
# Parameters: none
# Purpose: Reads the high score value from file, converts into an int, and returns it
# Define ReadHighScore function

def ReadHighScore():
    with open("high_scores.txt", "r") as infile:
        high_score = infile.read()
    return high_score

    

