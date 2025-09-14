def entertocontuine():
    input("\n<<press [ENTER!] to continue!>>\n")

print("\n<<Welcome traveler, to the rolling hills of Dew Drop Valley! You have come just in time!>>\n")

print("""You see, the dreaded dic-tartor Catomus Maximus has invaded the Valley and treatens to takeover all the prospourus farm lands for us local folk. Not even the highest quailty cat-nip will appease his greed and stave off the onsalught of his kitten army.""")
entertocontuine()

willhelp = True
while willhelp:     
    Travelerschoice = input ("Will you help us in our time of dire need?! y/n:")  
    if Travelerschoice in ["Y","y","Yes","yes","YES"]:  
        print("That is WONDERFUL news!")
        entertocontuine() 
        willhelp = False
    elif Travelerschoice in ["n","NO","no","Nooooooo","N"]:
        print("You are not the GOAT! How Bahhhhhad of you!")
        print("You lose the game.")
        exit()
        willhelp = False 
    else:print("Maybe next time, thanks for trying traveler!")
    print("n\<<Now it's time to choose your race! Here in Dew Drop Valley we have 3 common races, Bear, Dog, and Cat! I Can't wait to see what you pick!>>\n")
race = True
while race:
    Avatar = input ("Pick one to advance!:")
    if Avatar.casefold() == "bear":
        print("Bear! How did know that wa my favorite, you will be strong in battel.")
        race = False
    elif Avatar.casefold() == "dog":
        print("Dog, hu! WOW, how did you know that was my favorite! Aruuuu, you will be very wise and a great ally in the field.")
        race = False
    elif Avatar.casefold() == "cat":
        print("How meowity of you, how did you know Cat was my favorite! You will be a cunning and quick competitor.")
        race = False
    else: print("Hmmm, that was not one of the options, sorry adventurer we need to blend in to hide from the terriable Catomus Maximus.")

print("Now its time to choose your job!")
    