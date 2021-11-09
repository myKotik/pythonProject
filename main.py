import random

print("Rock, Paper, Scissors")


def try_again():
    rps = ["Rock", "Paper", "Scissors"]
    computer = random.choice(rps)

    player = input("your choice: ").lower().capitalize()

    if computer =="Rock":
        if player =="Rock":
            print(f"I chose {computer}, you chose {player}\nit's a tie!")
        elif player == "Paper":
                print(f"I chose {computer}, you chose {player}\nYou win!")
        elif player =="Scissors":
            print(f"I chose {computer}, you chose {player}\n You lost!")
    elif computer =="Paper":
        if player =="Rock":
            print(f"I chose {computer}, you chose {player}\n You lost!")
        elif player == "Paper":
                print(f"I chose {computer}, you chose {player}\nit's a tie!")
        elif player =="Scissors":
            print(f"I chose {computer}, you chose {player}\nYou win!")
    elif computer =="Scissors":
        if player =="Rock":
            print(f"I chose {computer}, you chose {player}\nYou win!")
        elif player == "Paper":
                print(f"I chose {computer}, you chose {player}\n You lost!")
        elif player =="Scissors":
            print(f"I chose {computer}, you chose {player}\nit's a tie!")
    play_again = input("Do you want to play again? yes or no: ").lower().capitalize()
    # If the player says yes, go back to the function
    if play_again == "Yes":
        try_again()
    # If the player says no, say goodbye
    elif play_again == "No":
        print("Goodbye")


# End of function
try_again()