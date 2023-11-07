import tkinter as tk
from tkinter import messagebox
import random


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_choice_var.set(computer_choice)

    winner = get_winner(user_choice, computer_choice)
    winner_var.set(winner)

    global user_score
    global computer_score
    if winner == "You win!":
        user_score += 1
    elif winner == "Computer wins!":
        computer_score += 1
    user_score_var.set(f"User: {user_score}")
    computer_score_var.set(f"Computer: {computer_score}")

    if user_score == 5 or computer_score == 5:
        play_again()


def play_again():
    response = messagebox.askyesno("Game Over", "Do you want to play again?")
    if response:
        global user_score
        global computer_score
        user_score = 0
        computer_score = 0
        user_score_var.set("User: 0")
        computer_score_var.set("Computer: 0")
        user_choice_var.set("rock")
        computer_choice_var.set("")
        winner_var.set("")
    else:
        window.destroy()


window = tk.Tk()
window.title("Rock Papers Scissors game")

user_choice_var = tk.StringVar()
user_choice_var.set("rock")

computer_choice_var = tk.StringVar()
computer_choice_var.set("")

winner_var = tk.StringVar()
winner_var.set("")

user_score = 0
computer_score = 0
user_score_var = tk.StringVar()
user_score_var.set("User: 0")
computer_score_var = tk.StringVar()
computer_score_var.set("Computer: 0")

label = tk.Label(window, text="Choose rock, paper, or scissors:")
label.pack()

rock_button = tk.Radiobutton(
    window, text="Rock", variable=user_choice_var, value="rock"
)
rock_button.pack()

paper_button = tk.Radiobutton(
    window, text="Paper", variable=user_choice_var, value="paper"
)
paper_button.pack()

scissors_button = tk.Radiobutton(
    window, text="Scissors", variable=user_choice_var, value="scissors"
)
scissors_button.pack()

play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

winner_label = tk.Label(window, textvariable=winner_var)
winner_label.pack()

computer_label = tk.Label(window, text="Computer's Choice:")
computer_label.pack()

computer_choice_label = tk.Label(window, textvariable=computer_choice_var)
computer_choice_label.pack()

user_score_label = tk.Label(window, textvariable=user_score_var)
user_score_label.pack()

computer_score_label = tk.Label(window, textvariable=computer_score_var)
computer_score_label.pack()

window.mainloop()
