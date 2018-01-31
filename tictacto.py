from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Tic Tac Toe Game")


click = True
win = False

def check(buttons):
    global click
    global win
    if buttons["text"] == "" and click == True:
        buttons["text"] = "X"
        click = False
        changecolor(buttons)
        subcheck()
        if win == False:
            lose()

    elif buttons["text"] == "" and click == False:
        buttons["text"] = "O"
        click = True
        changecolor(buttons)
        subcheck()
        if win == False:
                lose()

    elif buttons["text"] == "X" or buttons["text"] == "O":
        pass



def subcheck():
    global win
    if (btn1["text"] == "X" and btn2["text"] == "X" and  btn3["text"] == "X" or
        btn4["text"] == "X" and btn5["text"] ==  "X" and btn6["text"] == "X" or
        btn7["text"] == "X" and btn8["text"] ==  "X" and btn9["text"] == "X" or
        btn1["text"] == "X" and btn5["text"] ==  "X" and btn9["text"] == "X" or
        btn8["text"] == "X" and btn5["text"] ==  "X" and btn2["text"] == "X" or
        btn7["text"] == "X" and btn4["text"] ==  "X" and btn1["text"] == "X" or
        btn9["text"] == "X" and btn6["text"] ==  "X" and btn3["text"] == "X" or
        btn7["text"] == "X" and btn5["text"] ==  "X" and btn3["text"] == "X"):
            tkinter.messagebox.showinfo("Winner X","The player with X win the game...")
            win = True
            root.quit();
    elif(btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O" or
        btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O" or
        btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O" or
        btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O" or
        btn8["text"] == "O" and btn5["text"] == "O" and btn2["text"] == "O" or
        btn7["text"] == "O" and btn4["text"] == "O" and btn1["text"] == "O" or
        btn9["text"] == "O" and btn6["text"] == "O" and btn3["text"] == "O" or
        btn7["text"] == "O" and btn5["text"] == "O" and btn3["text"] == "O"):
            tkinter.messagebox.showinfo("Winner O", "The player with O win the game...")
            win = True
            root.quit()

def lose():
    if (    btn1["text"] != "" and btn2["text"] != "" and btn3["text"] != "" and
            btn8["text"] != "" and btn7["text"] != "" and btn4["text"] != "" and
            btn9["text"] != "" and btn6["text"] != "" and btn5["text"] != "" ):
        tkinter.messagebox.showinfo("Withdraw", "No one win the game ")

        root.quit()

def changecolor(button):
    button.configure(bg="powder blue")


buttons = StringVar()


btn1 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn1), bd=10, bg="light green")

btn1.grid(row=0,column=0, sticky = S+N+E+W)

btn2 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn2), bd=10, bg="light green")

btn2.grid(row=0,column=1, sticky = S+N+E+W)

btn3 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn3), bd=10, bg="light green")

btn3.grid(row=0,column=2, sticky = S+N+E+W)

btn4 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn4), bd=10, bg="light green")

btn4.grid(row=1,column=0, sticky = S+N+E+W)

btn5 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn5), bd=10, bg="light green")

btn5.grid(row=1,column=1, sticky = S+N+E+W)

btn6 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn6), bd=10, bg="light green")

btn6.grid(row=1,column=2, sticky = S+N+E+W)

btn7 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn7), bd=10, bg="light green")

btn7.grid(row=2,column=0, sticky = S+N+E+W)

btn8 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn8), bd=10, bg="light green")

btn8.grid(row=2,column=1, sticky = S+N+E+W)

btn9 = Button(root,width = 5, height = 3, font = ("arial",20,"bold"), command = lambda:check(btn9), bd=10, bg="light green")

btn9.grid(row=2,column=2, sticky = S+N+E+W)

root.mainloop()