print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
# The player is prompted to choose between "left" or "right" at a crossroad.
choice1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ")
# If the player chooses "left", the game proceeds with another set of choices:
if choice1.lower() == "left":
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    # If the player chooses "wait", the game proceeds with another set of choices:
    if choice2.lower() == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ")
        # Depending on the door chosen, different outcomes are printed:
        if choice3.lower() == "red":
            # If the player chooses "red", they are trapped in a room full of fire and the game ends.
            print("It's a room full of fire. Game Over.")
        elif choice3.lower() == "yellow":
            # If the player chooses "yellow", they find the treasure and win the game.
            print("You found the treasure! You Win!")
        elif choice3.lower() == "blue":
            # If the player chooses "blue", the game ends with a message:
            print("You enter a room of beasts. Game Over.")
        else:
            # Any other input results in choosing a non-existent door (Game Over).
            print("You chose a door that doesn't exist. Game Over.")
    else:
        # If the player chooses "right" at the crossroad:
        print("You chose an option that doesn't exist. Game Over.")
else:
    print("You fell into a hole. Game Over.")
