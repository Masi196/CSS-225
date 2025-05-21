
import random

def chapter_1():

    global playername
    playername = input("entr your name")
    


    #action walk through the village and observe the surroundings
    print("walk throug the village and observe")

    surroundings = ["old stone house", "old empthy house",
      "a rusty lantern flickering in the wind",
      "a strange statue covered in moss near the village sqaure" ]
    


    for scene in surroundings:
        print("- " + scene)



    #action 2: talk to a few villagers
    npc_names= ["Dexter", "Ryan", "Dawn", "Andie"]

    responses = [
        "strane things happen at night",
        "the treasure i know nothing",
        "walks away silently",
        "you are not the first to come looking",
        "only fools chase old legends"]
    

    random.shuffle(npc_names)
    random.shuffle(responses)


    npc = npc_names[0]
    response = responses[0]




    print(f"\n{npc}: Hello, i am {npc}. would you like to talk to me?")
    choice = input("press 'y' to talk or press any key to walk away: ").lower()
    if choice =='y':
        print(f"{npc}: {response}")

    else:
        print(f"{npc}:... Very well.")




    #action 3: pay th villager and get information about the village
    villager = "Dexter"

    print(f"\n you gave a few coins to {villager}, who hesitates before accepting them. ")
    print(f"{villager}: you can find an old map of the entire village and its hidden layout near well, south of the village. ")


    #action 4: find an old map fragment near the village well
    print("\n you examine the well and found something tucked into stone. ")
    print("you found an old map fragment. ")



chapter_1()
