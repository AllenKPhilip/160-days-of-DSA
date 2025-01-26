'''
Author:ALLEN K PHILIP
Description:program to create a simple game:-STICK GAME.
'''


print("""Welcome to the Stick Game.
Description: The player to pick the last stick loses the game.
Rules:
This is a two player game.
16 sticks are on the table.
Each player can picks one set of sticks during his/her turn.
A set contains 1, 2, or 3 sticks.""")


person1=input("enter the name:")
person2=input("enter the name:")
stick=16
while stick!=0:
    #player1
    if stick!=0:
        print(stick)
        choice=int(input(f"{person1},The no: of sticks player can take 1,2 or 3:"))
        
        while  stick<choice or choice<=0 :
            print("please enter the choice within the range!")
            choice=int(input(f"{person1},The no: of sticks player can take 1,2 or 3:"))
        stick=stick-choice
        player=person1    

    #player2
    if stick!=0:
        print(stick)
        choice = int(input(f"{person2},The no: of sticks player can take 1,2 or 3:"))
        
        while stick < choice or choice<=0  :
            print("please enter the choice within the range!")
            choice=int(input(f"{person2},The no: of sticks player can take 1,2 or 3:"))
        stick=stick-choice
        player=person2    


if stick==0:
    print(f"{player}, is the loser.")
