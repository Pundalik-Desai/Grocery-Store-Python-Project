from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
from loginPage import *
import mysql.connector
# from loginPage import LogInPage 

class SignUp_Class:

    def __init__(self,Signup_window):

        self.Signup_window = Signup_window
        self.Signup_window.geometry("1355x700+0+0")
        self.Signup_window.title("SIgn Up")
        self.Signup_window.config(bg="palegreen")
        self.Signup_window.resizable(FALSE,FALSE)
        self.photo = PhotoImage(file="C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\home-delivery.png")
        self.Signup_window.iconphoto(FALSE,self.photo)
#--------------------------------------------------------------------------------------------------------

        # Label for background
        # self.main_frame_1 = Frame(Signup_window,bg="red")
        # self.main_frame_1.place(x=0,y=0,width=1370,height=710)
        
        # main background image
        # self.back_i1 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\image12.png")
        # self.back_i1 = self.back_i1.resize((1370,710),Image.LANCZOS)
        # self.back_i2 = ImageTk.PhotoImage(self.back_i1)

        # self.main_l1 = Label(Signup_window,image=self.back_i2)
        # self.main_l1.place(x=0,y=0,width=1370,height=710)

#--------------------------------------------------------------------------------------------------------
# Variables
        self.username_string = StringVar()
        self.name_string = StringVar()
        self.email_string = StringVar()
        self.address_string = StringVar()
        self.phone_string = StringVar()
        self.city_string = StringVar()
        self.state_string = StringVar()
        self.pincode_string = StringVar()
        self.password_string = StringVar()


#--------------------------------------------------------------------------------------------------------
        self.imageFrame_f1 = LabelFrame(self.Signup_window,bg="White",borderwidth=3,relief=RAISED,width=1100,height=500)
        self.imageFrame_f1.place(x=140,y=100)
        
        self.i1 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\image17.png")
        self.i1.resize((5000,3000),Image.LANCZOS)
        self.i2 = ImageTk.PhotoImage(self.i1)

        self.imageLabel_l2 = Label(self.imageFrame_f1,image=self.i2,bg="white")
        self.imageLabel_l2.place(x=30,y=70,width=398,height=332)
#--------------------------------------------------------------------------------------------------------


# sign up Label

        self.signup_label = Label(self.imageFrame_f1,text="Sign Up",font=("microsoft yahei ui light",25,"bold"),bg="white",fg="Green")
        self.signup_label.place(x=580,y=0,width=300,height=80) 
#--------------------------------------------------------------------------------------------------------


# label frame for sign up window like name email ect

        self.signup_labelFrame = LabelFrame(self.imageFrame_f1,bg="white",bd=0,borderwidth=0)
        self.signup_labelFrame.place(x=450,y=90,width=640,height=390)
#--------------------------------------------------------------------------------------------------------
    

# username feild

        # function for username
        def onEnter1(event):
            self.username_sw.delete(0,END)
        
        def onExtit1(event):
            if self.username_sw.get() == "":
                self.username_sw.insert(0,"Username")

        
        self.username_sw = Entry(self.signup_labelFrame,fg="black",font=("microsoft yahei ui light",13,"bold"),borderwidth=0,width=25,textvariable=self.username_string)
        self.username_sw.bind("<FocusIn>",onEnter1)
        self.username_sw.bind("<FocusOut>",onExtit1)
        self.username_sw.grid(row=0,column=0,sticky=W)
        self.username_sw.insert(0,"username")
        self.BorderFrame = Frame(self.signup_labelFrame,width=250,height=2,bg="lime")
        self.BorderFrame.grid(row=1,column=0,sticky=W)


#--------------------------------------------------------------------------------------------------------
        

# name feild

        # function for name feild
        def onEnter2(event):
                self.name_sw.delete(0,END)
        def onExtit2(event):
                if self.name_sw.get() == "":
                     self.name_sw.insert(0,"name")

        self.name_sw = Entry(self.signup_labelFrame,fg="black",font=("microsoft yahei ui light",13,"bold"),borderwidth=0,width=25,textvariable=self.name_string)
        self.name_sw.bind("<FocusIn>",onEnter2)
        self.name_sw.bind("<FocusOut>",onExtit2)
        self.name_sw.grid(row=0,column=1,padx=120,sticky=W)
        self.name_sw.insert(0,"name")
       
        self.BorderFrame = Frame(self.signup_labelFrame,width=250,height=2,bg="lime")
        self.BorderFrame.grid(row=1,column=1,padx=120,sticky=W)
