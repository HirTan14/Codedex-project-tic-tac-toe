from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic-Tac-Toe")
#window.geometry("268x300")

# X starts
X_Plays = True
count = 0
color="SystemButtonFace"
fgcolor="black"
bg_win_color="#FF7F7F"
fg_win_color="black"


def disable_buttons():
    square1.config(state=DISABLED)
    square2.config(state=DISABLED)
    square3.config(state=DISABLED)
    square4.config(state=DISABLED)
    square5.config(state=DISABLED)
    square6.config(state=DISABLED)
    square7.config(state=DISABLED)
    square8.config(state=DISABLED)
    square9.config(state=DISABLED)

def tie():
    global bg_win_color, fg_win_color
    square1.config( bg=bg_win_color, fg=fg_win_color)
    square2.config( bg=bg_win_color, fg=fg_win_color)
    square3.config( bg=bg_win_color, fg=fg_win_color)
    square4.config( bg=bg_win_color, fg=fg_win_color)
    square5.config( bg=bg_win_color, fg=fg_win_color)
    square6.config( bg=bg_win_color, fg=fg_win_color)
    square7.config( bg=bg_win_color, fg=fg_win_color)
    square8.config( bg=bg_win_color, fg=fg_win_color)
    square9.config( bg=bg_win_color, fg=fg_win_color)

#click
def click(button):
    global X_Plays
    global count

    if (button["text"]==" " and X_Plays==True):
        button["text"]="X"
        X_Plays=False
        count+=1
        threeInRow()

    elif (button["text"]==" " and X_Plays==False):
        button["text"]="O"
        X_Plays=True
        count+=1
        threeInRow()

    else:
        messagebox.showerror("game", "box already full\n pick new box")

def threeInRow():
    global winner, count, fg_win_color, bg_win_color
    winner=False
    winnerLetter=""

    if(square1["text"]!=" " and square1["text"]==square2["text"] and square2["text"]==square3["text"]):
        square1.config( bg=bg_win_color, fg=fg_win_color)
        square2.config( bg=bg_win_color, fg=fg_win_color)
        square3.config( bg=bg_win_color, fg=fg_win_color)
        winner= True
        count=0
        winnerLetter=square1["text"] + " wins"
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", winnerLetter)
        

    elif(square4["text"]!=" " and square4["text"]==square5["text"] and square5["text"]==square6["text"]):
        square4.config( bg=bg_win_color, fg=fg_win_color)
        square5.config( bg=bg_win_color, fg=fg_win_color)
        square6.config( bg=bg_win_color, fg=fg_win_color)
        winner= True
        winnerLetter=square4["text"] + " wins"
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", winnerLetter)

    elif(square7["text"]!= " " and square7["text"]==square8["text"] and square8["text"]==square9["text"]):
        square7.config( bg=bg_win_color, fg=fg_win_color)
        square8.config( bg=bg_win_color, fg=fg_win_color)
        square9.config( bg=bg_win_color, fg=fg_win_color)
        winner= True
        winnerLetter=square7["text"] + " wins"
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", winnerLetter)
    
    elif(square1["text"]!= " " and square1["text"]==square4["text"] and square4["text"]==square7["text"]):
        square1.config( bg=bg_win_color, fg=fg_win_color)
        square4.config( bg=bg_win_color, fg=fg_win_color)
        square7.config( bg=bg_win_color, fg=fg_win_color)
        winner= True
        winnerLetter=square1["text"] + " wins"
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", winnerLetter)
    
    elif(square2["text"]!= " " and square2["text"]==square5["text"] and square5["text"]==square8["text"]):
        square2.config( bg=bg_win_color, fg=fg_win_color)
        square5.config( bg=bg_win_color, fg=fg_win_color)
        square8.config( bg=bg_win_color, fg=fg_win_color)
        winner= True
        winnerLetter=square2["text"] + " wins"
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", winnerLetter)

    elif(square3["text"]!= " " and square3["text"]==square6["text"] and square6["text"]==square9["text"]):
        square3.config( bg=bg_win_color, fg=fg_win_color)
        square6.config( bg=bg_win_color, fg=fg_win_color)
        square9.config( bg=bg_win_color, fg=fg_win_color)
        winner= True
        winnerLetter=square3["text"] + " wins"
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", winnerLetter)

    elif(square1["text"]!= " " and square1["text"]==square5["text"] and square5["text"]==square9["text"]):
        square1.config( bg=bg_win_color, fg=fg_win_color)
        square5.config( bg=bg_win_color, fg=fg_win_color)
        square9.config( bg=bg_win_color, fg=fg_win_color)
        winner= True
        winnerLetter=square1["text"] + " wins"
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", winnerLetter)

    elif(square3["text"]!= " " and square3["text"]==square5["text"] and square5["text"]==square7["text"]):
        square3.config( bg=bg_win_color, fg=fg_win_color)
        square5.config( bg=bg_win_color, fg=fg_win_color)
        square7.config( bg=bg_win_color, fg=fg_win_color)
        winner= True
        winnerLetter=square3["text"] + " wins"
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", winnerLetter)
    
    elif(count==9):
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", "its a tie")


