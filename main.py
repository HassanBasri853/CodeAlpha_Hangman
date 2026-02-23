import tkinter as tk
from gui import HangmanGUI

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()