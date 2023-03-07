#Greet the user and provide instructions
print(f"Hello there brave adventurer! We have a grave situation in our once prosperous land! ")
print(f"Before we begin, Do give us your name. After typing an answer, press enter.")

userName = input("\nEnter your name:  ")
while len(userName) == 0:
    userName = input("A brave soul like you should have a name!  Please enter your name:  ")	
print(f"\nHello, {userName}. We are delighted to meet you!")
input(f"\nPress the enter key to continue...")

print(f"\nLet's begin with a few questions to help us on our journey!")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    

#5 Questions Before the story begins
#First Question
    chooseSupplies = input(f"\nWhat is your favorite cooking utensil?:  ")
    while len(chooseSupplies) == 0:
        chooseSupplies = input(f"Please enter a utensil:  ")

#Second Question
    weaponChoice = input(f"If you were stranded on an island, and you could only bring one thing, what would it be?:  ")
    while len(weaponChoice) == 0:
        weaponChoice = input(f"Please enter a thing:  ")

#Third Question
    rallyCall = input(f"What is something you would chant before a big game?:  ")
    while len(rallyCall) == 0:
        rallyCall = input(f"Please enter a chant:  ")

#Fourth Question
    darkWoods = input(f"What is one thing you use in the dark?:  ")
    while len(darkWoods) == 0:
        darkWoods = input(f"Please enter something you use in the dark:  ")

#Fifth Question
    scaryMonster = input(f"What animal are you afraid of?:  ")
    while len(scaryMonster) == 0:
        scaryMonster = input(f"Please enter an animal:  ")
#Story Start
    print(f"\nNow we are ready to GO!!")
    print(f"While walking in the woods, you stumble upon a distressed creature.")
    print(f"You begin to walk a little closer and ask the poor creature, Are you alright?.")
    print(f"The startled creature jumps and frantically replies, ABSOLUTELY NOT! Do I look alright to you?! You reply, Ok! well just calm down Sir. What is your name?")
    print(f"The creature replies, I am Sir Boggles, right hand ROUS to Princess Grape Propel!AND she has been lured away by the ruthless Smores!?! Will you help me save her??")

#Decision 1
    helpBoggles = input("Do you choose to help Sir Boggles save the princess? yes or no: ")
    while helpBoggles.lower() != "yes" and helpBoggles.lower() != "no":
        helpBoggles = input("Please type yes or no:  ")

    if helpBoggles == "yes":
        print(f"\nYou begin walking through the woods on the path to save a Princess, and stumble upon a tavern filled with people of the woods.")
        print(f"As you and Sir Boggles enter the tavern,  He announces, I am Sir Boggles and this is {userName}!")
        print(f"We are going to save Princess Grape Propel and we need your help!")
        print(f"You stand on the table and yell {rallyCall}! The people in the tavern erupt in excitement and agree to help on this quest.")
        print(f"Everyone begins the journey through the deep forest to the Land of Marshmellows.")
        print(f"You pullout your trusty {darkWoods}, to help guide the way.")
        print(f"You begin to smell the burned mallows and molten hot chocolate volcanos. You know you're close.")
        print(f"You reach a giant cliff that opens the forest into a dark, charred, sticky mess of destruction.")
        print(f"Everyone looks at the burned land with sadness, and a wave of fear comes over your tired group of recruited worriors.")
        print(f"We take shelter in the woods and plan our attack!")
        print(f"You see the King of The Smores, and know that he can be taken by surprise. The plan is in place, and now it is time to go to battle!")
    else: 
        print(f"\nWell fine! I didn't need your help anyways {userName}!!! Good luck finding your way home in these woods!")
        print(f"You turn away in shame and begin looking for a way home.")
        print(f"As you are walking, your bag gets really heavy and you decide to leave {chooseSupplies} behind.")
        print(f"You hear something coming closer to you, and you grab your {darkWoods} to see what could possibly be there.")
        print(f"All of a sudden, a huge {scaryMonster} jumps from the brush and begins to chase you!")
        print(f"While running for your life, you trip and fall into a deep cave.")
        print(f"You pull out {weaponChoice} to try and help crawl out of the deep cave, but it fails.")

    #Decision 2
    goToBattle = input(f"\nDo you choose to go to battle with the Smores?! Type yes or no:  ")
    while goToBattle.lower() != "yes" and goToBattle.lower() != "no":
        goToBattle = input("Please type yes or no:  ")


    if goToBattle == "yes":
        print(f"\nYou gather the people of the woods and yell, {rallyCall}!!!")
        print(f"You pull out your {weaponChoice} and lead the charge into the dark realm of the Smores!")
        print(f"As you approach the King, a giant {scaryMonster} leaps out in front of you!")
        print(f"You raise your {weaponChoice} and lunge toward the monster slicing it to pieces!")
        print(f"The beast falls to the ground and you once again head for the King.")
        print(f"The King is now ready for your fight, and sees you heading straight for him!")
        print(f"You scream out one more {rallyCall} and the people of the owwds charge the King with you!")
        print(f"You raise your {weaponChoice} and slice the King of the Mallows in half!")
        print(f"The land erupts in celebration for the demise of the King!! And suddenly the once dark clouds leave and reveal the once beautiful land of the Mallows.")
        print(f"You hear the Princess calling {userName} and run to the dungeons!")
    else:
        print(f"\nYou yell for help, but the cave is too deep for anyone to hear your calls.")
        print(f"The more you try to escape, the more tired your get.")
        print(f"A wave of fear comes over you, as you begin to think you will never make it home.")
        print(f"Then, suddenly the ground begins to shake, and an opening appears!")
        print(f"You gather the strength to climb out of the cave!")

    #Alternate Endings 
    if helpBoggles == "yes" and goToBattle == "yes":
       print(f"\nYou run to the Princess and release her from her doom!")
       print(f"She is so thankful that she leaves the Land of Mallows in your hands to defend forever!")
       print(f"And in honor of your bravery she takes your {weaponChoice} and Knights you as {userName} Defender of The Mallows!")
       print(f"You live in the Kingdom of Chocolate and Mallows for the rest of your life.")
    elif helpBoggles == "no" and goToBattle == "no":
       print(f"\nYou lay on the ground tired and cold from the crawl out of the cave.")
       print(f"Suddenly you can see the sky change from dark doom, to a clear and sunny hopeful blue!")
       print(f"You sit up, and look around for any signs of life.")
       print(f"While the sky is now clear, and you seem out of danger, you never seem to find your way home and live in the woods forever.")
    else:
       print(f"\nThe battle is won! But, you feel homesick.")
       print(f"You leave the land of Chocolate and Mallows to go home.")
       print(f"Once home, you tell everyone of your great journey! And feel that you need more adventure!")
       print(f"So, you decide to bring your family to your new Kingdom, and live happily ever after!")

    print(f"\nThe End") 

    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")