import tkinter
import random

# Global Variables to store score
user_score = 0
machine_score = 0

# Function to play game
def game(player):
    global user_score, machine_score

    # List Of Choice for The Computer
    choices = ["ROCK", "PAPER", "SCISSOR"]

    # Randomly choose computer's move
    computer_choice = random.choice(choices)

    # Winner Determination
    result = winner_decision(player, computer_choice)

    # Label Updating with choice and result
    user_label["text"] = f"Your Choice: {player}"
    computer_label["text"] = f"Computer's Choice: {computer_choice}"
    result_label["text"] = f"Result: {result}"

    # Updating Score based on the result
    if result == "You Win":
        user_score += 1
    elif result == "Computer Wins":
        machine_score += 1

    # Updating score Labels
    user_score_label["text"] = f"User: {user_score}"
    machine_score_label["text"] = f"Computer: {machine_score}"
    result_score_label["text"] = f"Result: {user_score} - {machine_score}"

# Function to determine Winner
def winner_decision(player, computer_choice):
    if player == computer_choice:
        return "It's a Tie"
    elif (player == "ROCK" and computer_choice == "SCISSOR") or \
         (player == "PAPER" and computer_choice == "ROCK") or \
         (player == "SCISSOR" and computer_choice == "PAPER"):
        return "You Win"
    else:
        return "Computer Wins"

# Creating the screen of Tkinter window and its layout buttons, text, labels
screen = tkinter.Tk()
screen.title("WELCOME TO THE GAME OF ROCK PAPER AND SCISSOR")
screen.geometry("550x550")

# Game Title Label
label = tkinter.Label(screen, text="ROCK PAPER SCISSOR GAME", font=("Arial", 25, "bold"))
label.place(x=85, y=45)

# Buttons Styling
rock_button = tkinter.Button(screen, command=lambda: game("ROCK"), text="Rock", bg="black", fg="white", font=("Arial", 15, "bold"), height=4, width=5)
rock_button.place(x=150, y=100)

paper_button = tkinter.Button(screen, command=lambda: game("PAPER"), text="Paper", bg="black", fg="white", font=("Arial", 15, "bold"), height=4, width=5)
paper_button.place(x=250, y=100)

scissor_button = tkinter.Button(screen, command=lambda: game("SCISSOR"), text="Scissor", bg="black", fg="white", font=("Arial", 15, "bold"), height=4, width=5)
scissor_button.place(x=350, y=100)

# Labels for displaying choice and result
user_label = tkinter.Label(screen, text="Your Choice: ", font=("Arial", 14, "bold"))
user_label.place(x=50, y=200)

computer_label = tkinter.Label(screen, text="Computer's Choice: ", font=("Arial", 14, "bold"))
computer_label.place(x=50, y=230)

result_label = tkinter.Label(screen, text="Result: ", font=("Arial", 14, "bold"))
result_label.place(x=50, y=260)

# Displaying Scores
user_score_label = tkinter.Label(screen, text=f"User: {user_score}", font=("Arial", 14, "bold"))
user_score_label.place(x=400, y=200)

machine_score_label = tkinter.Label(screen, text=f"Computer: {machine_score}", font=("Arial", 14, "bold"))
machine_score_label.place(x=400, y=230)

result_score_label = tkinter.Label(screen, text=f"Result: {user_score} - {machine_score}", font=("Arial", 14, "bold"))
result_score_label.place(x=400, y=260)

screen.mainloop()
