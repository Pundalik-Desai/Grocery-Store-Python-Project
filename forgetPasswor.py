from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk
import email_pass
import smtplib
import random
import urllib


class ForgetPassword :
    def __init__(self,forgetpassword_window):

        self.forgetpassword_window = forgetpassword_window
        self.forgetpassword_window.geometry("1355x700+0+0")
        self.forgetpassword_window.title("Forget Password")
        self.forgetpassword_window.config(bg="salmon")
        self.photo = PhotoImage(file="C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\home-delivery.png")
        self.forgetpassword_window.iconphoto(FALSE,self.photo)

        # self.forgetpassword_window.configure(color="Red")
        
# main Bakground Image 
        self.imageFrame_f1 = LabelFrame(self.forgetpassword_window,bg="White",borderwidth=3,relief=RAISED,width=850,height=400)
        self.imageFrame_f1.place(x=250,y=125)
        
        self.i1 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\Forgotpassword.png")
        self.i1.resize((400,350),Image.LANCZOS)
        self.i2 = ImageTk.PhotoImage(self.i1)

        self.imageLabel_l2 = Label(self.imageFrame_f1,image=self.i2)
        self.imageLabel_l2.place(x=30,y=35,width=392,height=332)

# Label frame for title
        self.title_label = Label(self.imageFrame_f1,text="Forgot Password",font=("microsoft yahei ui light",20,"bold"),fg="salmon",bg="white")
        self.title_label.place(x=510,y=5)


# name and password frame
        self.f2 = Frame(self.imageFrame_f1,bg="white",width=440,height=345)
        self.f2.place(x=405,y=50)


# entry feilds
        # event functions for enter email entry
        # def onEnter1(event):
        #     self.email_entry.delete(0,END)
        def onExit1(event):
            if self.email_entry.get() == "":
                self.email_entry.insert(0,"enter email")


# enter email entry feild
        self.email_entry = Entry(self.f2,font=("microsoft yahei ui light",13,"bold"),bg="white",width=42,borderwidth=0,justify=CENTER)
        # self.email_entry.bind("<FocusIn>",onEnter1)
        self.email_entry.bind("<FocusOut>",onExit1)
        self.email_entry.grid(row=0,column=0,padx=6,pady=30)
        self.email_entry.insert(0,"enter email")

        self.borderframe = Frame(self.f2,bg="salmon",width=420,height=2)
        self.borderframe.place(x=6,y=55)
        
        
# get otp button

        self.getotp_button = Button(self.f2,text="get OTP",font=("microsoft yahei ui light",11,"bold"),borderwidth=0,bg="salmon",fg="white",width=30,height=1,command=self.send_otp)
        self.getotp_button.grid(row=1,column=0)

# enter otp

        # event functions for enter new password entry
        def onEnter2(event):
            self.enterOTP_entry.delete(0,END)
        def onExit2(event):
            if self.enterOTP_entry.get() == "":
                self.enterOTP_entry.insert(0,"enter OTP")


        self.enterOTP_entry = Entry(self.f2,font=("microsoft yahei ui light",13,"bold"),bg="white",width=22,borderwidth=0,justify=CENTER)
        self.enterOTP_entry.bind("<FocusIn>",onEnter2)
        self.enterOTP_entry.bind("<FocusOut>",onExit2)
        self.enterOTP_entry.grid(row=2,column=0,padx=6,pady=30,sticky=W)
        self.enterOTP_entry.insert(0,"enter OTP")

        self.borderframe = Frame(self.f2,bg="salmon",width=210,height=2)
        self.borderframe.place(x=6,y=170)

# submit opt Button
        self.submitotp_button = Button(self.f2,text="submit",font=("microsoft yahei ui light",11,"bold"),borderwidth=0,bg="salmon",fg="white",width=15,height=1,state="disabled",command=self. submit_otp)
        self.submitotp_button.place(x=250,y=140)

