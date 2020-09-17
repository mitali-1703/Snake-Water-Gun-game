#Snake, Water, Gun Game
import random
k=0
j=0
i=1
list=["Snake","Water","Gun"]
while(i<=10):
    print("Press 's' for snake,'w' for water,'g' for gun")
    a=input()
    choice = random.choice(list)
    print("PC chose", choice)
    if(a=='s' and choice=="Snake"):
        print("Tie so nobody gets a point")
    elif(a=='w' and choice=="Water"):
        print("Tie so nobody gets a point")
    elif(a=='g' and choice=="Gun"):
        print("Tie so nobody gets a point")
    elif(a=='s' and choice=="Water"):
        j=j+1
        print("You got",j,"point")
    elif (a == 's' and choice == "Gun"):
        k = k + 1
        print("PC got", k, "point")
    elif (a == 'w' and choice == "Gun"):
        j = j + 1
        print("You got", j, "point")
    elif (a == 'w' and choice == "Snake"):
        k = k + 1
        print("PC got", k, "point")
    elif (a == 'g' and choice == "Snake"):
        j = j + 1
        print("You got", j, "point")
    elif (a == 'g' and choice == "Water"):
        k = k + 1
        print("PC got", k, "point")
    i=i+1
print("\nChances over!!")
if (k>j):
    print("\nPC won the game...Better luck next time!!")
else:
    print("Congo!! You won the game")

