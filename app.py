from tkinter import Tk, Label, Button, PhotoImage
import os
from sender import SenderWindow
from receiver import ReceiverWindow




class App:
      def __init__(self): # Giriş Ekranı UI 
            self.root = Tk()
            self.root.title("Paylaş")
            self.root.geometry("540x720+600+240")
            self.root.configure()
            self.root.resizable(False,False)
            image_icon = PhotoImage(file="assets/share.png")
            self.root.iconphoto(False,image_icon)

            self.title_label = Label(self.root,text="File Transfer",
                                     font=("Acumin Variable Concept",20,'bold')).place(x=180,y=30)
            
            #Send and Receiver Button

            #send_image=PhotoImage(file="assets/sender.png")
            self.send_button=Button(self.root,text="Send",bg="#7d2fbd",bd=0,
                                    width=12,height=2,font="arial 14 bold",
                                    command=self.open_sender)
            self.send_button.place(x=50,y=120)
       
            #receive_image=PhotoImage(file="assets/receive.png")
            self.receive_button=Button(self.root,text="Receive",bg="#7d2fbd",bd=0,
                                       width=12,height=2,font="arial 14 bold",
                                       command=self.open_receiver)
            self.receive_button.place(x=350,y=120)
         
            #buton başlıkları
            #Label(self.root,text="Send",font=("Acumin Variable Concept",17,"bold"),bg="#7d2fbd").place(x=70,y=200)
            #Label(self.root,text="Receiver",font=("Acumin Variable Concept",17,"bold"),bg="#7d2fbd").place(x=350,y=200)

            background=PhotoImage(file="assets/background.png")
            Label(self.root,image=background).place(x=20,y=323)
            #incele !!

      def open_sender(self):
            SenderWindow(self.root)

      def open_receiver(self):
            ReceiverWindow(self.root)
