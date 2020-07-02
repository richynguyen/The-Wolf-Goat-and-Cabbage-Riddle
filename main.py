import random
East=['C','F','G','W']
West=[]
Forbidden=[['c','g','w'],['c','g'],['g','w']]


#Complete the following function so it Prints the objects at East and then the objects at West===========================
def PrintContains(East,West):

    #Display Lists
    print("East:")
    for k in East:
        print(k)
    print("\nWest:")
    for k in West:
        print(k)
   
    return 


#Go West: Complete this function according to the instructions on HW4
def GoWest(East,West):

    #Forbidden Loop/Choice
    if East != ["G","W"] and East != ["C","G"] and East != ["C","G","W"]:

        #Move Farmer West
        East.sort()
        #print(East)
        if "F" in East:
            East.remove("F")
        if "F" not in West:
            West.append("F")
            West.sort()
   
        #RNG Choice
        random_choice = random.choice(East)
        #print("EAST RANDOM CHOICEEEEEE")
        #print(random_choice,"\n")
        #print("EASTTTTTTT")
        #print(East,"\n")     

        #Cabbage Choice
        if random_choice == "C":
            if "F" in East:
                East.remove("F")
            if "F" not in West:
                West.append("F")
                West.sort()    
            if "C" in East:
                East.remove("C")
            if "C" not in West:
                West.append("C")
                West.sort()

            #FORBIDDEN GOAT/WOLF
            if East == ["G","W"]: 
                West.remove("C")
                East.append("C")
                if "F" in West:
                    West.remove("F")
                if "F" not in East:
                    East.append("F")
                    East.sort() 
                    West.sort()            

        #Goat Choice
        if random_choice == "G":
            if "G" in East:
                East.remove("G")
            if "G" not in West:
                West.append("G")
                West.sort()        

        #Wolf Choice
        if random_choice == "W":
            if "F" in East:
                East.remove("F")
            if "F" not in West:
                West.append("F")
            if "W" in East:
                East.remove("W")
            if "W" not in West:
                West.append("W")
                West.sort()

            #FORBIDDEN CABBAGE/GOAT
            if East == ["C","G"]: 
                West.remove("W")
                East.append("W")
                if "F" in West:
                    West.remove("F")
                if "F" not in East:
                    East.append("F")
                    East.sort() 
                    West.sort()            


    PrintContains(East,West)
    print('-------------------------------------\n')
    return  East, West
    
    
#Go East: Complete this function according to the instructions on HW4   
def GoEast(East,West):

    #Move Farmer East
    West.sort()
    if West != ["C","F","G","W"]:
        if "F" in West:
            West.remove("F")
        if "F" not in East:
            East.append("F")
            East.sort()   

    #FORBIDDEN CABBAGE/GOAT
    if West == ["C","G"]:

        #RNG Choice
        random_choice2 = random.choice(West)
        #print("WEST RANDOM CHOICEEEEEE")
        #print(random_choice2,"\n")        

        #Move Farmer
        if "F" in East:
            East.remove("F")
        if "F" not in West:
            West.append("F")

        #Cabbage Choice
        if random_choice2 == "C":
            if "C" in West:
                West.remove("C")
            if "C" not in East:
                East.append("C")
            if "F" in West:
                West.remove("F")
            if "F" not in East:
                East.append("F")
                West.sort()
                East.sort()

        #Goat Choice
        if random_choice2 == "G":
            if "G" in West:
                West.remove("G")
            if "G" not in East:
                East.append("G")
            if "F" in West:
                West.remove("F")
            if "F" not in East:
                East.append("F")
                West.sort()
                East.sort()            

    #FORBIDDEN GOAT/WOLF
    if West == ["G","W"]:

        #RNG Choice
        random_choice2 = random.choice(West)
        #print("WEST RANDOM CHOICEEEEEE")
        #print(random_choice2,"\n")            

        #Move Farmer
        if "F" in East:
            East.remove("F")
        if "F" not in West:
            West.append("F")

        #Goat Choice
        if random_choice2 == "G":
            if "G" in West:
                West.remove("G")
            if "G" not in East:
                East.append("G")
            if "F" in West:
                West.remove("F")
            if "F" not in East:
                East.append("F")
                West.sort()
                East.sort()

        #Wolf Choice
        if random_choice2 == "W":
            if "W" in West:
                West.remove("W")
            if "W" not in East:
                East.append("W")
            if "F" in West:
                West.remove("F")
            if "F" not in East:
                East.append("F")
                West.sort()
                East.sort()            


    PrintContains(East,West)
    print('-------------------------------------\n')    
    return  East, West
    
    
# Solution: This function returns True if all objects are on the West side otherwise returns False (One line of code)    
def Solution():

    #End
    if West == ["C","F","G","W"]:
        return condition == True


#Do not change anything in the following lines. Your job is to complete the functions above.
PrintContains(East,West)
print('-------------------------------------')  
condition=True
while condition:
    East, West=GoWest(East,West)
    if not Solution():
       East, West=GoEast(East,West)
    else:
     condition=False
