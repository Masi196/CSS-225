

import random


def chapter_3():
    print("you enter a glowing cave filled with crystals. ")



    #Action 1: Explore the cave chambers

    print("You chose a chamber. ")

    chamber1= ["Wide chamber with glwoing floor"]
    chamber2=["Small chamber with gems carved into walls"]
    chamber3=["Chamber with a winding hallway that makes a humming sound"]

    input("chose the chamebr you want to check first( chamber 1 , chamber 2, or chamber 3")
    if input  == "chamber 1":
        print(chamber1)
    elif input == "chamber 2":
        print(chamber2)
    elif input == "chamber 3":
        print(chamber3)
    else:
        print("restart chapter 3")
        

   
    print("\nYou explore the cave the chambers. ")
    


    #action 2: read ancient carvings for clues
    carvings = [
        "You read symbols the seem to tell a story about a sealed power. ",
        "The carvings mention a puzzle that must be solved to continue. ",
        "You see repeating symbols: a circle and a flame. "]
    
    random.shuffle(carvings)
    print("\nYou examine the ancient carvings on the wall. ")
    print("- " + carvings[0])



    #action 3: Solve a simple puzzle in the wall

    print("\nYou find puzzle carved into stone with three symbols <, ^, >. ")
    print("You press them in the order you saw earlier: <, ^, >. ")
    print("A soft rumble follows as part of the wall slides open. ")


    #action 4: Discover a sealed stnne door deeper inside

    print("\nAs you go deeper, you find a massive stone door sealed shut. ")
    

chapter_3()

    


    




