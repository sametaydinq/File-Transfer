from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import socket
import os

filename = None



class App:
      def __init__(self):
            self.root = Tk()
            self.root.title("Paylaş")
            self.root.geometry("540x720+600+240")
            self.root.configure(bg="#7d2fbd")
            self.root.resizable(False,False)

            image_icon = PhotoImage(file="share.png")
            self.root.iconphoto(False,image_icon)

            self.title_label = Label(self.root,text="File Transfer",
                                     font=("Acumin Variable Concept",20,'bold'),
                                    bg="#7d2fbd").place(x=25,y=30)

            #Frame(self.root,width=420,height=2,bg="#ffffff").place(x=25,y=32)

            send_image=PhotoImage(file="sender.png")
            self.send_button=Button(self.root,image=send_image,bg="#7d2fbd",bd=0,command=self.open_sender)
            self.send_button.place(x=60,y=100)

            receive_image=PhotoImage(file="receive.png")
            self.receive_button=Button(self.root,image=receive_image,bg="#7d2fbd",bd=0,command=self.open_receiver)
            self.receive_button.place(x=360,y=100)


            #label 
            Label(self.root,text="Send",font=("Acumin Variable Concept",17,"bold"),bg="#7d2fbd").place(x=70,y=200)
            Label(self.root,text="Receiver",font=("Acumin Variable Concept",17,"bold"),bg="#7d2fbd").place(x=350,y=200)


            background=PhotoImage(file="assets/background.png")
            Label(self.root,image=background).place(x=20,y=323)

      def open_sender(self):
            SenderWindow(self.root)

      def open_receiver(self):
            ReceiverWindow(self.root)


class SenderWindow:
      pass


class ReceiverWindow:
      pass


"""
def select_file():

      filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",
                                          filetypes=(("file_type","*.txt"),("all files","*.*")))
      
def sender():
      s=socket.socket()
      host=socket.gethostname()
      port=8080
      s.bind((host,port))
      s.listen(1)
      print(host)
      print("Waiting please")
      conn,addr = s.accept()
      file=open(filename,"rb")
      file_data=file.read(1024)
      conn.send(file_data)
      print("Veri transfer edildi")


def Send():
      window=Toplevel(root)
      window.title("Send")
      window.geometry("450x540+500+200")
      window.configure(bg="#f4fdfe")
      window.resizable(False,False)

      #icon
      image_icon1=PhotoImage(file="sender.png")
      window.iconphoto(False,image_icon1)

      Sbackground =PhotoImage(file="sender.png")
      Label(window,image=Sbackground).place(x=2,y=7)
      
      Mbackground = PhotoImage(file="id.png")
      Label(window,image=Mbackground).place(x=-10,y=100)
      
      host = socket.gethostname()
      Label(window,text=f'ID: {host}',bg="white",fg="black").place(x=200,y=165)

      Button(window,text="Select File",width=10,height=1,font="arial 14 bold",bg="#fff",fg="#000",command=select_file).place(x=150,y=30)
      Button(window,text="SEND",width=8,height=1,font="arial 14 bold",bg="#000",fg="#fff",command=sender).place(x=300,y=30)

      window.mainloop()


def Receive():
      main=Toplevel(root)
      main.title("Receiver")
      main.geometry("450x540+500+200")
      main.configure(bg="#f4fdfe")
      main.resizable(False,False)


      def receiver():
            ID=SenderID.get()
            filename1 = incoming_file.get()
            s=socket.socket()
            port=8080
            s.connect((ID,port))
            file=open(filename1,'wb')
            file_data = s.recv(1024)
            file.write(file_data)
            file.close()
            print("Dosya alındı")
            




      #icon
      image_icon2=PhotoImage(file="receive.png")
      main.iconphoto(False,image_icon2)
      
      Hbackground =PhotoImage(file="receiver.png")
      Label(main,image=Hbackground).place(x=7,y=0)

      #logo=PhotoImage(file="profile.png")
      #Label(main,image=logo,bg="#f4fdfe").place(x=100,y=280)

      Label(main,text="Receive",font=("arial",20),bg="#f4fdfe").place(x=100,y=280)

      Label(main,text="Gönderen adi girişi",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=340)
      SenderID = Entry(main,width=25,fg="black",border=2,bg="white",font=("arial",15))
      SenderID.place(x=20,y=370)
      SenderID.focus()

      Label(main,text="Gelen dosya adi",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=420)
      incoming_file = Entry(main,width=25,fg="black",border=2,bg="white",font=("arial",15))
      incoming_file.place(x=20,y=450)
      
      imageicon = PhotoImage(file="share.png")
      Butonkutu = Button(main,text="Receive",image=image_icon,compound=LEFT,width=130,bg="blue",font="arial 14 bold",command=receiver)
      Butonkutu.place(x=20,y=490)


      main.mainloop()


##icon
"""

if __name__ == "__main__":
    app = App()
    app.root.mainloop()

