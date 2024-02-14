from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from homepg import HotelManagementSystem

def main():
    win=Tk()
    app= Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        self.bg=ImageTk.PhotoImage(file=r"E:\hotel mng\image10.JPG")

        lba=Label(self.root,image=self.bg)
        lba.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=520,y=150,width=340,height=450)

        img=Image.open(r"C:\Users\User\Downloads\icons8-login-64.PNG")
        img1=img.resize((100,100),Image.LANCZOS)
        self.img2=ImageTk.PhotoImage(img1)
        lbb=Label(image=self.img2,bg="black",borderwidth=0)
        lbb.place(x=640,y=150,width=100,height=100)

        lbc=Label(frame,text="Get Started",font=("times new roman",16,"bold"),fg="white",bg="black")
        lbc.place(x=105,y=95)

        username=Label(frame,text="Username",font=("times new roman",14,"bold"),fg="white",bg="black")
        username.place(x=65,y=130)

        self.txtuser=ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.txtuser.place(x=40,y=155,width=270)

        password=Label(frame,text="Password",font=("times new roman",14,"bold"),fg="white",bg="black")
        password.place(x=65,y=200)

        self.txtpassword=ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.txtpassword.place(x=40,y=225,width=270)

        img=Image.open(r"C:\Users\User\Downloads\icons8-login-64.PNG")
        img2=img.resize((30,30),Image.LANCZOS)
        self.img3=ImageTk.PhotoImage(img2)
        lbb=Label(image=self.img3,bg="black",borderwidth=0)
        lbb.place(x=560,y=275,width=30,height=30)

        img1=Image.open(r"C:\Users\User\Downloads\icons8-login-64.PNG")
        img4=img1.resize((30,30),Image.LANCZOS)
        self.img5=ImageTk.PhotoImage(img2)
        lbb=Label(image=self.img5,bg="black",borderwidth=0)
        lbb.place(x=560,y=345,width=30,height=30)

        loginbutton=Button(frame,text="Login",font=("times new roman",14,"bold"),bd=1,relief=RIDGE,fg="white",bg="red",
                           activeforeground="white",activebackground="red",command=self.login)
        loginbutton.place(x=70,y=290,width=200,height=40)

        registerbutton=Button(frame,text="New User Register",borderwidth=0,font=("times new roman",10,"bold"),relief=RIDGE,fg="white",bg="black",
                           activeforeground="white",activebackground="black",command=self.register_window)
        registerbutton.place(x=90,y=360,width=150)

       
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","all fields are required")
        elif self.txtuser.get()=="Syed" and self.txtpassword.get()=="Mohideen":
            messagebox.showinfo("Success","Welcome to Arab hotel")
        else:
            conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="prophet")
            cur=conn.cursor()
            cur.execute("select * from Register where email=%s and password=%s",(
                                                                                 self.txtuser.get(),
                                                                                 self.txtpassword.get()
                                                                                 ))
            row=cur.fetchone()
            if row!= None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("yesno","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
            




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()










        self.bg=ImageTk.PhotoImage(file=r"E:\hotel mng\imageh9.JPG")
        lb1=Label(self.root,image=self.bg)
        lb1.place(x=0,y=0,relwidth=1,relheight=1)

        
        self.bg1=ImageTk.PhotoImage(file=r"E:\hotel mng\imageh4.JPG")
        lb2=Label(self.root,image=self.bg1)
        lb2.place(x=50,y=100,width=420,height=500)

        frame=Frame(self.root,bg="white")
        frame.place(x=470,y=100,width=700,height=500)

        register_lba=Label(frame,text="REGISTER HERE",font=("times new roman",16,"bold"),fg="darkgreen",bg="white")
        register_lba.place(x=25,y=25)

        fname=Label(frame,text="First Name",font=("times new roman",14,"bold"),bg="white")
        fname.place(x=50,y=85)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",12,"bold"))
        self.fname_entry.place(x=50,y=115,width=240)

        
        lname=Label(frame,text="Last Name",font=("times new roman",14,"bold"),bg="white")
        lname.place(x=380,y=85)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",12,"bold"))
        self.lname_entry.place(x=380,y=115,width=240)

        contact=Label(frame,text="Contact",font=("times new roman",14,"bold"),bg="white")
        contact.place(x=50,y=160)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",12,"bold"))
        self.contact_entry.place(x=50,y=190,width=240)
        
        email=Label(frame,text="Mail ID",font=("times new roman",14,"bold"),bg="white")
        email.place(x=380,y=160)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",12,"bold"))
        self.email_entry.place(x=380,y=190,width=240)
        
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",14,"bold"),bg="white")
        security_Q.place(x=50,y=230)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","YournBirth Place","Your Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=260,width=240)
        self.combo_security_Q.current(0)

   
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",14,"bold"),bg="white")
        security_A.place(x=380,y=230)

        self.security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",12,"bold"))
        self.security_A_entry.place(x=380,y=260,width=240)
        
        password=Label(frame,text="Password",font=("times new roman",14,"bold"),bg="white")
        password.place(x=50,y=300)

        self.password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",12,"bold"))
        self.password_entry.place(x=50,y=330,width=240)
        
        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",14,"bold"),bg="white")
        confirm_password.place(x=380,y=300)

        self.confirm_password_entry=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",12,"bold"))
        self.confirm_password_entry.place(x=380,y=330,width=240)
        
        self.var_check=IntVar()
        checkbutton=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbutton.place(x=50,y=380)


        img=Image.open(r"C:\Users\User\Downloads\login-button-png-18030.PNG")
        image=img.resize((250,50),Image.LANCZOS)
        self.image1=ImageTk.PhotoImage(image)

        b1=Button(frame,image=self.image1,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=280)

        
        img2=Image.open(r"C:\Users\User\Downloads\register-button-png-18469.PNG")
        image2=img2.resize((200,50),Image.LANCZOS)
        self.image3=ImageTk.PhotoImage(image2)

        b1=Button(frame,command=self.register_data,image=self.image3,borderwidth=0,cursor="hand2")
        b1.place(x=380,y=420,width=280)

    def register_data(self):
       if self.var_fname.get()==""or self.var_email.get()=="" or self.var_securityQ.get()=="select":
          messagebox.showerror("Error","All fields are required")
       elif self.var_password.get()!=self.var_confirm_password.get():
          messagebox.showerror("Error","Password Should Be Matched")
       elif self.var_check.get()==0:
          messagebox.showerror("Error","Please agree our terms and conditions")
       else:
          conn=mysql.connector.connect(port=3307,user="root",password="ejaz",database="prophet")
          cur=conn.cursor()
          query=("select * from Register where email=%s")
          value=(self.var_email.get(),)
          cur.execute(query,value)
          row=cur.fetchone()
          if row!=None:
              messagebox.showerror("Error","User already exist, please try another email")
          else:
              cur.execute("insert into Register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                              self.var_fname.get(),
                                                                              self.var_lname.get(),
                                                                              self.var_contact.get(),
                                                                              self.var_email.get(),
                                                                              self.var_securityQ.get(),
                                                                              self.var_securityA.get(),
                                                                              self.var_password.get()
                                                                              ))
          conn.commit()
          conn.close()
          messagebox.showinfo("Success","Register Successfully")
                
            


        
        
                    
            
            




        



        

        


        





if __name__== "__main__":
   main()
