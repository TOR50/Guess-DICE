import random

def print_dice(n,m):
    for i in range(len(n)):
        print(n[i],"  ",m[i])

if __name__=="__main__":
    print("DICE GUESS GAME")
    print("Rules:")
    print("1) AI throws dice")
    print("2) User needs to guess the number on dice")
    print("3) if user guess it correctly +10 pts")
    print("4) if user guess it wrong 0 pts added")
    print("5) user can play this game as many times as he wants")
    print()
    print("press any key to start and 'exit' to quit:")
    print()
    dice = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        )
    }
    choice=input("Enter your choice: ")
    # print(dice[userinput],dice(random.randint(1,6)))
    while True:
        if choice == "exit":
            exit()

        else:
            score,n_turns=0,0
            while True:
                ai=random.randint(1,6)
                print()
                userinput=input("Guess the number: ")
                # print(dice[userinput])
                if userinput=="exit":
                    print("Thanks for playing the game!!")
                    print("you played",n_turns,"times")
                    print("your final scores is :",score)
                    exit()
                elif userinput!="exit" and (userinput.isalpha() or userinput==""):

                    print("wrong input or not input given")
                elif int(userinput)>6 or int(userinput)<1:
                    print("number entered is either greater than 6 or less than 1, please give a correct input!!")
                elif ai==int(userinput):
                    # print(dice[ai],dice[int(userinput)])
                    print_dice(dice[ai],dice[int(userinput)])
                    print("--------------RESULT---------------")
                    print("Good job u guessed it right")
                    print("+10 pts")
                    score+=10
                    n_turns+=1
                    print("number of turns",n_turns)
                    print("score:",score)
                else:
                    print_dice(dice[ai],dice[int(userinput)])
                    n_turns+=1
                    print("--------------RESULT---------------")
                    print("oops! you guessed the wrong number")
                    print("number of turns",n_turns)
                    
                    print("score:",score)