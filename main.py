from models import NumberGuessingGame, initialize_database

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 0 and 10. Can you guess it?")  # Updated range

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_hint(hint):
    print(hint)

def display_win_message(attempts):
    print(f"Congratulations! You guessed the number in {attempts} attempts.")

def ask_for_replay():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")

def display_game_history():
    print("\nGame History:")
    history = NumberGuessingGame.get_game_history()
    for row in history:
        print(f"Player: {row[1]}, Attempts: {row[2]}, Target Number: {row[3]}")

def main():
    initialize_database()
    game = NumberGuessingGame()
    while True:
        display_welcome_message()
        play_game(game)
        if not ask_for_replay():
            display_game_history()
            print("Thank you for playing! Goodbye!")
            break

def play_game(game):
    game.reset_game()
    while True:
        guess = get_user_guess()
        hint = game.check_guess(guess)
        if hint == "Correct!":
            display_win_message(game.attempts)
            player_name = input("Enter your name to save your score: ")
            game.save_game_history(player_name)
            break
        else:
            display_hint(hint)

if __name__ == "__main__":
    main()