#--------------------------------------------------------------------------------------------------------

# email address feild

        # function for email feild
        def onEnter3(event):
                self.email_sw.delete(0,END)
        def onExtit3(event):
                if self.email_sw.get() == "":
                     self.email_sw.insert(0,"email")

        self.email_sw = Entry(self.signup_labelFrame,fg="black",font=("microsoft yahei ui light",13,"bold"),borderwidth=0,width=25,textvariable=self.email_string)
        self.email_sw.bind("<FocusIn>",onEnter3)
        self.email_sw.bind("<FocusOut>",onExtit3)
        self.email_sw.grid(row=6,column=0,sticky=W,pady=50)
        self.email_sw.insert(0,"email")
        self.BorderFrame = Frame(self.signup_labelFrame,width=250,height=2,bg="lime")
        self.BorderFrame.place(x=00,y=100)

#--------------------------------------------------------------------------------------------------------

# phone number info feild
       
        # function for name feild
        def onEnter4(event):
                self.phoneno_sw.delete(0,END)
        def onExtit4(event):
                if self.phoneno_sw.get() == "":
                     self.phoneno_sw.insert(0,"phone number")

        self.phoneno_sw = Entry(self.signup_labelFrame,fg="black",font=("microsoft yahei ui light",13,"bold"),borderwidth=0,width=25,textvariable=self.phone_string)
        self.phoneno_sw.bind("<FocusIn>",onEnter4)
        self.phoneno_sw.bind("<FocusOut>",onExtit4)
        self.phoneno_sw.grid(row=6,column=1,sticky=W,pady=50,padx=120)
        self.phoneno_sw.insert(0,"phone number")
        
        self.BorderFrame = Frame(self.signup_labelFrame,width=250,height=2,bg="lime")
        self.BorderFrame.place(x=380,y=100)


#--------------------------------------------------------------------------------------------------------
# address  feild:
      

        # function for house number feild
        def onEnter5(event):
                self.houseno_sw.delete(0,END)
        def onExtit5(event):
                if self.houseno_sw.get() == "":
                     self.houseno_sw.insert(0,"house no / flat no , build no, lane / area name")
        
        self.houseno_sw = Entry(self.signup_labelFrame,fg="black",width=62,borderwidth=0,font=("microsoft yahei ui light",13,"bold"),textvariable=self.address_string)
        self.houseno_sw.bind("<FocusIn>",onEnter5)
        self.houseno_sw.bind("<FocusOut>",onExtit5)
        self.houseno_sw.grid(row=7,column=0,sticky=W,pady=0,columnspan=2)
        self.houseno_sw.insert(0,"house no / flat no , build no, lane / area name")
        
        self.BorderFrame = Frame(self.signup_labelFrame,bg="lime",width=620,height=2)
        self.BorderFrame.place(x=0,y=175)

#--------------------------------------------------------------------------------------------------------
# city feild

        # function for city feild
        def onEnter6(event):
                self.city_sw.delete(0,END)
        def onExtit6(event):
                if self.city_sw.get() == "":
                     self.city_sw.insert(0,"city")
        
        self.city_sw = Entry(self.signup_labelFrame,fg="black",width=14,borderwidth=0,font=("microsoft yahei ui light",13,"bold"),textvariable=self.city_string)
        self.city_sw.bind("<FocusIn>",onEnter6)
        self.city_sw.bind("<FocusOut>",onExtit6)
        self.city_sw.grid(row=8,column=0,sticky=W,pady=50,columnspan=2)
        self.city_sw.insert(0,"city")
        
        self.BorderFrame = Frame(self.signup_labelFrame,bg="lime",width=145,height=2)
        self.BorderFrame.place(x=0,y=250)
#--------------------------------------------------------------------------------------------------------
# state feild

        # function for state feild
        def onEnter7(event):
                self.state_sw.delete(0,END)
        def onExtit7(event):
                if self.state_sw.get() == "":
                     self.state_sw.insert(0,"state")

        # self.state = ["select state","Andhra Pradesh","Arunachal Pradesh","Asam","Bihar","Chattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jarkhand","Karnataka","Kerala","Madhya Pradesh","Maharashta","Manipur","Mghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamilnadu","Teklangana","Tripura","Uttarakhand","Uttar Pradesh","West Bangal"]
        
        self.state_sw = Entry(self.signup_labelFrame,width=20,fg="black",font=("microsoft yahei ui light",13,"bold"),borderwidth=0,textvariable=self.state_string)
        self.state_sw.bind("<FocusIn>",onEnter7)
        self.state_sw.bind("<FocusOut>",onExtit7)
        self.state_sw.grid(row=8,column=0,columnspan=2,sticky=W,pady=50,padx=210)

        # self.state_sw.config(value=self.state)
        self.state_sw.insert(0,"state")
        
        self.BorderFrame = Frame(self.signup_labelFrame,bg="lime",width=200,height=2)
        self.BorderFrame.place(x=210,y=250)
        
