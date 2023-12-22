import tkinter
import random

# Global Variables to store score


user = 0
machine_score = 0

# Function to play game
def game(player):
 global user,Computer_choice

# List Of Choice for The Computer
 li =["ROCK ", " PAPER ", " SCISSOR "]

 #  declaration
 # [.random na help computer ani choices lase ane try karse k let he wins ]
 Computer_choice = random.choice(li)

 #Winner Determine
 # attyare result name na variable ma wwinner decission store thase ane pache winnerdeciddion namme nu function banavsu  jem playerc ane computer/machine no statements passs karisu
 result = winnerDecission(player,Computer_choice)

 # Label Updating with choice and result
 user.Label["text"]=f" User Choice :  {player}"
 machine_score.Label["text"]=f"Let Machine Decide : {machine_score}"
 result.Label["text"]=f" Result : {result}"


 # Updating Score based on te result
 if result == "You Win":
      user += 1

 elif result == "Computer Wins":
    machine_score += 1


 # Updating score Labels

 user["text"]= f"user : {user}"
 computer["text"]=f" Computer : {machine_score}"
 result["text"] =f"Result : {user}-{machine_score}"


 # Function to determine Winner

def winnerDecission(player,Computer_choice):
    if player == Computer_choice: # Agar player ane computer no score sarkho hase to niche nu return statemnets pass thase
       return "OOPS It's a Tie"

    # pachi user ne jitava mate ni condition check thase jose agar baddhu oppsite hoi computer thi to player jitse
    elif((player == "ROCK" and Computer_choice == "SCISSOR")or
         (player == "PAPER"  and Computer_choice == "ROCK")or
         (player == "SCISSOR" and Computer_choice == "PAPER")):
       return "GREAT! You Win "
    else:
       return "Computer Win"


# CREATING THE SCREEN OF TKINTER WINDOW AND ITS LAYOUT BUTTONS , TEXT , LABELS
screen = tkinter.Tk() # ani madad thi gui banse
screen.title("WELCOME TO THE GAME OF ROCK PAPER AND SCISSOR")    # je screen pop up thasse ne ani top ma title banse aa nam nu
screen.geometry("550x550") # ana thi  poped screen ni hheight width set thse
    #  "GAME TITLE LABEL"
label = tkinter.Label(screen , text ="ROCK PAPER SCISSOR GAME ", font=("Arial",25,"bold"))
label.place(x = 85 , y = 45)

# ROCK BUTOON STYLING

rock_button = tkinter.Button(screen, command=lambda: game("Rock"), text="Rock",bg="black",fg="white",font=("Arial",15,"bold"),height=4, width=5)
rock_button.place(x=150,y=100)

#PAPER BUTTON STYLING

paper_button = tkinter.Button(screen, command=lambda: game("Paper"), text="paper",bg="black",fg="white",font=("Arial",15,"bold"),height=4, width=5)
paper_button.place(x=250,y=100)

# SCISSOR BUTTON STYLING

scissor_button = tkinter.Button(screen, command=lambda: game("Scissor"), text="Scissor",bg="black",fg="white",font=("Arial",15,"bold"),height=4, width=5)
scissor_button.place(x=350,y=100)



# LABELS FOR DISPLAYING CHOICE AND RESULT
user = tkinter.Label(screen, text="Your choice: ", font=("Arial", 14, "bold"))
user.place(x=50, y=200)

computer = tkinter.Label(screen, text="Computer's choice: ", font=("Arial", 14, "bold"))
computer.place(x=50, y=230)

result = tkinter.Label(screen, text="Result: ", font=("Arial", 14, "bold"))
result.place(x=50, y=260)


 #DIPLAYING SCROES
user = tkinter.Label(screen, text=f"User: {user}", font=("Arial", 14, "bold"))
user.place(x=400, y=200)

computer = tkinter.Label(screen, text=f"Computer: {computer}", font=("Arial", 14, "bold"))
computer.place(x=400, y=230)

result = tkinter.Label(screen, text=f"Result: {user} - {computer}", font=("Arial", 14, "bold"))
result.place(x=400, y=260)



screen.mainloop()