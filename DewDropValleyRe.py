import sys
import random
import time

#Function with no parameter

def enterToContinue():
    input("Press [ENTER!] to continue!")

#Grass function
def printGrass():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣇⠀⣀⠀⠀⢀⣠⡶⢟⣩⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⢤⣤⣄⡀⠀⢀⡿⣿⣼⣻⢁⣴⠟⢥⣿⠟⠁⠀⠀⠀⠀⠀⠀⣄⠀⢠⣾⡏⢀⣠⣾⠆⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠻⣝⠳⣾⡇⣿⠃⣯⠞⠁⣰⡟⠁⠀⠀⠀⠀⠀⠀⢠⠀⢿⢧⣺⠉⣿⠞⣹⣏⣤⣶⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⠀⠁⠈⠐⠏⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡾⠌⠳⠀⠈⠀⠙⠁⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⣷⠀⠀⠀⠀⡄⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣾⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⡿⠀⢹⠀⢀⣴⡾⢻⡆⠀⢸⡿⣆⠀⠀⢀⣠⢀⣴⠞⣩⡾⣁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⢦⣄⢸⡇⠀⢸⣶⢿⡿⠀⡌⠳⠀⣼⠇⣿⢠⡼⣿⣿⡟⠁⢠⣟⣥⣼⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢶⣦⣌⣷⠙⢿⡇⠀⢸⠇⣿⣠⡾⠻⡕⣴⡏⠀⣽⠏⠀⣿⠋⠀⠀⣿⡟⢩⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠙⡇⠀⠀⠀⠈⠀⠹⠏⠀⠀⠙⠟⠀⠀⠀⠀⠀⠉⠀⠀⠀⠸⠷⣾⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⣄⠀⢰⡏⣸⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⢠⣧⠀⠀⢀⣀⠀⠀
⠀⢠⣿⠙⣦⡟⢠⣿⣿⢏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⣀⠀⠀⣿⢿⡄⣸⡿⣿⣤⡶⣿⠏⠀⠀
⣐⣟⢹⡆⠘⡇⢸⠟⣿⡼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡏⠛⢦⡏⠀⢻⠏⠀⣽⠛⢱⣿⣴⣷⠄
⠉⢻⡟⠓⠀⡇⠃⢸⡟⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣬⣧⡀⠀⠃⠀⠀⠀⠀⠁⠀⠀⠟⠿⠃⠀
⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠷⠶⠶⣬⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

def catMax():
    print("""⠀⠀⠀⠀⠀
       ⢀⡞⠉⠒⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠒⠉⠛⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡘⠁⢀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⣠⢖⣋⠀⠀⢀⣀⠀⠀⡸⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠇⢀⡸⠉⠉⠲⣄⠀⠉⢲⡀⠀⠀⣠⠞⠋⢈⡴⣚⡉⠁⠀⡇⠀⣨⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢼⡆⠈⣧⠀⠀⢀⠬⠓⠂⠉⠉⠉⠉⠉⠑⢶⡯⡀⠀⠀⠀⠐⡇⠀⣽⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⠇⠀⢣⡤⠊⣹⠓⠢⣄⠀⠀⠀⣠⠖⠊⠉⡇⠈⠑⢤⡀⢸⠀⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣇⡴⠃⠀⣀⣏⡀⠀⠈⢳⣠⠊⠁⠀⠀⣠⡧⠤⢄⡀⠈⢫⡀⢀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⠀⡽⢹⣿⠋⣡⡴⢿⣆⠀⠀⠀⠀⠀⢀⡞⢹⣌⣷⡀⢻⢳⡆⢱⡜⠀⣀⠀⠀⠀⠀⠀
⠀⢰⠋⢹⢠⠃⢸⡇⢠⡿⢶⣾⣿⡇⠀⠀⠀⠀⣼⣿⣿⣿⣯⠇⢸⡾⠀⠀⡇⢠⠏⢣⠀⠀⠀⠀
⢀⡇⠀⠀⠛⠄⠀⢧⠈⣿⣯⣿⢿⡇⠺⠿⠃⠀⢿⡻⣛⢱⠟⢠⡾⠁⠀⠐⠛⠁⠀⢸⠀⠀⠀⠀
⠀⠱⣄⠀⠀⡀⠀⠈⠓⠬⣛⣤⡞⠀⢀⣀⡀⢈⣠⠟⠋⠁⠒⠋⠀⠀⢀⡀⠀⢀⡠⠋⠀⠀⠀⠀
⠀⣠⠔⢋⣉⡡⠀⠀⠀⠀⠀⠀⠉⠻⣟⣽⣿⣿⠈⠀⠀⠀⠀⠀⠀⠀⢠⣉⠙⠫⢤⠤⢤⣀⠀⠀
⠀⠈⠉⢁⡞⠀⠀⣠⠀⠀⠀⠀⠀⠀⢻⡟⢻⠇⠀⠀⠀⠀⠀⠀⡄⠀⠀⢸⠉⠉⠒⠃⠀⣈⡵⠄
⠀⠀⠀⠘⢆⠀⠘⢋⠑⠤⣄⡀⠀⠀⠀⠉⠁⠀⠀⠀⢀⣠⠤⣾⡗⠀⢀⣼⣀⡀⠀⠀⢠⡏⠀⠀
⠀⠀⠀⠀⠀⠑⠒⠈⠂⠸⣶⣾⣯⡷⣒⣶⢶⣖⣚⣿⣷⣶⣿⣻⠇⠒⠋⠀⠀⠉⠉⠁⢸⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣗⣿⢿⣿⣿⣿⡿⠃⠈⠙⠲⡄⠀⠀⠀⠀⢀⡾⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢿⠷⣶⠚⠷⢦⣤⣿⠿⠇⠀⢰⠀⠀⠸⡒⠦⢄⡴⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠸⢎⣹⠿⡅⠀⠀⠀⣆⡀⠀⠀⠀⢣⠀⠀⣵⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⢹⠦⢧⠀⠀⠀⡿⡛⣄⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠰⡇⢸⠀⠀⢀⣷⡇⠈⢢⡀⠀⢱⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⡇⢸⠀⠀⢸⡿⠁⠀⠀⠃⠀⢸⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⣠⠇⠦⣀⣀⡟⠁⠀⠀⠀⠧⠬⠋⠀⠀⠀⠀⠀⠀⠀""")