# enter new password entry

        def onEnter3(event):
            self.newpassword_entry.delete(0,END)
        def onExit3(event):
            if self.newpassword_entry.get() == "":
                self.newpassword_entry.insert(0,"new password")

        self.newpassword_entry = Entry(self.f2,font=("microsoft yahei ui light",13,"bold"),bg="white",width=42,borderwidth=0,justify=CENTER)
        self.newpassword_entry.bind("<FocusIn>",onEnter3)
        self.newpassword_entry.bind("<FocusOut>",onExit3)
        self.newpassword_entry.grid(row=3,column=0,padx=6,pady=10)
        self.newpassword_entry.insert(0,"new password")

        self.borderframe = Frame(self.f2,bg="salmon",width=420,height=2)
        self.borderframe.place(x=6,y=235)
        


# enter update password button
        self.update_password = Button(self.f2,text="update password",font=("microsoft yahei ui light",11,"bold"),borderwidth=0,bg="salmon",fg="white",width=30,height=1,state="disabled",command=self.update_pass)
        self.update_password.grid(row=4,column=0,pady=15)

        import random
        self.otp= random.randint(100001,999999)\
                
        print(self.otp)
        self.OTP_ = self.otp
        print(self.OTP_)

# fuctions

# function for checking email

    def send_otp(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="030803",db="gcsystem")
        mycursor = conn.cursor()

        query1 = "select * from signup where email =%s"
        value = (self.email_entry.get(),)

        mycursor.execute(query1,value)
        row = mycursor.fetchone()
         
        if  row  != None:
                
                import socket
                
                def check_internet():
                        try:
                                # create a socket object
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                #   s.settimeout(5) # set a timeout for the connection attempt

                                # try to connect to a well-known internet host
                                s.connect(('www.google.com', 80))
                                s.close()
                                return True
                        except:
                                return False
                                # display a message box indicating internet connection is successful
                #   messagebox.showinfo("Internet Status", "Device is connected to the internet.")
                if check_internet():

                        # sending otp 
                        s = smtplib.SMTP('smtp.gmail.com',587)
                        s.starttls()

                        #lognin 
                        email_  = email_pass.email_
                        pass_ = email_pass.pass_

                        s.login(email_,pass_)
                        
                        subject = "Reset Password"
                        msg = f"Dear sir/Madam ,\n\n Your username is {row[0]}\nYour OTP for reset password is\n{self.otp}\n\nThank you"
                        msg="Subject:{}\n\n{}".format(subject,msg)

                        s.sendmail(email_,self.email_entry.get(),msg)
                        check=s.ehlo()

                        if check[0] == 250:

                                messagebox.showinfo("INFO","OTP has send on your email address\nplese check email and enter OTP") 
                                self.submitotp_button["state"] = "normal"

                        else :
                                messagebox.showerror("Error Somethion went wrong\nplease try again")


                
                        self.enterOTP_entry.focus_set()
                else:

                     messagebox.showerror("Error","No Interner Conncetion!!\nPlease connect to Internet")
        else:
            messagebox.showerror("Error","No user found with this email\nIf dont have account plese register first")        

# function for check otp

    def submit_otp(self):

        check_otp = self.enterOTP_entry.get()
        print(check_otp)

        if check_otp == str(self.OTP_) :
                messagebox.showinfo("INFO","OTP Verified\nEnter your new password!!!")
                self.update_password["state"] = "normal"
        
        else:
             messagebox.showerror("ERROR","OTP not matched\nincase please try again!!")

# function for update password
    def update_pass(self) : 
        conn = mysql.connector.connect(host="localhost",user="root",password="030803",db="gcsystem")
        mycursor = conn.cursor()

        query = "update signup set password = %s where email = %s"
        value = (self.newpassword_entry.get(),self.email_entry.get())
        
        mycursor.execute(query,value)

        conn.commit()
        conn.close()

        messagebox.showinfo("INFO","Password Updated Successfully\nPlease login again!!")

        import loginPage

        self.forgetpassword_window.destroy()

        self.Login_window = Tk()
        obj = loginPage.LogInPage(self.Login_window)


if __name__ == "__main__" :
    
    forgetpassword_window = Tk()
    obj = ForgetPassword(forgetpassword_window)
    forgetpassword_window.mainloop()
