from tkinter import Button, PhotoImage
from tkinter import Toplevel, Button
from tkinter import filedialog
import os
import socket
import main
import app
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class SenderWindow:
    
    def __init__(self, window):
        self.main = tk.Toplevel(window)
        self.main.title("Send")
        self.main.geometry("450x200+500+200")
        self.main.configure(bg="#f4fdfe")
        self.main.resizable(False, False)

        self.send_button = tk.Button(
            self.main,
            text="Send",
            width=8,
            height=1,
            font="arial 14 bold",
            bg="#f4f",
            fg="#000",
            command=self.on_send_click,
        )
        self.send_button.pack(pady=20)

    def on_send_click(self):
        
        file_selector = FileSelectionWindow(self.main)
        self.main.wait_window(file_selector.main)  

        filename = file_selector.get_selected_filename()
        s=socket.socket()
        host=socket.gethostname()
        if filename:
            self.send_file(filename)
        else:
            messagebox.showerror("Error", "Please select a file to send.")

    def send_file(self, filename):
        # burayı daha düzgün bir hale getir
        # send den sonra aynı main pencereden receive yapılamıyor düzenle
            s=socket.socket()
            host=socket.gethostname()
            port=8080
            s.bind((host,port))
            s.listen(1)
            print(host)
            print("Lütfen bekleyiniz.")
            conn,addr = s.accept()
            file=open(filename,"rb")
            file_data=file.read(1024)
            conn.send(file_data)
            print("Veri transfer edildi.")
            conn.close()
            s.close()        
            print(f"Sending file: {filename}") 



class FileSelectionWindow:

    def __init__(self, window):
        self.main = tk.Toplevel(window)
        self.main.title("Select File")
        self.main.geometry("400x100+500+200")
        self.main.configure(bg="#f4fdfe")
        self.main.resizable(False, False)

        self.filename = None  

        self.select_file_button = tk.Button(
            self.main,
            text="Select File",
            width=10,
            height=1,
            font="arial 14 bold",
            bg="#f4f",
            fg="#000",
            command=self.on_select_file_click,
        )
        self.select_file_button.pack(pady=20)

    def on_select_file_click(self):
        self.filename = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select File",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
        )
        self.main.destroy() 

    def get_selected_filename(self):
        return self.filename
