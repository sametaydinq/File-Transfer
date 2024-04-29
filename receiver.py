from tkinter import Button, PhotoImage
from tkinter import Toplevel, Button
from tkinter import filedialog
import os
import socket
from tkinter import *
from tkinter import filedialog
import main
import app


import tkinter as tk
from tkinter import filedialog
import socket

class SocketFileTransfer:

    def __init__(self, window, port=8080):  ## port olayını çöz globalden al
        self.window = window
        self.port = port

    def transfer_file(self, sender_id, filename, action="receive"):
        s = socket.socket()
        if action == "receive":
            s.connect((sender_id, self.port))
        else:
            # es geç
            pass
        file = open(filename, 'wb' if action == "receive" else 'rb')
        while True:
            data = s.recv(1024)
            if not data:
                break
            file.write(data)
        file.close()
        print(f"File {action}d successfully!")


class ReceiverWindow:
   

    def __init__(self, window):
        self.main = Toplevel(window)
        self.main.title("Receiver")
        self.main.geometry("450x540+500+200")
        self.main.configure(bg="#f4fdfe")
        self.main.resizable(False, False)

        self.file_transfer = SocketFileTransfer(self.main)  

        self.sender_id_label = tk.Label(
            self.main, text="Sender ID:", font=("arial", 12), bg="#f4fdfe"
        )
        self.sender_id_label.pack(pady=10)
        self.sender_id_entry = tk.Entry(self.main, width=25, font=("arial", 12))
        self.sender_id_entry.pack()

        self.incoming_file_label = tk.Label(
            self.main, text="Receive File Name:", font=("arial", 12), bg="#f4fdfe"
        )
        self.incoming_file_label.pack(pady=10)
        self.incoming_file_entry = tk.Entry(self.main, width=25, font=("arial", 12) )
        self.incoming_file_entry.pack()

        self.receive_button = tk.Button(
            self.main,
            text="Receive",
            width=8,
            height=1,
            font="arial 14 bold",
            bg="#f4f",
            fg="#000",
            command=self.on_receive_click,
        )
        self.receive_button.pack(pady=20)

    def on_receive_click(self):
        sender_id = self.sender_id_entry.get()
        filename = self.incoming_file_entry.get()
        if sender_id and filename:
            self.file_transfer.transfer_file(sender_id, filename)
        else:
            print("Please enter sender ID and filename.")


