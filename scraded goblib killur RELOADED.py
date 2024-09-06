goblino = ("You see a goblin sitting in the grass")

name = input("enter name: ")
print(name, "go kill some goblin argh")
choice1 = input("Type 1 to go find a goblin, 2 to go explore the town: ")
if choice1 == "1":
    print(goblino)
    goblinchoice1 = input("try to kill the goblin? Y/N: ")
    if goblinchoice1 == "Y" or goblinchoice1 == "y":
        print("You go to attack the goblin but you have no weapon.")
        print("It easily escapes.")
        print("You have failed.")
    if goblinchoice1 == "N" or goblinchoice1 == "n":
        print("You do not kill the goblin, it continues its buisiness")
        print("You have failed.")
elif choice1 == "2":
    storechoice = input("you go into town and find a weapon store. Go in? Y/N: ")
    if storechoice == "N" or storechoice == "n":
        print("you do not go into the store")
    if storechoice == "Y" or storechoice == "y":
        print("you go into the store and buy a sword. You are now ready to kill a goblin")       
else:
    print("you do nothing for the rest of time")
        
    
