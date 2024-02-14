from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector as connection
from tkinter import messagebox

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("SPORTS MANAGEMENT SYSTEM")
        self.root.geometry("1136x460+230+250")


  

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cus_nam=StringVar()
        self.var_gend=StringVar()
        self.var_mobno=StringVar()
        self.var_malid=StringVar()
        self.var_nation=StringVar()
        self.var_addr=StringVar()
        self.var_cus_ref_add=StringVar()


        la2=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        la2.place(x=0,y=0,width=1136,height=50)

        p1=Image.open("imageh5.jpg")
        p1=p1.resize((100,50),Image.LANCZOS)
        self.p3=ImageTk.PhotoImage(p1)
        lab=Label(self.root,image=self.p3,bd=0,relief=RIDGE)
        lab.place(x=0,y=0,width=100,height=50)

        lable_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        lable_frame.place(x=5,y=50,width=430,height=390)

        customer_ref=Label(lable_frame,text="Customer Reference",font=("axial",12,"bold"),padx=2,pady=5)
        customer_ref.grid(row=0,column=0,sticky=W)

        refentry=ttk.Entry(lable_frame,width=18,textvariable=self.var_ref,font=("axial",12,"bold"),state="readonly")
        refentry.grid(row=0,column=1)

        customer_name=Label(lable_frame,text="Customer Name",font=("axial",12,"bold"),padx=2,pady=5)
        customer_name.grid(row=1,column=0,sticky=W)

        refentry=ttk.Entry(lable_frame,textvariable=self.var_cus_nam,width=18,font=("axial",12,"bold"))
        refentry.grid(row=1,column=1)

        gender=Label(lable_frame,text="Gender",font=("axial",12,"bold"),padx=2,pady=5)
        gender.grid(row=2,column=0,sticky=W)

        combogender=ttk.Combobox(lable_frame,textvariable=self.var_gend,font=("axial",12,"bold"),width=18,state="readonly")
        combogender["value"]=("male","female","other")
        combogender.current(0)
        combogender.grid(row=2,column=1)

        customer_phno=Label(lable_frame,text="Mobile Number",font=("axial",12,"bold"),padx=2,pady=5)
        customer_phno.grid(row=3,column=0,sticky=W)

        refentry=ttk.Entry(lable_frame,textvariable=self.var_mobno,width=18,font=("axial",12,"bold"))
        refentry.grid(row=3,column=1)


        customer_email=Label(lable_frame,text="Mail ID",font=("axial",12,"bold"),padx=2,pady=5)
        customer_email.grid(row=4,column=0,sticky=W)

        refentry=ttk.Entry(lable_frame,textvariable=self.var_malid,width=18,font=("axial",12,"bold"))
        refentry.grid(row=4,column=1)

        customer_nationality=Label(lable_frame,text="Nationality",font=("axial",12,"bold"),padx=2,pady=5)
        customer_nationality.grid(row=5,column=0,sticky=W)

        combogender1=ttk.Combobox(lable_frame,textvariable=self.var_nation,font=("axial",12,"bold"),width=18,state="readonly")
        combogender1["value"]=("indian","pakistani","saudhi")
        combogender1.current(0)
        combogender1.grid(row=5,column=1)

        customer_address=Label(lable_frame,text="Customer Address",font=("axial",12,"bold"),padx=2,pady=5)
        customer_address.grid(row=6,column=0,sticky=W)

        refentry=ttk.Entry(lable_frame,textvariable=self.var_addr,width=18,font=("axial",12,"bold"))
        refentry.grid(row=6,column=1)

        customer_refaddress=Label(lable_frame,text="Customer Reference Address",font=("axial",12,"bold"),padx=2,pady=5)
        customer_refaddress.grid(row=7,column=0,sticky=W)

        refentry=ttk.Entry(lable_frame,textvariable=self.var_cus_ref_add,width=18,font=("axial",12,"bold"))
        refentry.grid(row=7,column=1)

        b1=Frame(lable_frame,bd=2,relief=RIDGE)
        b1.place(x=0,y=300,width=400,height=35)

        add=Button(b1,text="Add",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.include_data)
        add.grid(row=0,column=0,padx=1)

        update=Button(b1,text="Update",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.update)
        update.grid(row=0,column=1,padx=1)

        delete=Button(b1,text="Delete",font=("axial",12,"bold"),bg="black",fg="gold",width=8,command=self.mDelete)
        delete.grid(row=0,column=2,padx=1)

        reset=Button(b1,text="Reset",font=("axial",12,"bold"),bg="black",fg="gold",width=11,command=self.reset_data)
        reset.grid(row=0,column=3,padx=1)


        table_frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=50,width=700,height=390)

        label_search=Label(table_frame,text="Search by",font=("axial",12,"bold"),bg="red",fg="white")
        label_search.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()                     

        combosearch1=ttk.Combobox(table_frame,textvariable=self.search_var,font=("axial",12,"bold"),width=20,state="readonly")
        combosearch1["value"]=("Mobno","Cus_nam")
        combosearch1.current(0)
        combosearch1.grid(row=0,column=1,padx=2)
        
        self.searchtxt_var=StringVar()
        searchtxt=ttk.Entry(table_frame,textvariable=self.searchtxt_var,width=20,font=("axial",12,"bold"))
        searchtxt.grid(row=0,column=2,padx=2)

        search2=Button(table_frame,text="Search",font=("axial",12,"bold"),bg="black",fg="gold",width=8)
        search2.grid(row=0,column=3,padx=1)

        showall=Button(table_frame,text="Showall",font=("axial",12,"bold"),bg="black",fg="gold",width=8)
        showall.grid(row=0,column=4,padx=1)

        detail_frame=Frame(table_frame,bd=3,relief=RIDGE)
        detail_frame.place(x=0,y=50,width=700,height=300)

        scrollx=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(detail_frame,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(detail_frame,column=("var_ref","cus_nam","gend","mobno","malid",
                                                  "nation","addr","cus_ref_add"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.Cust_Details_Table.xview)
        scrolly.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("var_ref",text="Customer Reference")
        self.Cust_Details_Table.heading("cus_nam",text="Customer Name")
        self.Cust_Details_Table.heading("gend",text="Gender")
        self.Cust_Details_Table.heading("mobno",text="Mobile Number")
        self.Cust_Details_Table.heading("malid",text="Mail ID")
        self.Cust_Details_Table.heading("nation",text="Nationality")
        self.Cust_Details_Table.heading("addr",text="Address")
        self.Cust_Details_Table.heading("cus_ref_add",text="Customer Reference Address")


        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("var_ref",width=100)
        self.Cust_Details_Table.column("cus_nam",width=100)
        self.Cust_Details_Table.column("gend",width=100)
        self.Cust_Details_Table.column("mobno",width=100)
        self.Cust_Details_Table.column("malid",width=100)
        self.Cust_Details_Table.column("nation",width=100)
        self.Cust_Details_Table.column("addr",width=100)
        self.Cust_Details_Table.column("cus_ref_add",width=100)


        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def include_data(self):
        if self.var_mobno.get()=='' or self.var_malid.get()=='':
           messagebox.showerror("error","All fields are required")
        else:
          try:
              conn=connection.connect(port=3307,user="root",password="ejaz",database="farhad")
              mycursor=conn.cursor()
              mycursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",
                           (self.var_ref.get(),self.var_cus_nam.get(),self.var_gend.get(),self.var_mobno.get(),
                                 self.var_malid.get(),self.var_nation.get(),self.var_addr.get(),self.var_cus_ref_add.get()))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("success","Customer has been added",parent=self.root)

          except Exception as es:
              messagebox.showwarning("warning",f"something went wrong {str(es)}",parent=self.root)


              
    def fetch_data(self):
         conn=connection.connect(port=3307,user="root",password="ejaz",database="farhad")
         mycursor=conn.cursor()
         mycursor.execute("select *  from customer")
         rows=mycursor.fetchall()
         if len(rows)!=0:
             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
             for i in rows:
                 self.Cust_Details_Table.insert("",END,values=i)

             conn.commit()
         conn.close()

    def get_cursor(self,event=""):
         cursor_row=self.Cust_Details_Table.focus()
         content=self.Cust_Details_Table.item(cursor_row)
         row=content["values"]

         self.var_ref.set(row[0]),
         self.var_cus_nam.set(row[1]),
         self.var_gend.set(row[2]),
         self. var_mobno.set(row[3]),
         self.var_malid.set(row[4]),
         self.var_nation.set(row[5]),
         self.var_addr.set(row[6]),
         self.var_cus_ref_add.set(row[7])

    def update(self):
      if self.var_mobno.get()=='':
         messagebox.showerror("error","please enter mobile number",parent=self.root)
      else:    
         conn=connection.connect(port=3307,user="root",password="ejaz",database="farhad")
         mycursor=conn.cursor()
         mycursor.execute("update customer set cus_nam=%s,gend=%s,mobno=%s,malid=%s,nation=%s,addr=%s,cus_ref_add=%s where cus_ref=%s",
                         (self.var_cus_nam.get(),self.var_gend.get(),self.var_mobno.get(),
                                 self.var_malid.get(),self.var_nation.get(),self.var_addr.get(),self.var_cus_ref_add.get(),self.var_ref.get()))

         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("success","customer details has been updated successfully",parent=self.root)


    def mDelete(self):
      mDelete=messagebox.askyesno("delete","Do you want to delete this customer",parent=self.root)
      if mDelete>0:
         conn=connection.connect(port=3307,user="root",password="ejaz",database="farhad")
         mycursor=conn.cursor()
         query="delete from customer where cus_ref=%s"
         value=(self.var_ref.get(),)
         mycursor.execute(query,value)
      else:
        if not mDelete:
            return

        conn.commit()
        self.fetch_data()
        conn.close()


    def reset_data(self):
        self.var_ref.set(""),
        self.var_cus_nam.set(""),
        #self.var_gend.set(""),
        self.var_mobno.set(""),
        self.var_malid.set(""),
        #self.var_nation.set(""),
        self.var_addr.set(""),
        self.var_cus_ref_add.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):
        conn=connection.connect(port=3307,user="root",password="ejaz",database="farhad")
        mycursor=conn.cursor()

        mycursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%" +str(self.searchtxt_var.get())+"%'" )
        row=mycursor.fetchall()
        if len(row)!=0:
           self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
           for i in row:
               self.Cust_Details_Table.insert("",END,values=i)

        conn.commit()
        conn.close()           






     



if __name__== "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
