print('''
                  _____
                 _|[]_|_
               _/_/=|_\_\_
             _/_ /==| _\ _\_
           _/__ /===|_ _\ __\_
         _/_ _ /====| ___\  __\_
       _/ __ _/=====|_ ___\ ___ \_
     _/ ___ _/======| ____ \_  __ \_
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this side 👇
direction = input("Which direction do you want to go? Left or Right: ")

if direction.lower() == "left":
    action = input("Do you want to swim across the river or wait? ")
    if action.lower() == "wait":
        door = input("Which door would you like to choose? Red, Yellow, or Blue: ")
        if door.lower() == "red":
            print("\nYou were engulfed by flames. Game Over.")
        elif door.lower() == "yellow":
            print("\nCongratulations! You've found the hidden treasure. You Win!")
        elif door.lower() == "blue":
            print("\nYou were devoured by ferocious beasts. Game Over.")
        else:
            print("\nYou hesitated too long. Game Over.")
    else:
        print("\nYou were attacked by a school of aggressive trout. Game Over.")
else:
    print("\nYou fell into a dark hole. Game Over.")