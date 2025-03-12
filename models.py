import sqlite3
import random

# Database setup
def initialize_database():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT,
            attempts INTEGER,
            target_number INTEGER
        )
    ''')
    conn.commit()
    conn.close()

class NumberGuessingGame:
    def __init__(self, min_num=0, max_num=10):  # Range updated to 0–10
        self.min_num = min_num
        self.max_num = max_num
        self.target_number = random.randint(min_num, max_num)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.target_number:
            return "Too low!"
        elif guess > self.target_number:
            return "Too high!"
        else:
            return "Correct!"

    def reset_game(self):
        self.target_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0

    def save_game_history(self, player_name):
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO game_history (player_name, attempts, target_number)
            VALUES (?, ?, ?)
        ''', (player_name, self.attempts, self.target_number))
        conn.commit()
        conn.close()

    @staticmethod
    def get_game_history():
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM game_history')
        rows = cursor.fetchall()
        conn.close()
        return rows