#replay
def replay():
    global color
    square1.config(text=" ", state=NORMAL, bg=color)
    square2.config(text=" ", state=NORMAL, bg=color)
    square3.config(text=" ", state=NORMAL, bg=color)
    square4.config(text=" ", state=NORMAL, bg=color)
    square5.config(text=" ", state=NORMAL, bg=color)
    square6.config(text=" ", state=NORMAL, bg=color)
    square7.config(text=" ", state=NORMAL, bg=color)
    square8.config(text=" ", state=NORMAL, bg=color)
    square9.config(text=" ", state=NORMAL, bg=color)
    global count
    count = 0

def blue():
    global color, fgcolor, bg_win_color
    color="#03dbfc"
    fgcolor="white"
    global bg_win_color
    bg_win_color="white"
    replay()

def red():
    global color, fgcolor
    color="#FF7F7F"
    fgcolor="black"
    global bg_win_color
    bg_win_color="white"
    replay()


def yellow():
    global color, fgcolor
    color="#e3c23d"
    fgcolor="black"
    global bg_win_color
    bg_win_color="white"
    replay()


def green():
    global color
    color="#4cba5d"
    global fgcolor
    fgcolor="white"
    global bg_win_color
    bg_win_color="white"
    replay()


def default_color():
    global color, fgcolor
    color="SystemButtonFace"
    fgcolor="black"
    global bg_win_color
    bg_win_color="#FF7F7F"
    replay()


option_menu=Menu(window)
window.config(menu=option_menu)
options=Menu(option_menu, tearoff=False )
option_menu.add_cascade(label="color", menu=options)
options.add_command(label="blue", command=blue)
options.add_command(label="red", command=red)
options.add_command(label="yellow", command=yellow)
options.add_command(label="green", command=green)
options.add_command(label="default", command=default_color)




#buttons
square1=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square1))
square2=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square2))
square3=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square3))

square4=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square4))
square5=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square5))
square6=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square6))

square7=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square7))
square8=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square8))
square9=Button(window, text=" ", font=("Helvetica", 20), height=2, width=5, bg=color, fg=fgcolor, command=lambda: click(square9))

square10=Button(window, text="Replay", font=("Helvetica", 10), height=2, width=5, bg="SystemButtonFace", command=lambda:replay(), borderwidth=0)

#grid
square1.grid(row=0, column=0)
square2.grid(row=0, column=1)
square3.grid(row=0, column=2)

square4.grid(row=1, column=0)
square5.grid(row=1, column=1)
square6.grid(row=1, column=2)

square7.grid(row=2, column=0)
square8.grid(row=2, column=1)
square9.grid(row=2, column=2)

square10.grid(row=3, column=0, columnspan = 3, padx = 1, pady = 1)
window.mainloop()

