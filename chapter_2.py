


import random

def chapter_2():
    print("You arrive at the shrine ")


    #action 1: examine the shrine for the clues
    
    clues = ["You notice carvings of an ancient symbol",
             "There is a crack in the stone wall, something was moved",
             "A path of bent grass goes behind the shrine "]
    
    random.shuffle(clues)
    print("\nYou examine the shrine closely. ")
    print("- " + clues[0])



    # action 2: find and follow the hidden path


    print("\nYou step behind the shrine and find a narrow, hidden path. ")
    print("You follow the hidden path. ")


    # action 3: collect a strange symbol carved in stone

    print("\nAs you walk, you notice something sticking out of a tree trunk. ")
    print("It's a small flat stone with a glowing symbol carved into it. You take it with you. ")


    #action 4: avoid traps
    traps = [
        "You duck just in time to avoid a falling log trap. ",
        "You stop short before stepping into a pit covered in leaves. ",
        "You hear a click and jump back as arrows shoot out from the bushes. "]
    
    random.shuffle(traps)
    print("\nAs you walk, you sense danger. ")
    print("- " + traps[0])
    



chapter_2()

