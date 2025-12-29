import random

def game():
    choices = ["rock", "paper", "scissors"]

    try:
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if player_choice not in choices:
            raise ValueError

        computer_choice = random.choice(choices)

        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie game")
        elif (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "rock" and computer_choice == "scissors"):
            print("You won")
        else:
            print("Computer wins")

    except ValueError:
        print("Error: Please enter only rock, paper, or scissors.")

while True:
    game()

    try:
        again = input("Play again? (yes/no): ").lower()
        if again not in ["yes", "no"]:
            raise ValueError

        if again == "no":
            print("Thanks for playing")
            break

    except ValueError:
        print("Error: Please type only yes or no.")