# Travel Function Nested loop
def travel(travelTime = 1):
    for setTime in range(travelTime):
        printGrass()
        print("You continue traveling")
        for dotTime in range(5):
            if dotTime == 3:
                break
            else:
                print(". ")
                time.sleep(0.5)
        setTime =+ 1

# 3B - Function with one parameter
    # Get skill bonus, calculate total skill, then print.
def skillCheck(skill):
    playerRoll = random.randrange(1,21)
    skillResult = playerRoll + skill
    if playerRoll == 20:
        print("Critical Sucess!!")
        playerRoll = 31
        return playerRoll
    elif playerRoll == 1:
        print("Critical Failure!!")
        playerRoll = 30
        return playerRoll
    else:
        print("You rolled a ", playerRoll, "with a ", skill, " modifier, that makes a total of ", skillResult, ".")
        return skillResult

# 3F - Function with a default parameter
    #Grab user Name
def playerName(playerName = "player"):
    userName = input("What is your name?: ")
    if not userName:
        playerName = userName
        print("Welcome, ", playerName)
        return playerName
    else:
        playerName = userName
        print("Welcome, ", playerName)
        return playerName

#4B Recursion
def playerWeapon(sharpObject):
    playerInventory = []
    inventoryCheck = 0
    if sharpObject in playerInventory:
        print(f"{avatarName} you already have one of those!")
    elif sharpObject not in playerInventory and inventoryCheck == 0:
        playerInventory.append(sharpObject)
        inventoryCheck == 1
        return playerInventory
    else:
        playerWeapon(playerInventory)
        inventoryCheck == 0
        



#Introduction
print("""It's 2am here in the real world, your finding it hard to sleep 
so you reach for your gameboi green and load in your new game, Dew Drop Valley.
You hear a soft hum as the opening music plays a soft guitar melody and the screen comes to life.""") 
enterToContinue()
print("The game loads to the main screen where you see the pixel art of a farmer and his dog with some trees."
"You hit the A button and off you travel.")
enterToContinue()
print("""Its a cold winter morning, but the first true frost has yet to hit the valley. 
There is dew on the ground as you hear the crunch of grass under your boots.
Off in the distance the sun is starting to peak over the faraway hills.""")
travel()
enterToContinue()

print("You come to a crossroads, you can see a village off in the distance to the left.")
time.sleep(0.1)
travelChoice = input("Would you like to head towards it? Y/N: ").lower()
if travelChoice in ["y", "yes", "YES", "Yeah",]:
    print("You head towards the village.")
    enterToContinue()
else:
    print("You continue on as the village becomes a small ant like fixture of houses, grass and trees in your past. ")
    exit()

travel(3)
print("You get closer to the village.")
travel()
print("As you continue to walk, grass gives way to a well worn path of dirt that slowly becomes a thoughtfully crafted sandstone path. ")
enterToContinue()
travel()
print('''Before you is a large iron gate with a brick wall on either side that seems to span for miles.
Hanging to the side overhead is a wooden sign that reads, "Welcome to Dew Drop Valley".''')
enterToContinue()


#player-name 

