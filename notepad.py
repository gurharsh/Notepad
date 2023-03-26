# NotePad
from tkinter import *
from tkinter import messagebox
import os
from tkinter.filedialog import askopenfilename,asksaveasfilename
notepad=Tk()
notepad.title("Notepad")
notepad.wm_iconbitmap("notepadproject.ico")
scrb=Scrollbar(notepad)
scrb.pack(side="right",fill=Y)
notepad.geometry("500x400")
txt=Text(notepad,height="600",width="500",undo=True,yscrollcommand=scrb.set)
txt.pack()
scrb.config(command=txt.yview)
file=None
def helppad():
    msgshow=messagebox.showinfo("Help","If You Need Any Help Contact to Gurharsh")
def newFile():
    global file
    txt.delete(1.0,END)
    notepad.title("Untitled.txt")
def openx():
    # file=None
  global file
  file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
                                                          ("Text Document",".txt")])
  txt.delete(1.0,END)
  notepad.title(os.path.basename(file)+"-Notepad")
  f=open(file,"r")
  txt.insert(1.0,f.read())
  f.close()
def save():
    global file
    file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document",".txt")])
    f=open(file,"w")
    f.write(txt.get(1.0,END))
    f.close()
    notepad.title(os.path.basename(file)+"-Notepad")

def copy():
    txt.event_generate(("<<Copy>>"))
def cut():
    txt.event_generate(("<<Cut>>"))
def paste():
    txt.event_generate(("<<Paste>>"))
def undo():
    txt.event_generate(("<<Undo>>"))
def redo():
    txt.event_generate(("<<Redo>>"))
def deletex():
    txt.event_generate(("<<Clear>>"))
def replacex():
    txt.event_generate(("<<Replace>>"))
def selectx():
    txt.event_generate(("<Control-a>"))

def exit():
    check=messagebox.askquestion("Exit","Do you want to exit notepad ?")
    # print(check)
    if(check=='yes'):
        notepad.destroy()

mainmenu=Menu(notepad)
mainsub=Menu(mainmenu,tearoff=0)
mainedit=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="File",menu=mainsub)
mainsub.add_command(label="New",command=newFile)
mainsub.add_command(label="Open",command=openx)
mainsub.add_command(label="Save",command=save)
mainsub.add_command(label="Exit",command=exit)
mainedit.add_command(label="Select All",command=selectx)
mainedit.add_command(label="Undo",command=undo)
mainedit.add_command(label="Redo",command=redo)
mainedit.add_command(label="Delete",command=deletex)
mainedit.add_command(label="Cut",command=cut)
mainedit.add_command(label="Copy",command=copy)
mainedit.add_command(label="Paste",command=paste)
mainmenu.add_cascade(label="Edit",menu=mainedit)
mainmenu.add_command(label="Help",command=helppad)
notepad.config(menu=mainmenu)
notepad.mainloop()