from random import choice

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice1 = (input("left or right")).lower()
if choice1 == "left":
    choice2 = input(' You have arrived at a mysterious ship.'
                ' There is a island that you can see.'
                ' Do u wanna "wait" for the boat.'
                ' Or wanna "swim" to the island.\n').lower()
    if choice2 == "wait":
        choice3 = input('You waited for the boat.'
                        ' Then you took the boat to the island.'
                        ' Once you have arrived at the island.'
                        ' You see a house with 3 different doors.'
                        ' "Red","Blue" and "Yellow".\n').lower()
        if choice3 == "red":
            print("GAME OVER. You fell into a fire-pit.")
        elif choice3 == "blue":
            print("GAME OVER. You were eaten by a monster")
        elif choice3 == "yellow":
            print("Congratulations. You found the treasure")
        else:
            print("You choose a door that doesnt exist. GAME OVER.")
    else:
        print("You got attacked by a angry trout.GAME OVER")
else:
    print("You fall into a hole. GAME OVER")