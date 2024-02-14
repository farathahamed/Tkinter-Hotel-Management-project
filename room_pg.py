from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

    
class RoomBooking:
    def __init__(self,root):
       self.root=root
       root.title("HOTEL MANAGEMENT SYSTEM")
       root.geometry("1136x460+230+250")

       
       self.var_contact=StringVar()
       self.var_checkin=StringVar()
       self.var_checkout=StringVar()
       self.var_roomtype=StringVar()
       self.var_roomavailable=StringVar()
       self.var_meal=StringVar()
       self.var_noofdays=StringVar()
       self.var_paidtax=StringVar()
       self.var_actualtotal=StringVar()
       self.var_total=StringVar()




       la2=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
       la2.place(x=0,y=0,width=1136,height=50)


       p1=Image.open("imageh5.jpg")
       p1=p1.resize((100,50),Image.LANCZOS)
       self.p2=ImageTk.PhotoImage(p1)

       la3=Label(root,image=self.p2,bd=0,relief=RIDGE)
       la3.place(x=0,y=0,width=100,height=50)

       lable_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("arial",12,"bold"))
       lable_frame.place(x=5,y=50,width=430,height=390)

       customer_contact=Label(lable_frame,text="Customer Contact",font=("axial",10,"bold"),padx=2,pady=6)
       customer_contact.grid(row=0,column=0,sticky=W)

       ref_cont=ttk.Entry(lable_frame,textvariable=self.var_contact,width=20,font=("axial",11,"bold"))
       ref_cont.grid(row=0,column=1,sticky=W)

       btnFetchData=Button(lable_frame,text="Fetch Data",font=("axial",10,"bold"),bg="black",fg="gold",width=8,command=self.Fetch_contact)
       btnFetchData.place(x=300,y=1)

       check_in_date=Label(lable_frame,text="Check_in Date",font=("axial",10,"bold"),padx=2,pady=6)
       check_in_date.grid(row=1,column=0,sticky=W)

       txt_check_in_date=ttk.Entry(lable_frame,textvariable=self.var_checkin,width=32,font=("axial",11,"bold"))
       txt_check_in_date.grid(row=1,column=1,sticky=W)

       check_out_date=Label(lable_frame,text="Check_Out Date",font=("axial",10,"bold"),padx=2,pady=6)
       check_out_date.grid(row=2,column=0,sticky=W)

       txt_check_out_date=ttk.Entry(lable_frame,textvariable=self.var_checkout,width=32,font=("axial",11,"bold"))
       txt_check_out_date.grid(row=2,column=1,sticky=W)

       label_RoomType=Label(lable_frame,text="Room Type",font=("axial",10,"bold"),padx=2,pady=6)
       label_RoomType.grid(row=3,column=0,sticky=W)

       conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
       mycursor=conn.cursor()
       mycursor.execute("select roomtype  from details")
       types=mycursor.fetchall()


       combo_RoomType=ttk.Combobox(lable_frame,textvariable=self.var_roomtype,font=("axial",12,"bold"),width=30,state="readonly")
       combo_RoomType["value"]=types
       combo_RoomType.current(0)
       combo_RoomType.grid(row=3,column=1,sticky=W)

       lbRoomAvailable=Label(lable_frame,text="Available Room",font=("axial",10,"bold"),padx=2,pady=6)
       lbRoomAvailable.grid(row=4,column=0,sticky=W)

       #txtRoomAvailable=ttk.Entry(lable_frame,textvariable=var_roomavailable,width=32,font=("axial",11,"bold"))
       #txtRoomAvailable.grid(row=4,column=1,sticky=W)

       conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
       mycursor=conn.cursor()
       mycursor.execute("select roomno  from details")
       rows=mycursor.fetchall()

       combo_Roomno=ttk.Combobox(lable_frame,textvariable=self.var_roomavailable,font=("axial",12,"bold"),width=30,state="readonly")
       combo_Roomno["value"]=rows
       combo_Roomno.current(0)
       combo_Roomno.grid(row=4,column=1,sticky=W)

       lbMeal=Label(lable_frame,text="Meal:",font=("axial",10,"bold"),padx=2,pady=6)
       lbMeal.grid(row=5,column=0,sticky=W)

       txtMeal=ttk.Entry(lable_frame,textvariable=self.var_meal,width=32,font=("axial",11,"bold"))
       txtMeal.grid(row=5,column=1,sticky=W)

       lbNoofDays=Label(lable_frame,text="No of Days:",font=("axial",10,"bold"),padx=2,pady=6)
       lbNoofDays.grid(row=6,column=0,sticky=W)

       txtNoofDays=ttk.Entry(lable_frame,textvariable=self.var_noofdays,width=32,font=("axial",11,"bold"))
       txtNoofDays.grid(row=6,column=1,sticky=W)

       lbNoofDays=Label(lable_frame,text="Paid Tax:",font=("axial",10,"bold"),padx=2,pady=6)
       lbNoofDays.grid(row=7,column=0,sticky=W)

       txtNoofDays=ttk.Entry(lable_frame,textvariable=self.var_paidtax,width=32,font=("axial",11,"bold"))
       txtNoofDays.grid(row=7,column=1,sticky=W)
                 
       lbNoofDays=Label(lable_frame,text="Sub Total:",font=("axial",10,"bold"),padx=2,pady=6)
       lbNoofDays.grid(row=8,column=0,sticky=W)

       txtNoofDays=ttk.Entry(lable_frame,textvariable=self.var_actualtotal,width=32,font=("axial",11,"bold"))
       txtNoofDays.grid(row=8,column=1,sticky=W)

       lbIDNumber=Label(lable_frame,text="Total Cost:",font=("axial",10,"bold"),padx=2,pady=6)
       lbIDNumber.grid(row=9,column=0,sticky=W)

       txtIDNumber=ttk.Entry(lable_frame,textvariable=self.var_total,width=32,font=("axial",11,"bold"))
       txtIDNumber.grid(row=9,column=1,sticky=W)
 
       bill=Button(lable_frame,text="Bill",font=("axial",9,"bold"),bg="black",fg="gold",width=8,command=self.total)
       bill.grid(row=10,column=0,padx=1,sticky=W)

       b1=Frame(lable_frame,bd=2,relief=RIDGE)
       b1.place(x=0,y=330,width=400,height=35)

       add=Button(b1,text="Add",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.include_data)
       add.grid(row=0,column=0,padx=1)

       update=Button(b1,text="Update",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.update)
       update.grid(row=0,column=1,padx=1)

       delete=Button(b1,text="Delete",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.mDelete)
       delete.grid(row=0,column=2,padx=1)

       reset=Button(b1,text="Reset",font=("axial",12,"bold"),bg="black",fg="gold",width=11,command=self.reset_data)
       reset.grid(row=0,column=3,padx=1)

       p1=Image.open("bedroom1.jpg")
       p2=p1.resize((430,300),Image.LANCZOS)
       self.p3=ImageTk.PhotoImage(p2)
       la3=Label(self.root,image=self.p3,bd=4,relief=RIDGE)
       la3.place(x=700,y=50,width=430,height=300)



       table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"))
       table_frame.place(x=435,y=250,width=700,height=190)

       label_search=Label(table_frame,text="Search by",font=("axial",12,"bold"),bg="red",fg="white")
       label_search.grid(row=0,column=0,sticky=W,padx=2)

       self.search_var=StringVar()                     

       combosearch1=ttk.Combobox(table_frame,textvariable=self.search_var,font=("axial",12,"bold"),width=20,state="readonly")
       combosearch1["value"]=("Contact","Roomavailable")
       combosearch1.current(0)
       combosearch1.grid(row=0,column=1,padx=2)
       self.searchtxt_var=StringVar()

       searchtxt=ttk.Entry(table_frame,textvariable=self.searchtxt_var,width=20,font=("axial",12,"bold"))
       searchtxt.grid(row=0,column=2,padx=2)

       search2=Button(table_frame,text="Search",command=self.search,font=("axial",12,"bold"),bg="black",fg="gold",width=8)
       search2.grid(row=0,column=3,padx=1)

       showall=Button(table_frame,text="Showall",command=self.fetch_data,font=("axial",12,"bold"),bg="black",fg="gold",width=8)
       showall.grid(row=0,column=4,padx=1)


       detail_frame=Frame(table_frame,bd=3,relief=RIDGE)
       detail_frame.place(x=0,y=50,width=700,height=125)

       scrollx=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
       scrolly=ttk.Scrollbar(detail_frame,orient=VERTICAL)

       self.room_Table=ttk.Treeview(detail_frame,column=("contact","checkin","checkout","roomtype","roomavailable",
                                                  "meal","noofdays"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)

       scrollx.config(command=self.room_Table.xview)
       scrolly.config(command=self.room_Table.yview)

       self.room_Table.heading("contact",text="Contact")
       self.room_Table.heading("checkin",text="Check-in")
       self.room_Table.heading("checkout",text="Check-out")
       self.room_Table.heading("roomtype",text="Room Type")
       self.room_Table.heading("roomavailable",text="Room NO")
       self.room_Table.heading("meal",text="Meal")
       self.room_Table.heading("noofdays",text="NoOfDays")


       self.room_Table["show"]="headings"

       self.room_Table.column("contact",width=100)
       self.room_Table.column("checkin",width=100)
       self.room_Table.column("checkout",width=100)
       self.room_Table.column("roomtype",width=100)
       self.room_Table.column("roomavailable",width=100)
       self.room_Table.column("meal",width=100)
       self.room_Table.column("noofdays",width=100)   
       self.room_Table.pack(fill=BOTH,expand=1)
       self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
       self.fetch_data()


       
    def Fetch_contact(self):
       if self.var_contact.get()=="":
           messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
       else:
           conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
           mycursor=conn.cursor()
           query=("select cus_nam from customer where mobno=%s")
           value=(self.var_contact.get(),)
           mycursor.execute(query,value)
           row=mycursor.fetchone()

           if row==None:
              messagebox.showerror("Error","This number Not Found",parent=self.root)
           else:
              conn.commit()
              conn.close()

              showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
              showDataFrame.place(x=450,y=50,width=250,height=180)

              lbname=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
              lbname.place(x=0,y=0)

              lb=Label(showDataFrame,text=row,font=("arial",12,"bold"))
              lb.place(x=60,y=0)

              conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
              mycursor=conn.cursor()
              query=("select gend from customer where mobno=%s")
              value=(vself.ar_contact.get(),)
              mycursor.execute(query,value)
              row=mycursor.fetchone()

              lbgender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
              lbgender.place(x=0,y=30)

              lb2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
              lb2.place(x=90,y=30)

              conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
              mycursor=conn.cursor()
              query=("select malid from customer where mobno=%s")
              value=(self.var_contact.get(),)
              mycursor.execute(query,value)
              row=mycursor.fetchone()

              lbmailid=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
              lbmailid.place(x=0,y=60)

              lb3=Label(showDataFrame,text=row,font=("arial",12,"bold"))
              lb3.place(x=90,y=60)

            
              conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
              mycursor=conn.cursor()
              query=("select nation from customer where mobno=%s")
              value=(self.var_contact.get(),)
              mycursor.execute(query,value)
              row=mycursor.fetchone()

              lbnation=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
              lbnation.place(x=0,y=90)

              lb4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
              lb4.place(x=90,y=90)

              conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
              mycursor=conn.cursor()
              query=("select addr from customer where mobno=%s")
              value=(self.var_contact.get(),)
              mycursor.execute(query,value)
              row=mycursor.fetchone()

              lbaddress=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
              lbaddress.place(x=0,y=120)

              lb5=Label(showDataFrame,text=row,font=("arial",12,"bold"))
              lb5.place(x=90,y=120)


              
    def search(self):
        conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
        mycursor=conn.cursor()

        mycursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%" +str(self.searchtxt_var.get())+"%'" )
        row=mycursor.fetchall()
        if len(row)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in row:
               self.room_Table.insert("",END,values=i)

        conn.commit()
        conn.close()


    def include_data(self):
      if self.var_contact.get()=='' or self.var_checkin.get()=='':
         messagebox.showerror("error","All fields are required")
      else:
          try:
             conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
             mycursor=conn.cursor()
             mycursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",
                           (self.var_contact.get(),
                            self.var_checkin.get(),
                            self.var_checkout.get(),
                            self.var_roomtype.get(),
                            self.var_roomavailable.get(),
                            self.var_meal.get(),
                            self.var_noofdays.get()))
                            
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("success","Room Booked",parent=self.root)

          except Exception as es:
            messagebox.showwarning("warning",f"something went wrong {str(es)}",parent=self.root)


    def fetch_data(self):
         conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
         mycursor=conn.cursor()
         mycursor.execute("select *  from room")
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
    
       self.var_contact.set(row[0]),
       self.var_checkin.set(row[1]),
       self.var_checkout.set(row[2]),
       self.var_roomtype.set(row[3]),
       self.var_roomavailable.set(row[4]),
       self.var_meal.set(row[5]),
       self.var_noofdays.set(row[6])


    def update( self):
       if  self.var_contact.get()=='':
           messagebox.showerror("error","please enter mobile number")
       else:    
           conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
           mycursor=conn.cursor()
           mycursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where Contact=%s",
                         ( self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(),
                                  self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get(), self.var_contact.get()))

           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("success","Room details has been updated successfully")


    def mDelete(self):
       mDelete=messagebox.askyesno("delete","Do you want to delete this customer")
       if mDelete!=0:
           conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="farhad")
           mycursor=conn.cursor()
           query="delete from room where Contact=%s"
           value=( self.var_contact.get(),)
           mycursor.execute(query,value)
       else:
        if not mDelete:
            return

       conn.commit()
       self.fetch_data()
       conn.close()
    

    def reset_data(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")



    def total(self):
       inDate=self.var_checkin.get()
       outDate=self.var_checkout.get()
       inDate=datetime.strptime(inDate,"%d/%m/%Y")
       outDate=datetime.strptime(outDate,"%d/%m/%Y")
       var_noofdays.set(abs(outDate-inDate).days)

       if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Laxary"):  
          s1=float(400)
          s2=float(1000)
          s3=float(self.var_noofdays.get())
          s4=float(s1+s2)
          s5=float(s3+s4)
          Tax="Rs."+str("%.2f"%((s5)*0.09))
          ST="Rs."+str("%.2f"%((s5)))
          TT="Rs."+str("%.2f"%(s5+((s5)*0.09)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)
       

       elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="single"):  
         s1=float(200)
         s2=float(500)
         s3=float(self.var_noofdays.get())
         s4=float(s1+s2)
         s5=float(s3+s4)
         Tax="Rs."+str("%.2f"%((s5)*0.09))
         ST="Rs."+str("%.2f"%((s5)))
         TT="Rs."+str("%.2f"%(s5+((s5)*0.09)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)


    
       elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):  
         s1=float(300)
         s2=float(700)
         s3=float(self.var_noofdays.get())
         s4=float(s1+s2)
         s5=float(s3+s4)
         Tax="Rs."+str("%.2f"%((s5)*0.09))
         ST="Rs."+str("%.2f"%((s5)))
         TT="Rs."+str("%.2f"%(s5+((s5)*0.09)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self. var_total.set(TT)   
            
   














if __name__== "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop() 
