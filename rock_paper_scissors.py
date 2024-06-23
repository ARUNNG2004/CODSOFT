import random

def get_user():
    print("""
    1. Rock
    2. Paper
    3. Scissors
    """)
    choice = input("Enter your choice (1/2/3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        return 'rock'
    elif choice == '2':
        return 'paper'
    elif choice == '3':
        return 'scissors'

def get_computer():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if winner == "tie":
        print("tie game")
    elif winner == "user":
        print("user win😊")
    else:
        print("user lose😒")

def main():
    user_score = 0
    computer_score = 0

    while True:
        user = get_user()
        computer = get_computer()
        winner = determine_winner(user, computer)
        display_result(user, computer, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}")

        play_again = input("\n play another round (y/n): ").lower()
        if play_again != 'y':
            break

    print(f"\nFinal Score: You {user_score} - Computer {computer_score}")

if __name__ == "__main__":
    main()
