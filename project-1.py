import random

def game():
    choices = ["rock", "paper", "scissors"]

    while True:
        try:
            player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

            if player_choice not in choices:
                raise ValueError("Invalid choice")

            computer_choice = random.choice(choices)

            print(f"Player chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie game")
            elif (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper") or \
                 (player_choice == "rock" and computer_choice == "scissors"):
                print("You won ")
            else:
                print("Computer wins ")


        except ValueError:
            print(" Please enter only rock, paper, or scissors.")
game()
while True:
    again = input("Play again? (yes/no): ").lower()
    if again == "no":
        break

print("Thanks for playing ")