from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import socket
import os

filename = None
host = socket.gethostname()
port = 8080

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

      def open_sender(self):
            SenderWindow(self.root)

      def open_receiver(self):
            ReceiverWindow(self.root)


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
                  print("Waiting please")
                  conn,addr = s.accept()
                  file=open(filename,"rb")
                  file_data=file.read(1024)
                  conn.send(file_data)
                  print("Veri transfer edildi")
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
                  s.connect((ID,port))
                  file=open(filename1,'wb')
                  file_data = s.recv(1024)
                  file.write(file_data)
                  file.close()
                  print("Dosya alındı")


            self.sender_id_label = Label(
            self.main, text="Gönderen ID:", font=("arial", 12), bg="#f4fdfe"
            )
            self.sender_id_label.pack(pady=10)
            self.sender_id_entry = Entry(self.main, width=25, font=("arial", 12))
            self.sender_id_entry.pack()

            self.incoming_file_label = Label(
            self.main, text="Alınacak Dosya Adı:", font=("arial", 12), bg="#f4fdfe"
            )
            self.incoming_file_label.pack(pady=10)
            self.incoming_file_entry = Entry(self.main, width=25, font=("arial", 12))
            self.incoming_file_entry.pack()



            self.receive_button = Button(
            self.main,
            text="Al",
            width=8,
            height=1,
            font="arial 14 bold",
            bg="#f4f",
            fg="#000",
            command=receiver_file,
            )
            self.receive_button.pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.root.mainloop()

