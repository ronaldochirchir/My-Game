# Number Guessing Game with CLI and ORM

A Python application that combines a Command Line Interface (CLI) with Object-Relational Mapping (ORM). The game allows users to guess a number between 0 and 10 and stores their game history in a SQLite database.

## Features

- **CLI**: Interact with the game via the terminal.
- **ORM**: Manage players and game history using SQLite.
- **Gameplay**: Guess a number between 0 and 10.
- **History**: View game history for each player.
- **Error Handling**: Validates user input and handles errors gracefully.

## How to Run

### Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of using the terminal or command prompt.

### Steps to Run the Game

1. **Clone the Repository (if applicable)**:
    ```sh
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Set Up the Virtual Environment**:
    ```sh
    python -m venv env
    ```

3. **Activate the Virtual Environment**:
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```

4. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run Database Migrations (if applicable)**:
    ```sh
    python models.py migrate
    ```

6. **Run the Game**:
    - To play the game:
        ```sh
        python main.py play
        ```
    - To view game history:
        ```sh
        python main.py history
        ```

## Project Structure

cli_orm_project/
├── requirements.txt      # Contains project dependencies
├── README.md             # Project description and instructions
├── main.py               # Main entry point for the CLI application
├── models.py             # Contains ORM models and database-related code
├── migrations/           # Directory for database migrations (if applicable)
└── game.db               # SQLite database file


# Number Guessing Game with CLI and ORM

A Python application that combines a Command Line Interface (CLI) with Object-Relational Mapping (ORM). The game allows users to guess a number between 0 and 10 and stores their game history in a SQLite database.

## Features

- **CLI**: Interact with the game via the terminal.
- **ORM**: Manage players and game history using SQLite.
- **Gameplay**: Guess a number between 0 and 10.
- **History**: View game history for each player.
- **Error Handling**: Validates user input and handles errors gracefully.

## How to Run

### Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of using the terminal or command prompt.

### Steps to Run the Game

1. **Clone the Repository (if applicable)**:
    ```sh
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Set Up the Virtual Environment**:
    ```sh
    python -m venv env
    ```

3. **Activate the Virtual Environment**:
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```

4. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run Database Migrations (if applicable)**:
    ```sh
    python models.py migrate
    ```

6. **Run the Game**:
    - To play the game:
        ```sh
        python main.py play
        ```
    - To view game history:
        ```sh
        python main.py history
        ```

## Project Structure

```
cli_orm_project/
├── requirements.txt      # Contains project dependencies
├── README.md             # Project description and instructions
├── main.py               # Main entry point for the CLI application
├── models.py             # Contains ORM models and database-related code
├── migrations/           # Directory for database migrations (if applicable)
└── game.db               # SQLite database file
```

## Dependencies

The project uses the following Python libraries:

- **Click**: For building the CLI interface.
- **SQLAlchemy**: For handling the database ORM.
- **SQLite**: Lightweight database solution.

You can install the dependencies by running:
```sh
pip install -r requirements.txt
```

## Usage

### Playing the Game

Run the following command:
```sh
python main.py play
```

- Enter your name and the target number (between 0 and 10).
- Start guessing! The game will tell you if your guess is too high or too low.
- Once you guess the correct number, your score will be saved.

### Viewing Game History

Run the following command:
```sh
python main.py history
```

- Enter the player's name to view their game history.

## Example Output

### Gameplay

```sh
$ python main.py play
Enter your name: Alice
Enter the target number (0-10): 7
Enter your guess: 5
Too low!
Enter your guess: 8
Too high!
Enter your guess: 7
Congratulations! You guessed the number in 3 attempts.
```

### Game History

```sh
$ python main.py history
Enter player name: Alice
Game history for Alice:
Attempts: 3, Target Number: 7
```

## Code Organization

- **main.py**: Contains the CLI logic using the Click library.
- **models.py**: Contains the ORM layer for managing players and games.
- **migrations/**: Directory for database migrations (if applicable).
- **game.db**: SQLite database file that stores player and game data.

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear and descriptive messages.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- **Click Library**: For simplifying CLI development.
- **SQLAlchemy**: For providing an ORM for database interactions.
- **SQLite**: For providing a lightweight and easy-to-use database.

## Contact

For questions or feedback, please contact:

- **Gmail**:ronaldochirchir8@gmail.com
- **GitHub**:ronaldochirchir
