from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win
from room_pg import RoomBooking
from details_py import RoomDetails

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1366x768+0+0")


        img1=Image.open("imageh4.jpg")
        img1=img1.resize((1366,160),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img1)

        l1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        l1.place(x=0,y=0,width=1366,height=160)


        imga=Image.open("imageh5.jpg")
        imga=imga.resize((230,160),Image.LANCZOS)
        self.imgb=ImageTk.PhotoImage(imga)

        l1=Label(self.root,image=self.imgb,bd=4,relief=RIDGE)
        l1.place(x=0,y=0,width=230,height=160)


        l2=Label(self.root,text="Hotel Management System",font=("times new roman",35,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        l2.place(x=0,y=160,width=1366,height=60)

        f1=Frame(self.root,bd=3,relief=RIDGE)
        f1.place(x=0,y=220,width=1366,height=548)

        l3=Label(f1,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        l3.place(x=0,y=0,width=230)

        buttonf1=Frame(f1,bd=3,relief=RIDGE)
        buttonf1.place(x=0,y=40,width=225,height=150)

        b1=Button(buttonf1,text="CUSTOMER",width=20,font=("times new roman",14,"bold"),
                                            bg="black",fg="gold",bd=0,cursor="hand2",command=self.cust_details)
        b1.grid(row=0,column=0,pady=1)

        b2=Button(buttonf1,text="ROOM",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2",command=self.roombooking)
        b2.grid(row=1,column=0,pady=1)

        b3=Button(buttonf1,text="DETAILS",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2",command=self.roomdetails)
        b3.grid(row=2,column=0,pady=1)

        b5=Button(buttonf1,text="LOGOUT",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2",command=self.logout)
        b5.grid(row=4,column=0,pady=1)

        img3=Image.open("imageh2.jpg")
        img3=img3.resize((1136,470),Image.LANCZOS)
        self.img4=ImageTk.PhotoImage(img3)

        l1=Label(f1,image=self.img4,bd=4,relief=RIDGE)
        l1.place(x=230,y=0,width=1136,height=470)

        img5=Image.open("imageh3.png")
        img5=img5.resize((230,280),Image.LANCZOS)
        self.img6=ImageTk.PhotoImage(img5)

        l2=Label(f1,image=self.img6,bd=4,relief=RIDGE)
        l2.place(x=0,y=190,width=230,height=280)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app= RoomBooking(self.new_window)
        
    def roomdetails(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomDetails(self.new_window)

    def logout(self):
       self.root.destroy()

    

    



if __name__== "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

