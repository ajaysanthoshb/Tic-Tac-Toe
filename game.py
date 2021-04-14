from tkinter import *
import random

def next_turn(row,column):
    global player

    #if a player clicked button and that button is empty
    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]: #if players[0] clicked button
            buttons[row][column]['text'] = player
            buttons[row][column].config(fg = "red")

            if check_winner() is False:
                player = players[1]
                label1.config(text = player + " turn")

            elif check_winner() is True:
                label1.config(text = player + " wins")

            elif check_winner() == "Tie":
                label1.config(text = ("TIE!!!!!"))

        else: #if players[1] clicked button
            buttons[row][column]['text'] = player
            buttons[row][column].config(fg="cyan")

            if check_winner() is False:
                player = players[0]
                label1.config(text=player + " turn")

            elif check_winner() is True:
                label1.config(text=player + " wins")

            elif check_winner() == "Tie":
                label1.config(text=("TIE!!!!!"))

def check_winner():

    #check along row wise
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg = "green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # check along column wise
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    #check along left diagonal

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    #check along right diagonal
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    #check empty_spaces there or not
    elif check_empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg = "yellow")
        return "Tie"

    else:
        return False


def check_empty_spaces():
     spaces = 9

     for row in range(3):
         for column in range(3):
             if buttons[row][column]['text'] != "":
                 spaces -= 1

     if spaces == 0:
         return False

     else:
         return True

def new_game():

    global player

    player = random.choice(players)
    label1.config(text = player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "",bg = "#F0F0F0")
    pass

window = Tk()
window.wm_title("Tic-Tac-Toe")
players = ['x','o']
player = random.choice(players) #choose a random character (x or o)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label1 = Label()
label1.config(text = player + " Turn",font = ('consolas',40))
label1.pack(side = "top")

reset_button = Button()
reset_button.config(text = "restart",font = ('consolas',20),command = new_game,fg = "black",bg = "pink")
reset_button.pack(side = "top")

frame = Frame(window) #we are gonna place all these buttons in a frame
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame,text = "",font = ('consolas',40),width = 5, height = 2
                                      ,command = lambda row = row,column = column:next_turn(row,column))
        buttons[row][column].grid(row = row , column = column) #grids works for frames
window.mainloop()
