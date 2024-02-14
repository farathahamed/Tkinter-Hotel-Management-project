from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector 
from tkinter import messagebox

class RoomDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1136x460+230+250")



        la2=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        la2.place(x=0,y=0,width=1136,height=50)

        p1=Image.open("imageh5.jpg")
        p2=p1.resize((100,50),Image.LANCZOS)
        self.p3=ImageTk.PhotoImage(p2)

        la3=Label(self.root,image=self.p3,bd=0,relief=RIDGE)
        la3.place(x=0,y=0,width=100,height=50)

        lable_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room ADD ",padx=2,font=("arial",12,"bold"))
        lable_frame.place(x=5,y=50,width=520,height=300)

        floor=Label(lable_frame,text="Floor",font=("axial",10,"bold"),padx=2,pady=6)
        floor.grid(row=0,column=0,sticky=W)


        self.var_floor=StringVar()
        ref_floor=ttk.Entry(lable_frame,textvariable=self.var_floor,width=20,font=("axial",11,"bold"))
        ref_floor.grid(row=0,column=1,sticky=W)

        roomno=Label(lable_frame,text="Room No",font=("axial",10,"bold"),padx=2,pady=6)
        roomno.grid(row=1,column=0,sticky=W)

        self.var_roomno=StringVar()
        ref_roomno=ttk.Entry(lable_frame,textvariable=self.var_roomno,width=20,font=("axial",11,"bold"))
        ref_roomno.grid(row=1,column=1,sticky=W)

        roomtype=Label(lable_frame,text="Room Type",font=("axial",10,"bold"),padx=2,pady=6)
        roomtype.grid(row=2,column=0,sticky=W)

        self.var_roomtype=StringVar()
        ref_roomtype=ttk.Entry(lable_frame,textvariable=self.var_roomtype,width=20,font=("axial",11,"bold"))
        ref_roomtype.grid(row=2,column=1,sticky=W)

        b1=Frame(lable_frame,bd=2,relief=RIDGE)
        b1.place(x=0,y=200,width=400,height=35)

        add=Button(b1,text="Add",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.include_data)
        add.grid(row=0,column=0,padx=1)

        update=Button(b1,text="Update",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.update)
        update.grid(row=0,column=1,padx=1)

        delete=Button(b1,text="Delete",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.mDelete)
        delete.grid(row=0,column=2,padx=1)

        reset=Button(b1,text="Reset",font=("axial",12,"bold"),bg="black",fg="gold",width=11,command=self.reset_data)
        reset.grid(row=0,column=3,padx=1)


        table_frame=LabelFrame(root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=570,y=50,width=500,height=300)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.room_Table=ttk.Treeview(table_frame,column=("floor","roomno","roomtype"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.room_Table.xview)
        scrolly.config(command=self.room_Table.yview)

        self.room_Table.heading("floor",text="Floor")
        self.room_Table.heading("roomno",text="Room No")
        self.room_Table.heading("roomtype",text="Room Type")


        self.room_Table["show"]="headings"

        self.room_Table.column("floor",width=100)
        self.room_Table.column("roomno",width=100)
        self.room_Table.column("roomtype",width=100)
  
        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def include_data(self):
      if self.var_floor.get()=='' or self.var_roomtype.get()=='':
          messagebox.showerror("error","All fields are required")
      else:
          try:
             conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
             mycursor=conn.cursor()
             mycursor.execute("insert into details values(%s,%s,%s)",
                           (self.var_floor.get(),self.var_roomno.get(),self.var_roomtype.get()))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("success","New Room Added Successfully",parent=self.root)

          except Exception as es:
             messagebox.showwarning("warning",f"something went wrong {str(es)}",parent=self.root)


    def fetch_data(self):
       conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
       mycursor=conn.cursor()
       mycursor.execute("select *  from details")
       rows=mycursor.fetchall()
       if len(rows)!=0:
          self.room_Table.delete(*self.room_Table.get_children())
          for i in rows:
              self.room_Table.insert("",END,values=i)

          conn.commit()
          conn.close()

    def get_cursor(self,event=""):
       cursor_row=self.room_Table.focus()
       content=self.room_Table.item(cursor_row)
       row=content["values"]
    
       self.var_floor.set(row[0]),
       self.var_roomno.set(row[1]),
       self.var_roomtype.set(row[2]),

    def update(self):
       if self.var_floor.get()=='':
           messagebox.showerror("error","please enter mobile number")
       else:    
           conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
           mycursor=conn.cursor()
           mycursor.execute("update details set floor=%s,roomtype=%s where Roomno=%s",
                         (self.var_floor.get(),self.var_roomtype.get(),self.var_roomno.get()))

           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("success"," New Room details has been updated successfully")


    def mDelete(self):
       mDelete=messagebox.askyesno("delete","Do you want to delete this customer")
       if mDelete!=0:
           conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
           mycursor=conn.cursor()
           query="delete from details where Roomno=%s"
           value=(self.var_roomno.get(),)
           mycursor.execute(query,value)
       else:
           if not mDelete:
             return

           conn.commit()
           self.fetch_data()
           conn.close()

    def reset_data(self):
       self.var_floor.set(""),
       self.var_roomno.set(""),
       self.var_roomtype.set(""),
 









if __name__== "__main__":
    root=Tk()
    obj=RoomDetails(root)
    root.mainloop() 
