import random

# ----------------------------
# Game Constants
# ----------------------------
WORDS = ["python", "apple", "chair", "tiger", "cloud"]
MAX_ATTEMPTS = 6

# ----------------------------
# Game Functions
# ----------------------------

def get_random_word():
    """Select a random word from the predefined list."""
    return random.choice(WORDS)

def get_display_word(secret_word, guessed_letters):
    """Returns the word with guessed letters shown and underscores for unguessed letters."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)

def is_valid_guess(guess):
    """Checks if the guess is a single alphabet letter."""
    return len(guess) == 1 and guess.isalpha()

def already_guessed(guess, guessed_letters):
    """Checks if the letter has already been guessed."""
    return guess in guessed_letters

def has_won(secret_word, guessed_letters):
    """Returns True if all letters in the secret word are guessed."""
    return all(letter in guessed_letters for letter in secret_word)

def has_lost(incorrect_attempts):
    """Returns True if incorrect attempts have reached the maximum limit."""
    return incorrect_attempts >= MAX_ATTEMPTS