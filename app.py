from tkinter import Tk, Label, Button, PhotoImage
import os
from sender import SenderWindow
from receiver import ReceiverWindow


class ButtonBase:
    def __init__(self, root, text, command):  #tüm buton yazılarına aynı font ve boyut ayarlanır
        self.button = Button(root, text=text, bg="#7d2fbd", bd=0,
                             width=12, height=2, font="arial 14 bold",
                             command=command)  #komutu direkt yönlendirir
        
    def place(self, x, y): #gelen parametreleri yönlendirir
        self.button.place(x=x, y=y)


class SendButton(ButtonBase):
    def __init__(self, root, click_handler):
        super().__init__(root, text="Send", command=click_handler)


class ReceiveButton(ButtonBase):
    def __init__(self, root, click_handler):
        super().__init__(root, text="Receive", command=click_handler)
            #super fonksiyonu detaylı örnek yap

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Paylaş")
        self.root.geometry("540x720+600+240")
        self.root.configure()
        self.root.resizable(False, False)

    

        image_icon = PhotoImage(file="assets/share.png")
        self.root.iconphoto(False, image_icon)
        self.title_label = Label(self.root, text="File Transfer",
                                 font=("Acumin Variable Concept", 20, 'bold')).place(x=180, y=30)


        self.send_button = SendButton(self.root, self.open_sender)
        self.send_button.place(x=50, y=120)

        self.receive_button = ReceiveButton(self.root, self.open_receiver)
        self.receive_button.place(x=350, y=120)

        background = PhotoImage(file="assets/background.png")
        Label(self.root, image=background).place(x=20, y=323)

        self.root.mainloop()

    def open_sender(self):
        SenderWindow(self.root)

    def open_receiver(self):
        ReceiverWindow(self.root)
