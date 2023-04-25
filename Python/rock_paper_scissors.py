import random

def rock_paper_scissors():

    playing = True
    name = input("Whats your name?")
    round = 0
    player_counter = 0
    computer_counter = 0

    while playing == True:

        round =+ 1
        player = input("Pick between rock, paper and scissors! ")

        computer_paper = False
        computer_rock = False
        computer_scissors = False

        computer = random.randint(1,3)
        if computer == 1:
            computer_rock = True
            computer = "rock"
        elif computer == 2:
            computer_paper = True
            computer = "paper"
        elif computer == 3:
            computer_scissors = True
            computer = "scissors"

        if player.lower() == "rock":
            if computer_scissors == True:
                print("You Win! I chose", computer)
                player_counter += 1
            elif computer_paper == True:
                print("I chose", computer, "I win!")
                computer_counter += 1
            elif computer_rock == True:
                print("Gah Damn. Its a draw!")

        if player.lower() == "paper":
            if computer_rock == True:
                print("You Win! I chose", computer)
                player_counter += 1
            elif computer_scissors == True:
                print("I chose", computer, "I win!")
                computer_counter += 1
            elif computer_paper == True:
                print("Gah Damn. Its a draw!")

        if player.lower() == "scissors":
            if computer_paper == True:
                print("You Win! I chose", computer)
                player_counter += 1
            elif computer_rock == True:
                print("I chose", computer, "I win!")
                computer_counter += 1
            elif computer_scissors == True:
                print("Gah Damn. Its a draw!")
            
        print("")
        print("The score is:")
        print("Round:", round)
        print(name, ":", player_counter)
        print("computer : ", computer_counter)
        playagain = input("do you want to play again?")
        if playagain.lower() == "no":
            playing = False
        elif playagain.lower == "yes":
            pass

rock_paper_scissors()
