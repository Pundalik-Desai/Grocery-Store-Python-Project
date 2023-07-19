from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from main import *
from signup import *
import mysql.connector
# from signup import SignUp_Class

# from tkinter import 
        
class LogInPage:

    
    def __init__(self,Login_window):
        self.Login_window = Login_window
        self.Login_window.geometry("1400x800+0+0")
        self.Login_window.title("Log-in Page")
        self.Login_window.config(bg="white")
        self.photo = PhotoImage(file="C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\home-delivery.png")
        self.Login_window.iconphoto(FALSE,self.photo)
    




        # 🤔🤔🙄        
        self.name = StringVar()
        self.Cpassword = StringVar()

# main Bakground Image 
        self.imageFrame_f1 = LabelFrame(self.Login_window,bg="White",borderwidth=3,relief=RAISED,width=850,height=400)
        self.imageFrame_f1.place(x=250,y=125)
        
        self.i1 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\login.png")
        self.i1.resize((398,332),Image.LANCZOS)
        self.i2 = ImageTk.PhotoImage(self.i1)

        self.imageLabel_l2 = Label(self.imageFrame_f1,image=self.i2)
        self.imageLabel_l2.place(x=30,y=35,width=398,height=332)
                
# name and password frame
        self.f2 = Frame(self.imageFrame_f1,bg="white",width=350,height=350)
        self.f2.place(x=460,y=25)

# sign in Label
        self.signin_label = Label(self.f2,text="Sign in",bg="white",fg ="#57a1f8",font=("microsoft yahei ui light",23,"bold"))
        self.signin_label.place(x=120,y=5)

# username entry feild

        global  username
        def on_enter(e):
            self.username.delete(0,END)
            
        def on_exit(e):
            if self.username.get() == "":
                self.username.insert(0,"Username")


        self.username = Entry(self.f2,border=0,bg="white",fg="black",font=("microsoft yahei ui light",10,"bold"),textvariable=self.name)
        self.username.place(x=50,y=90)
        self.username.insert(0,"username")
        self.BorderFrame = Frame(self.f2,width=295,height=2,bg="black")
        self.BorderFrame.place(x=50,y=110)
        self.username.bind("<FocusIn>",on_enter)
        self.username.bind("<FocusOut>",on_exit)

# password entry feild
        def on_entry(e):
            self.password.delete(0,END)
        
        def on_leave(e):
            # self.password["show"]="*"
            # self.password.config(show="*")
            if self.password.get() == "":
                self.password.insert(0,"Password")


        self.password = Entry(self.f2,bg="white",fg="black",font=("microsoft yahei ui light",10,"bold"),border=0,textvariable=self.Cpassword,show="*")
        self.password.place(x=50,y=160)
        self.password.insert(0,'Password')
        self.password.bind("<FocusIn>",on_entry)
        self.password.bind("<FocusOut>",on_leave)
        self.BorderFrame2= Frame(self.f2,bg="black",width=295,height=2)
        self.BorderFrame2.place(x=50,y=180)

# show password function  
        def when_enter(event):
                self.password["show"] = ""
        
        def when_exit(event):
                self.password["show"]="*"
        
        
        self.i3 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\show_password.png")
        self.i3 = self.i3.resize((25,25),Image.LANCZOS)
        self.i4 = ImageTk.PhotoImage(self.i3)
        self.show_password = Button(self.f2,image=self.i4,bg="white",border=0)
        self.show_password.bind("<Button>",when_enter)
        self.show_password.bind("<ButtonRelease>",when_exit)
        self.show_password.place(x=305,y=150,height=25,width=25)

        # self.show_password.bind("<Button-1>",when_exit)


# SIgnIn Button
        self.signin_Button = Button(self.f2,text="Sign in",border=0,cursor="hand2",font=("microsoft yahei ui light",11,"bold"),bg="#57a1f8",fg="white",command=self.signIn)
        self.signin_Button.place(x=50,y=220,width=295,height=40)

# label unser Sign In 
        self.text_ = Label(self.f2,text="Dont have account ?..",font=("microsoft yahei ui light",10,"bold"),border=0,bg="white",fg="black")
        self.text_.place(x=90,y=275,width=170,height=20)

# sign up Button
        self.sign_up_button = Button(self.f2,text="Sign up",bg="white",fg="blue",font=("microsoft yahei ui",10,"bold"),border=0,cursor="hand2",command=self.SignUp_function)
        # self.sign_up_button.bind("<<Return>>",rnFunction)
        self.sign_up_button.place(x=245,y=275,width= 65,height=20)

# forget Password button
        self.forget_password = Button(self.f2,text="Forget Password ? 🤔🙄",font=("microsoft yahei ui",10,"bold"),bg="white",border=0,fg="steelblue",cursor="hand2",command=self.ForgotPass)
        self.forget_password.place(x=100,y=300,width=200,height=20)

        

# function for sign in button
    def signIn(self):
        
        flagregister = True

        
        self.conn=mysql.connector.connect(host="localhost",user="root",password="030803",db="gcsystem") 
        mycursor = self.conn.cursor()
               
        query1 = "select * from signup where username =%s"
        value = (self.username.get(),)
        
        mycursor.execute(query1,value)
        row = mycursor.fetchone()
        # if row[0] != self.username.get():

        #         messagebox.showerror("error","username not found!!")
        # print(row[0])               
                
        if row != None: 
               
                if row[8] != self.Cpassword.get():
               
                        messagebox.showerror("Error","Password doest match!!")
               
                else:   
                        messagebox.showinfo("Welcome","Log in Successful !!")

                        import main 
                        
                        username_lg = self.username.get()

                        self.Login_window.destroy()

                        # calling strore window and calling Store class in main.py
                        self.GC=Tk()
                        obj=main.Store(self.GC,username_lg)         


                        # self.new_window = Toplevel(Login_window)
                        # self.store = Store(self.new_window)
                        
                        # print("something went wrong...")
        
                        # messagebox.showerror("Error","wrong username or password...")
        else:
              messagebox.showerror("error","username not found!!")
        
# function for new user or sign up window 
    def SignUp_function(self):
        import signup
        # destroying CURRENT window and calling sign up window 
        self.Login_window.destroy()
 
        self.Signup_window=Tk()
        obj = signup.SignUp_Class(self.Signup_window)

# function for forgot password
    def ForgotPass(self):
        import forgetPasswor

        self.Login_window.destroy()

        self.forgetpassword_window = Tk()
        obj = forgetPasswor.ForgetPassword(self.forgetpassword_window)


if __name__ == "__main__" :
    Login_window = Tk()
    obj = LogInPage(Login_window)
    Login_window.mainloop()