import tkinter as tk
from game_logic import get_random_word, get_display_word, has_won, has_lost, MAX_ATTEMPTS

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Hangman Game")
        # Full window
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")

        # ----------------------------
        # Game State
        # ----------------------------
        self.secret_word = get_random_word()
        self.guessed_letters = []
        self.incorrect_attempts = 0

        # ----------------------------
        # Widgets
        # ----------------------------
        self.title_label = tk.Label(
            root, text="🎮 Hangman Game", font=("Helvetica", 36, "bold"), bg="#f0f0f0"
        )
        self.title_label.pack(pady=20)

        self.word_label = tk.Label(
            root, text="", font=("Courier New", 40, "bold"), bg="#ffffff",
            width=20, relief="solid", pady=20
        )
        self.word_label.pack(pady=20)

        self.info_label = tk.Label(
            root, text=f"Attempts remaining: {MAX_ATTEMPTS}", font=("Helvetica", 16), bg="#f0f0f0"
        )
        self.info_label.pack(pady=10)

        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=15)

        self.entry = tk.Entry(input_frame, font=("Helvetica", 24), width=3, justify="center")
        self.entry.grid(row=0, column=0, padx=10)

        self.guess_button = tk.Button(
            input_frame, text="Guess", font=("Helvetica", 16), command=self.make_guess,
            bg="#4CAF50", fg="white", width=10
        )
        self.guess_button.grid(row=0, column=1, padx=10)

        # Optional: Reset button for stability
        self.reset_button = tk.Button(
            root, text="🔄 Reset Game", font=("Helvetica", 14), command=self.reset_game,
            bg="#2196F3", fg="white", width=12
        )
        self.reset_button.pack(pady=10)

        # Initialize display
        self.update_display()

    # ----------------------------
    # Display Methods
    # ----------------------------
    def update_display(self):
        display = get_display_word(self.secret_word, self.guessed_letters)
        # Add spacing for readability
        spaced_display = "  ".join(display.split())
        self.word_label.config(text=spaced_display)
        self.info_label.config(
            text=f"Attempts remaining: {MAX_ATTEMPTS - self.incorrect_attempts}"
        )

    # ----------------------------
    # Guess Handling
    # ----------------------------
    def make_guess(self):
        guess = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            return

        if guess in self.guessed_letters:
            return

        self.guessed_letters.append(guess)

        if guess not in self.secret_word:
            self.incorrect_attempts += 1

        self.update_display()

        if has_won(self.secret_word, self.guessed_letters):
            self.info_label.config(text="🎉 You Won!")
            self.guess_button.config(state="disabled")
            self.entry.config(state="disabled")
        elif has_lost(self.incorrect_attempts):
            self.word_label.config(text="  ".join(self.secret_word))
            self.info_label.config(text="💀 Game Over!")
            self.guess_button.config(state="disabled")
            self.entry.config(state="disabled")

    # ----------------------------
    # Reset Game
    # ----------------------------
    def reset_game(self):
        self.secret_word = get_random_word()
        self.guessed_letters = []
        self.incorrect_attempts = 0
        self.guess_button.config(state="normal")
        self.entry.config(state="normal")
        self.update_display()