print ("Text based game prototype")
def gameend():
    endchoice = int(input("\n\nGame over.\n1. Try again.\n2. Die forever.\nYour choice: "))
    if endchoice == 1:
        choice1 = gamestart()
        gamesecond(choice1)
    elif endchoice == 2:
        print("Exiting...")
    else:
        print("Invalid input. Try again.\n\n")
        gameend()

def gamestart():
    print("\n\nWelcome to Kasra's text based game!\nHow to play: there well be numbers you can pick as routes you may take in the game.\nPick wisely! or you may end up dead...")
    print("\nYou are in a forest. You have three paths ahead of you. The left path seems the most promising.")
    choice1 = int(input("1. Take the left path.\n2. Go straight ahead.\n3. Take the right path.\nYour choice: "))
    return choice1

def gamesecond(choice1):
    if choice1 == 1:
        print("You took the left path and it seems like it was the correct option!\n\n at the end of the path you see a big house. What will you do?\n")
        choice2 = int(input("1. Look around the house\n2. Enter the house\n3. Scream for help!\n4. Go back the way you came.\nYour choice: "))
        gamethree(choice2)
    elif choice1 == 2:
        print("You took the straight path and fell into a pit of spike. You are now dead.")
        gameend()
    elif choice1 == 3:
        print("You took the right path and got attacked by a bear. You are now dead.")
        gameend()
    else:
        print("Not a valid option. Try again.\n\n")
        choice1 = gamestart()
        gamesecond(choice1)

def gamethree(choice2):
    if choice2 == 1:
        print("You tried to look around the house but you stepped into a bear trap and died.")
        gameend()
    elif choice2 == 2:
        print("you enter the house... and find a man attacking you with an axe!\nDefend yourself and defeat him!\n\nBoss fight!")
        gamefour()
    elif choice2 == 3:
        print("You tried screaming for help and attracted a bear who proceeded to eat you.")
        gameend()
    elif choice2 == 4:
        print("You tried to go back the way you came but you got lost and accidentally fell into a pit of spikes.")
        gameend()
    else:
        choice2 = gamesecond()
        gamethree(choice2)

def gamefour():
    playerHP = 40
    bossHP = 30
    while playerHP > 0:
        print("\n\nYour health is:", playerHP,"Boss health:", bossHP)
        fightchoice = int(input("1. Attack! (10 damage)\n2. Heal (5 health)\nYour choice: "))
        if fightchoice == 1:
            bossHP = bossHP - 10
            print("You attacked the boss! the boss loses 10 health!")
            if bossHP == 0:
               break
        elif fightchoice == 2:
            playerHP = playerHP + 5
            print("\n+5 HP to you. your health is now:", playerHP)
        else:
            print("\nInvalid choice! you just stood there watching. The boss attacks you anyway.")
        for i in range(2):
            playerHP = playerHP - 5
            print("\nYou've been hit by the boss! you lose 10 health! your health is now:", playerHP)
            if playerHP <= 0:
                break
    if playerHP > 0:
        print("You defeated the boss!\nYou win the game!")
    else:
        print("The boss killed you.")
        gameend()


choice1 = gamestart()
gamesecond(choice1)