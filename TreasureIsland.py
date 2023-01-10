from art import picture
print(picture)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
lr = input('You\'re at a crossroad. Want to go "left" or "right" ? ').lower()
if lr == "left":
    sw = input("Want to swim or wait ? ").lower()
    if sw == "wait":
        door = input("Which door (B/R/Y)")
        if door == "Y":
            print("You win!!")
        elif door == "R":
            print("Burned by fire \nGame over")
        elif door == "B":
            print("Eaten by beasts \nGame over")
        else:
            print("Game over")
    else:
        print("Attacked by trout\nGame over")
else:
    print("Fall into a hole.\nGame over")