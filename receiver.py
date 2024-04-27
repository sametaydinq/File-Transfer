from tkinter import Button, PhotoImage
from tkinter import Toplevel, Button
from tkinter import filedialog
import os
import socket
from tkinter import *
from tkinter import filedialog
import main

class ReceiverWindow:
      def __init__(self,window):
            self.main=Toplevel(window)
            self.main.title("Receiver")
            self.main.geometry("450x540+500+200")
            self.main.configure(bg="#f4fdfe")
            self.main.resizable(False,False)

            def receiver_file():
                  ID=self.sender_id_entry.get()
                  filename1 = self.incoming_file_entry.get()
                  s=socket.socket()
                  s.connect((ID,main.port))
                  file=open(filename1,'wb')
                  file_data = s.recv(1024)
                  file.write(file_data)
                  file.close()
                  print("Dosya alındı")


            self.sender_id_label = Label(
            self.main, text="Sender ID:", font=("arial", 12), bg="#f4fdfe"
            )
            self.sender_id_label.pack(pady=10)
            self.sender_id_entry = Entry(self.main, width=25, font=("arial", 12))
            self.sender_id_entry.pack()

            self.incoming_file_label = Label(
            self.main, text="Receive File Name:", font=("arial", 12), bg="#f4fdfe"
            )
            self.incoming_file_label.pack(pady=10)
            self.incoming_file_entry = Entry(self.main, width=25, font=("arial", 12))
            self.incoming_file_entry.pack()



            self.receive_button = Button(
            self.main,
            text="Receive",
            width=8,
            height=1,
            font="arial 14 bold",
            bg="#f4f",
            fg="#000",
            command=receiver_file,
            )
            self.receive_button.pack(pady=20)