print("You hear a voice call from between the iron bars, Hello there traveler welcome! : ")
avatarName = playerName()
print(f"Ah,{avatarName} thats a fine name, you can see a forlorn smile as he continues to speak, happy to have you visit Dew Drop Valley... ")
enterToContinue()
print("...sorry to inform you but its not the best time to vacation here I am afriad. ")
print("""You see, the dreaded over-lord Catomus Maximus who hails from the near by world Mewotopia, 
has started invading the outskirts of the Valley! Their world is running out of Spice-Milk and
not even the highest quailty cat-nip has appeased their greed.. we may soon be taken over by the onsalught of his spice hungry kitten army.""")


willhelp = True
while willhelp:     
    Travelerschoice = input ("Not all is lost though it seems, we could use another soilder, will you help us in our time of dire need?! Y/N:")  
    if Travelerschoice in ["Y","y","Yes","yes","YES"]:  
        print("That is WONDERFUL news!")
        enterToContinue()
        willhelp = False
    elif Travelerschoice in ["n","NO","no","Nooooooo","N"]:
        print("Thats most unfortunate"", they say as they usher you away from the gate!")
        enterToContinue()
        print("Have a nice day, see you again some time if the world is still here.")
        enterToContinue()
        print("You did not see them again, the world was devoured by the giant cat overlord, you lose.")
        travel()
        catMax()
        exit()
        
        willhelp = False 
    else:
        print("It seems you have not made up your mind just yet...maybe soon, thanks for trying traveler!")
    
    
    print(f"Hizzza {avatarName}! We are so greatful you decided to join us in our fight!")
    enterToContinue()
    print("""You hear the jingle of heavy keys and a click through the gameboi's small speaker, 
    the gate swings open and you see the farmer from the main screen come into view.
    He is wearing a red flannel, denim jeans and worn boots. He greets you with warm eyes and begans to speak, I'm Charlie.""")
    enterToContinue()

    print("He steps aside and you enter the village through the gate, this way he gestures as he guides you further in towards some buidlings.")
    travel()
    print("Now that your here lets get you suited up for battel.")
    enterToContinue()
    print("First, it's time to choose your race! Here in Dew Drop Valley we have 3 common races, Bear, Dog, and Cat! I Can't wait to see what you pick!")

race = True
while race:
    Avatar = input ("Pick one to advance!:")
    if Avatar.casefold() == "bear":
        print("Bear! How did know that was my favorite, you will be strong in battel.")
        race = False
    elif Avatar.casefold() == "dog":
        print("Dog, hu! WOW, how did you know that was my favorite! Aruuuu, you will be very wise and a great ally in the field.")
        race = False
    elif Avatar.casefold() == "cat":
        print("How meowity of you, how did you know Cat was my favorite! You will be a cunning and quick competitor.")
        race = False
    else: print("Hmmm, that was not one of the options, sorry adventurer we need to blend in to hide from the terriable Catomus Maximus.")

print("Now its time to choose your job!")
enterToContinue()
Job = True 
while Job:
    Occupation = input ("There are 3 options to pick from for your job: farmer, fighter, healer. ")
    if Occupation.casefold() == "farmer":
        print("Nice we could always use more Farmers!")
        Job = False
    elif Occupation.casefold() == "fighter":
        print("That is perfect, one more set of paws to aid in the fight against Catomous Maximus as we gorw our own army!")
        Job = False
    elif Occupation.casefold() == "healer":
        print("Healer! What a rare and wonderful chocie. There can never be to many healers!")
        Job = False
    else: print("It seems you want to join the ranks of our unempolyment line. We don't need more idel hands please choose a job!")
    
print(f"What great choices, Well done {avatarName}! Your help as {Occupation} will come in handy. Not to mention your {Avatar} shape shift is my favorite!")

# Choose a weapon
print("Now that we know what and who you are let's make your final choice! What weapon will you wield. Here are your options... ")
weapon = ["Sword", "Healing staff", "Pitch fork", "Axe", "Sheild"]
weaponList = ["sword", "healing staff", "pitch fork", "axe", "sheild"]
for numberweapon in weapon:
    print (numberweapon)

weaponChoose = True
while weaponChoose:
    avatarWeapon = str(input("What weapon will you choose?: ").lower())
    print(avatarWeapon)
    if avatarWeapon in weaponList:
        playerInventory = playerWeapon(avatarWeapon)
        print(f"Good choice, you have {playerInventory}!")
    else:
        print("that is not one of the weapons we have.")
        continue
    
    weaponInput = input("Would you like to choose another weapon? Y/N : ")
    if weaponInput in ["y", "yes", "YES", "Yeah",]: 
        weaponChoose = True
    else:
        weaponChoose = False












