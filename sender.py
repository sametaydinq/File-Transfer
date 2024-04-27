from tkinter import Button, PhotoImage
from tkinter import Toplevel, Button
from tkinter import filedialog
import os
import socket
import main



class SenderWindow:
      def __init__(self,window):
            self.main=Toplevel(window)
            self.main.title("Send")
            self.main.geometry("450x540+500+200")
            self.main.configure(bg="#f4fdfe")
            self.main.resizable(False,False)
      
            image_icon = PhotoImage(file="assets/share.png")
            self.main.iconphoto(False,image_icon)
            
            def send_file():
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


            self.select_file_button = Button(
            self.main,
            text="Select File",
            width=10,
            height=1,
            font="arial 14 bold",
            bg="#f4f",
            fg="#000",
            command=self.select_file,
            )
            self.select_file_button.pack(pady=20)

            self.send_button = Button(
            self.main,
            text="Send",
            width=8,
            height=1,
            font="arial 14 bold",
            bg="#f4f",
            fg="#000",
            command=send_file,
            )
            self.send_button.pack(pady=20)      
             
      def select_file(self):
            global filename
            filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                                title="Select Image File",
                                          filetypes=(("file_type","*.txt"),
                                                ("all files","*.*")))
            