#--------------------------------------------------------------------------------------------------------
# pincode feild

        # function for pincode feild
        def onEnter8(event):
                self.pincode_sw.delete(0,END)
        def onExtit8(event):
                if self.pincode_sw.get() == "":
                     self.pincode_sw.insert(0,"pincode")
        
        self.pincode_sw = Entry(self.signup_labelFrame,fg="black",width=14,borderwidth=0,font=("microsoft yahei ui light",13,"bold"),textvariable=self.pincode_string)
        self.pincode_sw.bind("<FocusIn>",onEnter8)
        self.pincode_sw.bind("<FocusOut>",onExtit8)
        self.pincode_sw.grid(row=8,column=0,columnspan=40,pady=50,padx=480,sticky=W)
        self.pincode_sw.insert(0,"pincode")
        
        self.BorderFrame = Frame(self.signup_labelFrame,bg="lime",width=145,height=2)
        self.BorderFrame.place(x=480,y=250)
#--------------------------------------------------------------------------------------------------------
# password feild
        
        def onEnter9(event):
                self.pass_sw.delete(0,END)
        def onExtit9(event):
                if self.pass_sw.get() == "":
                     self.pass_sw.insert(0,"password")

        self.pass_sw = Entry(self.signup_labelFrame,fg="black",font=("microsoft yahei ui light",13,"bold"),borderwidth=0,width=25,show="*")
        self.pass_sw.bind("<FocusIn>",onEnter9)
        self.pass_sw.bind("<FocusOut>",onExtit9)
        self.pass_sw.grid(row=9,column=0,sticky=W)
        self.pass_sw.insert(0,"password")
       
        self.BorderFrame = Frame(self.signup_labelFrame,width=250,height=2,bg="lime")
        self.BorderFrame.place(x=00,y=325)

#--------------------------------------------------------------------------------------------------------
# confirm password
        
        def onEnter10(event):
                self.conpass_sw.delete(0,END)
        def onExtit10(event):
                if self.conpass_sw.get() == "":
                     self.conpass_sw.insert(0,"confirm password")
        def onCursor(event):
               pass
        self.conpass_sw = Entry(self.signup_labelFrame,fg="black",font=("microsoft yahei ui light",13,"bold"),borderwidth=0,width=25,show="*",textvariable=self.password_string)
        self.conpass_sw.bind("<FocusIn>",onEnter10)
        self.conpass_sw.bind("<FocusOut>",onExtit10)
        self.conpass_sw.bind("<Enter>",onCursor)
        self.conpass_sw.grid(row=9,column=1,padx=120,sticky=W)
        self.conpass_sw.insert(0,"conform password")
       
        self.BorderFrame = Frame(self.signup_labelFrame,width=250,height=2,bg="lime")
        self.BorderFrame.place(x=380,y=325)
#--------------------------------------------------------------------------------------------------------
# Buttons
#--------------------------------------------------------------------------------------------------------
# view password button
        
        # show password function  
        def when_enter(event):
                self.pass_sw["show"] = ""
        
        def when_exit(event):
                self.pass_sw["show"]="*"
                
                
                # if self.pass_sw.get() == "":
                #      self.pass_sw["show"]=""
                #      self.pass_sw.insert(0,"password")
                        
        self.i3 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\show_password.png")
        self.i3 = self.i3.resize((15,15),Image.LANCZOS)
        self.i4 = ImageTk.PhotoImage(self.i3)
       
        self.show_password1 = Button(self.signup_labelFrame,image=self.i4,bg="white",border=0)
        self.show_password1.bind("<Button>",when_enter)
        self.show_password1.bind("<ButtonRelease>",when_exit)
        self.show_password1.place(x=230,y=300,height=25,width=25)
       
#--------------------------------------------------------------------------------------------------------
       
        def when_enter(event):
                self.conpass_sw["show"] = ""
        
        def when_exit(event):
                self.conpass_sw["show"]="*"
        
        
        self.i5 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\show_password.png")
        self.i5 = self.i3.resize((15,15),Image.LANCZOS)
        self.i6 = ImageTk.PhotoImage(self.i5)
       
        self.show_password2 = Button(self.signup_labelFrame,image=self.i6,bg="white",border=0)
        self.show_password2.bind("<Button>",when_enter)
        self.show_password2.bind("<ButtonRelease>",when_exit)
        self.show_password2.place(x=610,y=300,height=25,width=25)

