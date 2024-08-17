import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        self.root.configure(bg="#f4f4f9")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be or not to be, that is the question.",
            "All that glitters is not gold.",
            "The only thing we have to fear is fear itself."
        ]

        self.start_time = 0
        self.sentence = ""
        self.wpm = 0
        self.accuracy = 0

        # Display sentence
        self.sentence_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f4f4f9", fg="#333333", wraplength=500)
        self.sentence_label.pack(pady=20)

        # Typing input
        self.text_entry = tk.Entry(root, font=("Helvetica", 14), width=50, bd=2, relief="groove", bg="#ffffff", fg="#000000")
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<Return>", self.calculate_speed)

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, relief="raised")
        self.start_button.pack(pady=20)

        # Results label
        self.results_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f4f4f9", fg="#333333")
        self.results_label.pack(pady=20)

    def start_test(self):
        self.sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.sentence)
        self.text_entry.delete(0, tk.END)
        self.text_entry.focus()
        self.start_time = time.time()

    def calculate_speed(self, event):
        end_time = time.time()
        time_taken = end_time - self.start_time
        user_input = self.text_entry.get()
        words_count = len(user_input.split())
        self.wpm = round((words_count / time_taken) * 60)

        # Calculate accuracy
        correct_chars = sum(1 for a, b in zip(user_input, self.sentence) if a == b)
        total_chars = len(self.sentence)
        self.accuracy = round((correct_chars / total_chars) * 100)

        self.results_label.config(text=f"Speed: {self.wpm} WPM\nAccuracy: {self.accuracy}%", bg="#f4f4f9", fg="#333333")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
