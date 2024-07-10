def get_user_choice():
    """
    Function to get and validate user choice for rock, paper, or scissors.
    """
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    """
    Function to randomly generate computer's choice for rock, paper, or scissors.
    """
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the game based on choices.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    play_again = True
    while play_again:
        # Get user's choice
        user_choice = get_user_choice()
        
        # Get computer's choice
        computer_choice = get_computer_choice()

        # Print choices made by user and computer
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine and print the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask user if they want to play again
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False

    print("Thanks for playing!")

if __name__ == "__main__":
    main()