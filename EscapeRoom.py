import tkinter as tk
import random
import time

class EscapeRoomGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Escape Room")
        self.room_number = 1
        self.time_remaining = 300  # 5 minutes for the entire game
        self.score = 0
        self.inventory = []
        self.start_time = time.time()

        # Setup the first room
        self.setup_room()

        # Start the timer
        self.start_timer()

    def setup_room(self):
        """Set up the current room based on the room number."""
        self.clear_stage()
        if self.room_number == 1:
            self.room_1()
        elif self.room_number == 2:
            self.room_2()
        elif self.room_number == 3:
            self.room_3()
        elif self.room_number == 4:
            self.room_4()
        elif self.room_number == 5:
            self.room_5()
        else:
            self.end_game()

    def room_1(self):
        """First Room - The Locked Chest"""
        self.display_message("You find yourself in a small, dimly lit room. There's a locked chest in the corner.")
        self.display_message("There is a note on the chest that says: 'The code is the number of letters in the word 'escape'.'")

        # A hidden clue: The code is the number of letters in the word "escape" (6)
        self.display_message("Enter the code to unlock the chest:")

        self.code_entry = tk.Entry(self.root, font=("Arial", 14))
        self.code_entry.pack(pady=10)

        self.check_button = tk.Button(self.root, text="Check Code", command=self.check_code_room_1)
        self.check_button.pack(pady=10)

    def check_code_room_1(self):
        """Check if the user entered the correct code for room 1."""
        user_code = self.code_entry.get().strip()
        if user_code == "6":
            self.inventory.append("Key from chest")  # The key to open the next room
            self.display_message("The chest opens and you find a key!")
            self.score += 10
            self.room_number = 2
            self.setup_room()
        else:
            self.display_message("Incorrect code. Try again!")

    def room_2(self):
        """Second Room - The Locked Door"""
        self.display_message("You move to the next room. There's a locked door with a keypad.")
        self.display_message("You have a key from the chest. Try to use it on the door.")

        if "Key from chest" in self.inventory:
            self.display_message("Use the key to unlock the door!")
            self.room_number = 3
            self.setup_room()
        else:
            self.display_message("You need the key to open the door. Look around for clues.")

    def room_3(self):
        """Third Room - The Final Puzzle"""
        self.display_message("You're in the final room. There's a large puzzle on the wall.")
        self.display_message("The puzzle has missing pieces. Each piece corresponds to a number.")

        # Puzzle: Add 1 + 3 + 5
        self.display_message("Solve this puzzle to unlock the final door: 1 + 3 + 5 = ?")

        self.puzzle_entry = tk.Entry(self.root, font=("Arial", 14))
        self.puzzle_entry.pack(pady=10)

        self.check_button = tk.Button(self.root, text="Submit Answer", command=self.check_puzzle_answer)
        self.check_button.pack(pady=10)

    def check_puzzle_answer(self):
        """Check if the answer to the puzzle in room 3 is correct."""
        user_answer = self.puzzle_entry.get().strip()
        if user_answer == "9":
            self.display_message("Correct! You've solved the puzzle and unlocked the door!")
            self.score += 20
            self.room_number = 4
            self.setup_room()
        else:
            self.display_message("Incorrect answer. Try again!")

    def room_4(self):
        """Fourth Room - The Color Code"""
        self.display_message("You've entered a new room. There are colored buttons on the wall.")
        self.display_message("The buttons have numbers: Red (1), Blue (2), Green (3).")
        self.display_message("Press the buttons in the correct sequence to open the door.")
        self.display_message("The sequence is: Blue, Green, Red")

        self.color_button_blue = tk.Button(self.root, text="Blue", command=lambda: self.press_button("Blue"))
        self.color_button_blue.pack(pady=5)
        self.color_button_green = tk.Button(self.root, text="Green", command=lambda: self.press_button("Green"))
        self.color_button_green.pack(pady=5)
        self.color_button_red = tk.Button(self.root, text="Red", command=lambda: self.press_button("Red"))
        self.color_button_red.pack(pady=5)

        self.sequence = ["Blue", "Green", "Red"]
        self.user_sequence = []

    def press_button(self, color):
        """Record the button pressed and check if the sequence is correct."""
        self.user_sequence.append(color)
        if self.user_sequence == self.sequence:
            self.display_message("Correct sequence! The door opens.")
            self.score += 20
            self.room_number = 5
            self.setup_room()
        elif len(self.user_sequence) >= len(self.sequence):
            self.display_message("Incorrect sequence. Start again!")
            self.user_sequence = []

    def room_5(self):
        """Fifth Room - The Riddle"""
        self.display_message("You’ve reached the final room. There’s a riddle on the wall.")
        self.display_message("Solve the riddle to escape.")
        self.display_message("Riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'")

        self.riddle_entry = tk.Entry(self.root, font=("Arial", 14))
        self.riddle_entry.pack(pady=10)

        self.check_button = tk.Button(self.root, text="Submit Answer", command=self.check_riddle_answer)
        self.check_button.pack(pady=10)

    def check_riddle_answer(self):
        """Check if the riddle answer is correct."""
        user_answer = self.riddle_entry.get().strip().lower()
        if user_answer == "echo":
            self.display_message("Correct! You've solved the riddle and escaped the room!")
            self.score += 30
            self.end_game()
        else:
            self.display_message("Incorrect answer. Try again!")

    def start_timer(self):
        """Start the countdown timer."""
        self.timer_label = tk.Label(self.root, text=f"Time remaining: {self.format_time(self.time_remaining)}", font=("Arial", 14))
        self.timer_label.pack(pady=20)
        self.update_timer()

    def update_timer(self):
        """Update the timer every second."""
        if hasattr(self, 'timer_label') and self.timer_label.winfo_exists():
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time remaining: {self.format_time(self.time_remaining)}")

            if self.time_remaining > 0:
                self.root.after(1000, self.update_timer)
            else:
                self.end_game()

    def format_time(self, seconds):
        """Format time from seconds to mm:ss."""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def display_message(self, message):
        """Display a message to the user."""
        self.message_label = tk.Label(self.root, text=message, font=("Arial", 12), fg="red")
        self.message_label.pack(pady=10)

    def clear_stage(self):
        """Clear the current stage to prepare for the next puzzle."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def end_game(self):
        """End the game and show final score."""
        self.clear_stage()
        self.final_score = self.score + int(self.time_remaining / 10)  # Points for time remaining
        self.message_label = tk.Label(self.root, text=f"Game Over! Your final score: {self.final_score}", font=("Arial", 16))
        self.message_label.pack(pady=20)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)

    def restart_game(self):
        """Restart the game."""
        self.room_number = 1
        self.score = 0
        self.time_remaining = 300
        self.inventory = []
        self.start_time = time.time()
        self.clear_stage()
        self.setup_room()
        self.start_timer()


# Create the main window
root = tk.Tk()
game = EscapeRoomGame(root)
root.mainloop()
