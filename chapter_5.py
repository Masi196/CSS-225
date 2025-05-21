def chapter_5():
    print("You step through the final gate")

    # action 1: walk toward the pedestal

    print("\nIn the of the room stand a pedestal. ")
    print("You walk toward the pedestal. ")

    # action 2: inspect the treasure

    print("\nat the top of pesetal is the treasure you have been seeking. ")
    print("its a shining artiifact. ")

    # action 3: player choses to take or leave the artificat


    choice = input("\nDo yo want to take the artificat? (yes or no): ").lower()



    if choice == "yes":
        print("\n you reach out and take the artifat")

        # action 4: Exit the chamber as the story ends
        print("\nAhidden passage opens behind you.")
        print("You walk out of the chamber")
        print("Your journey is complete. ")

    if choice == "no":
        print("some treasures are best left untocuhed.")

        # action 4: Exit the chamber as the story ends

        print("You walk away, leaving the glowing artifact. ")
        print("You ends with peace. ")
    else:
        print("\nYou stand in silence, unable to decide. ")
              
