from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import socket
import os


root = Tk()
root.title("Paylaş")
root.geometry("540x720+600+240")
root.configure(bg="#7d2fbd")
root.resizable(False,False)


def Send():
      window=Toplevel(root)
      window.title("Send")
      window.geometry("450x540+500+200")
      window.configure(bg="#f4fdfe")
      window.resizable(False,False)

      #icon
      image_icon1=PhotoImage(file="sender.png")
      window.iconphoto(False,image_icon1)

      window.mainloop()


def Receive():
      main=Toplevel(root)
      main.title("Receiver")
      main.geometry("450x540+500+200")
      main.configure(bg="#f4fdfe")
      main.resizable(False,False)

      #icon
      image_icon1=PhotoImage(file="sender.png")
      main.iconphoto(False,image_icon1)
      
      main.mainloop()
##icon

image_icon = PhotoImage(file="share.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=("Acumin Variable Concept",20,'bold'),
      bg="#7d2fbd").place(x=25,y=30)

#Frame(root,width=420,height=2,bg="#ffffff").place(x=25,y=32)

send_image=PhotoImage(file="sender.png")
send=Button(root,image=send_image,bg="#7d2fbd",bd=0,command=Send)

send.place(x=60,y=100)

receive_image=PhotoImage(file="receiver.png")
receive=Button(root,image=receive_image,bg="#7d2fbd",bd=0,command=Receive)
receive.place(x=360,y=100)

#label 
Label(root,text="Send",font=("Acumin Variable Concept",17,"bold"),bg="#7d2fbd").place(x=70,y=200)
Label(root,text="Receiver",font=("Acumin Variable Concept",17,"bold"),bg="#7d2fbd").place(x=350,y=200)


background=PhotoImage(file="background.png")
Label(root,image=background).place(x=20,y=323)




root.mainloop()