#--------------------------------------------------------------------------------------------------------
# sign up Button


        self.signupbutton_sw = Button(self.signup_labelFrame,text="Sign Up",fg="white",bg="lime",borderwidth=0,width=25,font=("microsoft yahei ui light",12,"bold"),cursor="hand2",height=1,command=self.signup_function)
        self.signupbutton_sw.place(x=0,y=350)

#--------------------------------------------------------------------------------------------------------
# cancle Button

        self.canclebutton_sw = Button(self.signup_labelFrame,text="Cancle",fg="red",bg="lime",borderwidth=0,font=("microsoft yahei ui light",12,"bold"),cursor="hand2",height=1,width=25,command=self.cancle_function)
        self.canclebutton_sw.place(x=380,y=350)

#--------------------------------------------------------------------------------------------------------
        # fuction for password alpha numeric 
        self.alnum = self.pass_sw.get().isalnum()
        print(type(self.alnum))
#--------------------------------------------------------------------------------------------------------
# functions 
#--------------------------------------------------------------------------------------------------------
# function for cancle button
    def cancle_function(self):
        import loginPage 
        self.Signup_window.destroy()
        self.Login_window = Tk()        
        obj = loginPage.LogInPage(self.Login_window)


#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
# function for signup button
    def signup_function(self):
        flag = False     
        pass
        
        if self.username_string.get() == "username" or self.username_string.get() == "":
                messagebox.showerror("Error","enter username")
                flag = False

        elif self.name_string.get() == "name" or self.name_string.get() == "":
                messagebox.showerror("Error","enter name")
                flag = False
        
        elif self.email_string.get() == "email" or self.email_string.get() == "":
                messagebox.showerror("Error","enter email")
                flag = False
        
        elif self.phone_string.get() == "phone number" or self.phone_string.get() == "":
                messagebox.showerror("Error","enter phone number")
                flag = False
        
        elif self.address_string.get() == "house no / flat no , build no, lane / area name" or self.address_string.get() == "":
                messagebox.showerror("Error","enter address")
                flag = False
        
        elif self.city_string.get() == "city" or self.city_string.get() == "":
                messagebox.showerror("Error","enter city")
                flag = False
        
        elif self.state_string.get() == "state" or self.state_string.get() == "":
                messagebox.showerror("Error","enter state")
                flag = False
        
        elif len(self.pass_sw.get()) < 8:
                messagebox.showerror("Error","Password must be grater than 8 characters")
                flag = False
        
        elif self.alnum is False:
                flag  = False

        elif self.pass_sw.get() != self.password_string.get():
                messagebox.showerror("Error","Password not matched") 
                flag = False
        

        else : 
                flag = True

# inserting values into database
     
        if flag == True:
                try:
                        usernametxt = self.username_string.get()
                        nametxt = self.name_string.get()
                        emailtxt = self.email_string.get()
                        phonetxt = self.phone_string.get()
                        addresstxt = self.address_string.get()
                        citytxt = self.city_string.get()
                        statetxt = self.state_string.get()
                        pincodetxt = self.pincode_string.get()
                        passwordtxt = self.password_string.get()

                        self.conn = mysql.connector.connect(host="localhost",user="root",password="030803",db="gcsystem")
                        mycursor = self.conn.cursor()

                        mycursor.execute("insert into signup values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(usernametxt,
                                                                                                  nametxt,
                                                                                                  emailtxt,
                                                                                                  phonetxt,
                                                                                                  addresstxt,
                                                                                                  citytxt,
                                                                                                  statetxt,
                                                                                                  pincodetxt,
                                                                                                  passwordtxt))
                        
                        self.conn.commit()
                        self.conn.close()
                except:
                        messagebox.showerror("Error","mysql error")

                messagebox.showinfo("INFO","✔ sign up succsessful\nplease login again")
                import loginPage 
                self.Signup_window.destroy()
                self.Login_window = Tk()
                obj = loginPage.LogInPage(self.Login_window)


#--------------------------------------------------------------------------------------------------------
if __name__ == "__main__" :
    Signup_window=Tk()
    obj = SignUp_Class(Signup_window)
    Signup_window.mainloop()
#--------------------------------------------------------------------------------------------------------
