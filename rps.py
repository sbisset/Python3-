# RPS but python 

import random 



def variables():
    global playerwins 
    global compwins
    playerwins = 0
    compwins = 0 

variables()


def comp_choice(): 
    global comp 
    comp = random.randint(1,3)
    

    if comp == 1:
        print ("Computer played: Rock")
    elif comp == 2: 
        print ("Computer played: Paper")
    else :
        print("Computer played: Scissors")


	
def player_choice()  :
    print ("""1)Rock
2)Paper
3)Scissors""") 
    global player 
    player = int(input("Your choice?: "))



def game(): 
    if player +1 == comp or (player == 3 and comp == 1):
        print("You Lose!")
        global compwins
        compwins += 1
    elif player == comp : 
        print("Its a tie!")
    else:
        print("You Win !")
        global playerwins
        playerwins += 1 

def printgamestats():
    global compwins
    print("Comp wins: ",compwins)
    global playerwins
    print("Player wins: ",playerwins)


while True :
    player_choice()
    comp_choice()
    game()
    printgamestats()
    if compwins == 3:
        print ("Computer wins!")
        break
    elif playerwins == 3 :
        print ("Player wins!")
        break

