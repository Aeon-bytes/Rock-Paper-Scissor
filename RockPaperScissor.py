import random


def check_result(user_choice, computer_choice):
    if computer_choice == user_choice:
        return -1
    if user_choice == "rock" and computer_choice == "paper":
        return 0
    elif user_choice == "paper" and computer_choice == "rock":
        return 0
    if user_choice == "rock" and computer_choice == "scissor":
        return 1
    elif user_choice == "scissor" and computer_choice == "rock":
        return 0
    if user_choice == "paper" and computer_choice == "scissor":
        return 0
    elif user_choice == "scissor" and computer_choice == "paper":
        return 1


def play_game():
    computer = ["rock", "paper", "scissor"]
    computer_choice = random.choice(computer)
    check = True
    while check:
        user_choice = input("Enter your choice(rock/paper/scissor): ")
        if user_choice == "rock" or user_choice == "paper" or user_choice == "scissor":
            result = check_result(user_choice, computer_choice)
            if result == -1:
                print("Draw.")
            elif result == 0:
                print("Oh no! You Lose.")
            elif result == 1:
                print("You Win!!")
            print(f"Your choice is {user_choice} and computer's choice is {computer_choice}.")
            check = False
        else:
            print("Enter an Valid input.")


print("Rock Paper Scissors!!")
print("*******************************************")
game_mode = True

while game_mode:
    game = input("Do you wanna play a game of Rock Paper Scissors(yes/no): ")
    if game == "yes":
        play_game()
    else:
        game_mode = False
