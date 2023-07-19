from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image , ImageTk
from time import strftime
from datetime import*
import random
import tempfile
import os
import mysql.connector
import loginPage
import signup
import pymysql


#class store 
class Store:
     
    # constructor
    def __init__(self,GC,username_lg):
        self.GC=GC
        self.GC.geometry("1355x700+0+0")
        self.GC.title("store")
        self.GC.resizable(FALSE,FALSE)
        self.photo = PhotoImage(file="C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\home-delivery.png")
        self.GC.iconphoto(FALSE,self.photo)

# variables to be used
        self.customer_name = StringVar()
        self.customer_phone = StringVar()
        self.customer_email = StringVar()
        self.username_main = username_lg
        # self.username_main = "ayushempire"
        print(self.username_main)

        # z = random.randint(1111,9999)
        # # self.bill_no = IntVar()
        # self.bill_no = z

        self.product_category = StringVar()
        self.product_subcategory = StringVar()
        self.product_name = StringVar()
        self.product_price = IntVar()
        self.product_quantity = IntVar()
        
        self.search_bill = IntVar()

        self.bill_subtotal = IntVar()
        self.bill_gst = IntVar()
        self.bill_total = IntVar()

# Heading Lable 
        head_lbl = Label(GC,text=" Shree Ganesha Grocery Store",fg="white",bg="black",font=("times new roman",25,"bold"),justify=CENTER)
        head_lbl.place(x=0,y=0,height=50,width=1400)
# log out button
        self.logout_image = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\logout.png")
        self.logout_image= self.logout_image.resize((25,25),Image.LANCZOS)
        self.logout_image = ImageTk.PhotoImage(self.logout_image)
        
        self.log_out_button = Button(head_lbl,image=self.logout_image,bg="black",border=0,command=self.exit)
        self.log_out_button.place(x=10,y=5,height=25,width=25)

# date and time on top

#funcion time to print countinuos time
        def time1():
                now = strftime("%H:%M:%S %p")
                self.date_now = datetime.now()
                self.date_now = (f"{self.date_now.day}/{self.date_now.month}/{self.date_now.year}")
                time_lbl.configure(text=f"{now}\n{self.date_now}")
                time_lbl.after(100,time1) ## countinuoes time 

        time_lbl =Label(GC,font="calibri 12 bold",fg="white",bg="black",justify=LEFT)
        time_lbl.place(x=1260,y=7,height=30,width=83)
        time1()

        # i1 = Imge.open("image\\image1.jpg")
        # i1 = i1.resize((500,130),Image.LANCZOS)
        # self.i2=ImageTk.PhotoImage(i1)
        
        # lb1 = Label(self.GC,image=self.i2)
        # lb1.place(x=0,y=0,width=500,height=130)



# product categoriets and subcategories and products      
        self.category = ["select the option","Accessory","Stationary","footwear","grocery","cosmetics"]

        # Grocery
        self.grocery = ["soap","dals","rice","wheat","oil","biscuit","sugar","salt","tea"]

        # soap
        self.soap = ["vim dishwash","santoor","pears","colgate","rin","vim powder","rin powder"]
        self.vimdishwash = 15
        self.santoor = 20
        self.pears = 50
        self.colgate = 32
        self.rin = 20
        self.vimpowder = 50
        self.rinpowder = 52

        # dal
        self.dals = ["turdal","mugdal","masurdal","watana","pavata","chana"]
        self.turdal = 56
        self.mugdal = 58
        self.masurdal = 46
        self.watana = 46
        self.pavata = 50
        self.chana = 49

        # rice
        self.rice = ["onam","basmati","ashirwad"]
        self.onam = 40
        self.ashirwad = 48
        self.basmati = 23

        # wheat
        self.wheat = ["ashirwad","annapurna"]
        self.ashirwad_wheat = 32
        self.annapurna = 28

        # oil
        self.oil = ["parachute","dabour amla","shikekai"]
        self.parachute = 30
        self.dabour_amla = 60
        self.shikekai = 30

        # biscuit
        self.biscuit = ["parale", "marie","nutrichoice","burbon"]
        self.parale = 20
        self.marie = 30
        self.nutrihoice = 10
        self.burbon = 20

        # sugar
        self.sugar = ["madhur"]
        self.madhur = 38

        # salt
        self.salt = ["tata"]
        self.tata = 20

        # tea
        self.tea = ["red label","taj","HP"]
        self.redlabel = 35
        self.taj = 45
        self.HP = 70


# image files on top side under grocery head bar
        i1 = Image.open("image\\image8.jpg")
        i1 = i1.resize((350,130),Image.LANCZOS)
        self.i2 = ImageTk.PhotoImage(i1)

        l1 = Label(self.GC,image=self.i2)
        l1.place(x=0,y=50,width=350,height=130)


        i3 = Image.open("image\\image8.jpg")
        i3 = i3.resize((350,130),Image.LANCZOS)
        self.i4 = ImageTk.PhotoImage(i3)

        l2 = Label(GC,image=self.i4)
        l2.place(x=350,y=50,width=350,height=130)
        
        
        
        i5 = Image.open("image\\image8.jpg")
        i5 = i5.resize((350,130),Image.LANCZOS)
        self.i6 = ImageTk.PhotoImage(i5)

        l3 = Label(GC,image=self.i6)
        l3.place(x=700,y=50,width=350,height=130)
        
        
        
        i7 = Image.open("image\\image8.jpg")
        i7 = i7.resize((350,130),Image.LANCZOS)
        self.i8 = ImageTk.PhotoImage(i7)

        l4 = Label(GC,image=self.i8)
        l4.place(x=1050,y=50,width=350,height=130)

#  main Frame  used for everywhere except head title and head Images
        self.f1 = Frame(GC,bg="white",borderwidth=2,relief=SUNKEN)
        self.f1.place(x=0,y=180,width=1450,height=620)

#frame for customer: 
        self.fr_costmer = LabelFrame(self.f1,text="Customer",bg="white",fg="red",font=("Tahoma",12,"bold"))
        self.fr_costmer.place(x=10,y=6,width=300,height=160)

# labels in customer frame
       
        #name
        self.name_lbl = Label(self.fr_costmer,text="Name",font="Calibri 12 bold",bg="white",fg="black")
        self.name_lbl.grid(row=0,column=0,stick=W,padx=4,pady=5)
        
        #phone
        self.phone_lbl = Label(self.fr_costmer,text="Phone No.",font="Calibri 12 bold",bg="white",fg="black")
        self.phone_lbl.grid(row=1,column=0,stick=W,padx=4,pady=5)
        

        # email
        self.email_lbl = Label(self.fr_costmer,text="Email",font="Calibri 12 bold",bg="white",fg="black")
        self.email_lbl.grid(row=2,column=0,stick=W,padx=4,pady=5)


# Entry feilds for labels
        
        self.conn = mysql.connector.connect(host="localhost",user="root",password="030803",db="gcsystem")
        mycursor = self.conn.cursor()
        
        query1 = "select * from signup where username=%s"
        value=(self.username_main,)
        
        mycursor.execute(query1,value)

        row = mycursor.fetchone()
        if  row[0] != self.username_main:
                messagebox.showerror("something went wrong")
        else:
                # name
                self.c_name = Entry(self.fr_costmer,width=20,font="claibri 11 bold",bd=2,textvariable=self.customer_name)
                self.c_name.grid(row=0,column=1,padx=2)
                # self.c_name.insert(0,name)
                self.c_name.insert(0,row[1])
                

                # phone
                self.c_phone = Entry(self.fr_costmer,width=20,font="claibri 11 bold",bd=2,textvariable=self.customer_phone)
                self.c_phone.grid(row=1,column=1,padx=2)
                self.c_phone.insert(0,row[3])

                # email
                self.c_email = Entry(self.fr_costmer,width=20,font="claibri 11 bold",bd=2,textvariable=self.customer_email)
                self.c_email.grid(row=2,column=1,padx=2)
                self.c_email.insert(0,row[2])


# frame  for product
        self.fr_product = LabelFrame(self.f1,bg="white",text="Product",font="Tahoma 12 bold",fg ="red")
        self.fr_product.place(x=320,y=6,width=550,height=160)

# lables on Product
        
        #category
        self.catagory_lbl = Label(self.fr_product,text="Category",font="calibri 12 bold",bg="white",fg="black")
        self.catagory_lbl.grid(row=0,column=0,padx=4,pady=5,stick=W)
        
        #subcategory
        self.subcatagory_lbl = Label(self.fr_product,text="Sub Category",font="calibri 12 bold",bg="white",fg="black")
        self.subcatagory_lbl.grid(row=1,column=0,padx=4,pady=5,stick=W)
        
        # product name
        self.productname_lbl = Label(self.fr_product,text="Product Name",font="calibri 12 bold",bg="white",fg="black")
        self.productname_lbl.grid(row=2,column=0,padx=4,pady=5,stick=W)

        # price
        self.price_lbl = Label(self.fr_product,text="Price",font="calibri 12 bold",bg="white",fg="black")
        self.price_lbl.grid(row=0,column=2,padx=5,pady=4,stick=W)
        
        # quantity
        self.quantity_lbl = Label(self.fr_product,text="Quantity",font="calibri 12 bold",bg="white",fg="black")
        self.quantity_lbl.grid(row=1,column=2,padx=5,pady=4,stick=W)


# combo box for lables
        
        # category
        self.combo_categary = ttk.Combobox(self.fr_product,font="calibri 11 bold",state="readonly",value=self.category,textvariable=self.product_category)
        self.combo_categary.current(0)
        self.combo_categary.grid(row=0,column=1,padx=3,pady=4,sticky=W) 
        self.combo_categary.bind("<<ComboboxSelected>>",self.Categories)
        
        #subcategory
        self.combo_subcategary = ttk.Combobox(self.fr_product,font="calibri 11 bold",state="readonly",textvariable=self.product_subcategory)
        self.combo_subcategary.grid(row=1,column=1,padx=3,pady=4,sticky=W)
        self.combo_subcategary.bind("<<ComboboxSelected>>",self.product_set) 
        
        #product
        self.combo_productcategary = ttk.Combobox(self.fr_product,font="calibri 11 bold",state="readonly",textvariable=self.product_name)
        self.combo_productcategary.grid(row=2,column=1,padx=3,pady=4,sticky=W) 
        self.combo_productcategary.bind("<<ComboboxSelected>>",self.price_qty_set)
        
        # price
        self.combo_price = ttk.Combobox(self.fr_product,font="calibri 11 bold",textvariable=self.product_price)
        self.combo_price.grid(row=0,column=3,padx=3,pady=4,sticky=W) 
        
        # quantity
        self.entry_quantity = Entry(self.fr_product,font="calibri 11 bold",width=22,bd=2,justify=CENTER,textvariable=self.product_quantity)
        self.entry_quantity.grid(row=1,column=3,padx=3,pady=4,sticky=W) 

        # Button add to cart
        self.b_ato_cart = Button(self.fr_product,text="Add to Cart",bg="orange",fg="white",font="Tahoma 10 bold",width=28,cursor="hand2",command=self.add_to_cart)
        self.b_ato_cart.grid(row=2,column=2,columnspan=3)


# search bill label and button
        
        # search bill lable
        self.serach_lbl = Label(self.f1,text="Bill Number",font="Calibri 12 bold",fg="white",bg="black")
        self.serach_lbl.place(x=890,y=15,width=90)

        # search entry
        self.entry_search = Entry(self.f1,bg="white",fg="black",font="calibri 12 bold",justify=LEFT,borderwidth=2,relief=SUNKEN,textvariable=self.search_bill)
        self.entry_search.place(x=1000,y=15,width=160)

        # search button
        self.b_search = Button(self.f1,text="Search",font="tahoma 12 bold",fg="white",bg="darkorange",cursor="hand2",command=self.search_bill_function)
        self.b_search.place(x=1170,y=15,width=90,height=24)


# Frame for bill

        self.fr_bill = LabelFrame(self.f1,text="Bill",bg="white",font="tahoma 12 bold",fg="red")
        self.fr_bill.place(x=890,y=50,width=450,height=330)
        
# Tetxt feild for bill and scrollbar

        self.scr_bill =Scrollbar(self.fr_bill,orient=VERTICAL)
        self.bill_text1 = Text(self.fr_bill,yscrollcommand=self.scr_bill.set,bg="white",fg="blue",font=("times new roman",11,"bold"),state="normal")
        self.scr_bill.pack(side=RIGHT,fill=Y)
        self.scr_bill.config(command=self.bill_text1.yview)
        self.bill_text1.pack(fill=BOTH,expand=1)


# Frame for bill counter

        self.fr_billcounter = LabelFrame(self.f1,text="Bill Counter",fg="red",font="Tahoma 12 bold",bg="white")
        self.fr_billcounter.place(x=10,y=380,width=1330,height=120,)

# labels for bill counter
        
        # subtotal
        self.subtoatal_lbl = Label(self.fr_billcounter,text="Sub Total",fg="black",bg="white",font="calibri 12 bold")
        self.subtoatal_lbl.grid(row=0,column=0,padx=5,pady=3,stick=W)
        
        # GST
        self.gst_lbl = Label(self.fr_billcounter,text="GST",fg="black",bg="white",font="calibri 12 bold")
        self.gst_lbl.grid(row=1,column=0,padx=5,pady=3,stick=W)
        
        # Total
        self.toatal_lbl = Label(self.fr_billcounter,text="Total",fg="black",bg="white",font="calibri 12 bold")
        self.toatal_lbl.grid(row=2,column=0,padx=5,pady=3,stick=W)

# Entry box for lables of bill counter

        # subtotal
        self.entry_subtotal = Entry(self.fr_billcounter,bg="white",fg="black",font="calibri 11 bold",width=26,bd=2,textvariable=self.bill_subtotal)
        self.entry_subtotal.grid(row=0,column=2,padx=2,pady=3)
        
        # gst
        self.entry_gst = Entry(self.fr_billcounter,bg="white",fg="black",font="calibri 11 bold",width=26,bd=2,textvariable=self.bill_gst)
        self.entry_gst.grid(row=1,column=2,padx=2,pady=3)
        
        # total
        self.entry_total = Entry(self.fr_billcounter,bg="white",fg="black",font="calibri 11 bold",width=26,bd=2,textvariable=self.bill_total)
        self.entry_total.grid(row=2,column=2,padx=2,pady=3)


#  frame for Buttons

        self.fr_button = Frame(self.fr_billcounter,bg="white")
        self.fr_button.place(x=400,y=20,width=850,height=55)

        # generate bill
        self.b_generatebill = Button(self.fr_button,text="Generate Bill",fg="white",bg="darkorange",font="claibri 13 bold",bd=2,width=15,height=2,cursor="hand2",command=self.generate_bill)
        self.b_generatebill.grid(row=0,column=0,padx=2,pady=2)
        
        # save bill
        self.b_savebill = Button(self.fr_button,text="Save Bill",fg="white",bg="darkorange",font="claibri 13 bold",bd=2,width=15,height=2,cursor="hand2",command=self.save_bill)
        self.b_savebill.grid(row=0,column=1,padx=2,pady=2)
        
        # print
        self.b_printbill = Button(self.fr_button,text="Print Bill",fg="white",bg="darkorange",font="claibri 13 bold",bd=2,width=15,height=2,cursor="hand2",command=self.print_bill)
        self.b_printbill.grid(row=0,column=2,padx=2,pady=2)
        
        # clear
        self.b_clearbill = Button(self.fr_button,text="Clear",fg="white",bg="darkorange",font="claibri 13 bold",bd=2,width=15,height=2,cursor="hand2",command=self.clear_function)
        self.b_clearbill.grid(row=0,column=3,padx=2,pady=2)
        
        # exit
        self.b_pay = Button(self.fr_button,text="Pay",fg="white",bg="darkorange",font="claibri 13 bold",bd=2,width=15,height=2,cursor="hand2",command=self.pay)
        self.b_pay.grid(row=0,column=4,padx=2,pady=2)


# image on frame used in middle of frame

# scrollbar for images to be select

        self.scrollframe = LabelFrame(self.f1,bg="white")
        self.scrollframe.place(x=10,y=170,width=855,height=200)
        
        
        self.scr_product_image =Scrollbar(self.scrollframe,orient=VERTICAL)
        self.product_frame = Text(self.scrollframe,yscrollcommand=self.scr_product_image.set,bg="white",state="normal",border=0)
        self.scr_product_image.pack(side=RIGHT,fill=Y)
        self.scr_product_image.config(command=self.product_frame.yview)
        self.product_frame.pack(fill=BOTH,expand=1)

# product images and their buttons on middle of frame

        # self.madhur_img1 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\madhur_sugar.jpg")
        # self.madhur_img1.resize((100,100),Image.LANCZOS)
        # self.madhur_img2 = ImageTk.PhotoImage(self.madhur_img1)

        # self.madhur_lbl = Label(self.product_frame,image=self.madhur_img2)
        # self.madhur_lbl.grid(row=0,column=0)

        # self.bill_text1 = Text(self.fr_bill,yscrollcommand=self.scr_bill.set,bg="white",fg="blue",font=("times new roman",11,"bold"),state="normal")
        # self.scr_bill.pack(side=RIGHT,fill=Y)
        # self.scr_bill.config(command=self.bill_text1.yview)
        # self.bill_text1.pack(fill=BOTH,expand=1)


        # product image frame 
        i9 = Image.open("image\\image14.jpg")
        i9 = i9.resize((400,200),Image.LANCZOS)
        self.i10 = ImageTk.PhotoImage(i9)

        l5 = Label(self.f1,image=self.i10)
        l5.place(x=10,y=170,width=400,height=200)
        


        i11 = Image.open("image\\image10.jpg")
        i11 = i11.resize((400,200),Image.LANCZOS)
        self.i12 = ImageTk.PhotoImage(i11)

        l5 = Label(self.f1,image=self.i12)
        l5.place(x=420,y=170,width=400,height=200)

# creaing function for product tables
        

# creating table for customers product list

        datenow  = datetime.now()
        time_ = strftime("%H%M%S")
        datenow = f"{datenow.day}{datenow.month}{datenow.year}"
        # connecting with mysql server and entring data
        conn = mysql.connector.connect(host="localhost",user="root",password="030803",db="gcsystem")

        # crating table        
        mycursor = conn.cursor()
        query= f"create table {self.username_main}_{datenow}_{time_}(username varchar(100),name varchar(300),category varchar(200),subcategory varchar(200),product varchar(300),quantity varchar(300),price varchar(300),total varchar(300),address varchar(500),city varchar(100),state varchar(100),pincode int,phone varchar(300))"
        mycursor.execute(query)

        # retriving data using username

        query1 = "select * from signup where username =%s"
        value1 = (self.username_main,)
        mycursor.execute(query1,value1)

        row = mycursor.fetchone()
        
        self.tabel_name = f"{self.username_main}_{datenow}_{time_}"
        
        # inseting data into product table 
        query2 = f"insert into {self.tabel_name}(username,name,address,city,state,pincode,phone) values(%s,%s,%s,%s,%s,%s,%s)"
        value2 = (row[0],row[1],row[4],row[5],row[6],row[7],row[3])

        mycursor.execute(query2,value2)
        
        conn.commit()
        conn.close()



# function calling and lists for ccalculations
        self.total_list = []
        self.gst_list = []
        self.bill_()
        
        

# working of Product Frame

# add to card function used in add to cart button
    def add_to_cart(self): # claculate GST in aproprer manner

                self.gst = 2
                #calculate product price and quantity 
                self.a = float(self.product_price.get())
                # calculating prduct and quantity and passing it into a list
                self.b = float(self.product_quantity.get() * self.a)
                # passing into a list
                self.total_list.append(self.b)

                # calculating gst like price and quantity
                self.c = float((sum(self.total_list)) * (self.gst/100))
                self.gst_list.append(self.c)
                

                if self.product_name.get() =="":
                        messagebox.showerror("Error","Please Select Product..")
                
                else:
                        # addition of list items and align to subtotal
                        self.bill_subtotal.set(float(sum(self.total_list)))
                        # addition of list items and align to gst
                        self.bill_gst.set(sum(self.gst_list))

                        self.bill_total.set(float(self.bill_subtotal.get()+ self.bill_gst.get()))
                        
                        # adding the product details to text feild// bill
                        self.bill_text1.insert(END,f"{self.product_name.get()}\t\t               {self.product_quantity.get()}\t\t                     {self.product_price.get()}\n")

# uploading product list data to table 
                        
                        conn = mysql.connector.connect(host="localhost",user="root",password="030803",db="gcsystem")
        
                        mycursor = conn.cursor()
                        
                        query3 = f"insert into {self.tabel_name}(category,subcategory,product,quantity,price) values(%s,%s,%s,%s,%s)"
                        value3 = ((self.product_category.get()),(self.product_subcategory.get()),(self.product_name.get()),(self.product_quantity.get()),self.product_price.get())

                        mycursor.execute(query3,value3)

                        conn.commit()
                        conn.close()

# generate bill function
    def generate_bill(self):
                        
                        if self.product_name.get() =="":
                                messagebox.showerror("Error","Please select Product")
                        else:   
                                self.bill_text1.delete(4.0,7.0)
                                self.bill_text1.insert(4.0,f"Customer Name: {self.c_name.get()}\n")
                                self.bill_text1.insert(5.0,f"Customer Phone: {self.c_phone.get()}\n")
                                self.bill_text1.insert(6.0,f"Customer Email: {self.c_email.get()}gmail.com\n")                
                                self.bill_text1.insert(END,"===============================================\n")
                                self.bill_text1.insert(END,f"Subtotal:\t\t\t\t\t {self.bill_subtotal.get()}\n")
                                self.bill_text1.insert(END,f"GST:\t\t\t\t\t   {self.bill_gst.get()}\n")
                                self.bill_text1.insert(END,f"Total:\t\t\t\t\t  {self.bill_total.get()}\n")
        
# uploading total to table
                                conn = mysql.connector.connect(host="localhost",user="root",password="030803",db="gcsystem")
        
                                mycursor = conn.cursor()
                                
                                query3 = f"insert into {self.tabel_name}(total) values(%s)"
                                value3 = (self.bill_total.get(),)

                                mycursor.execute(query3,value3)

                                conn.commit()
                                conn.close()

# saving the bill in txt form
    def save_bill(self):
        
                self.ask = messagebox.askyesno("Grocery Store","Want to save bill ?")
        
                if self.ask == 1:
                        with open(f"C:\\Users\\AYUSH\\Desktop\\Grocery Store\\Bills\\{self.bill_no}.txt","w") as f:
                                f.write(str(self.bill_text1.get(1.0,END)))

                        messagebox.showinfo("Grocery Store","Bill saved...")        
# print bill function 
    def print_bill(self):
                
                self.bill_text_print = str(self.bill_text1.get(1.0,END))
                
                # creating a temp file
                temp_file = tempfile.mktemp(".txt")
                # writing the bill data into temp file
                open(temp_file,"w").write(self.bill_text_print)
                # printing the temp file
                os.startfile(temp_file,"print")

# search bill by bill nuber

    def search_bill_function(self) : 

                filename = self.search_bill.get()

                if os.path.isfile(f"C:\\Users\\AYUSH\\Desktop\\Grocery Store\\Bills\\{filename}.txt"):

                        with open(f"C:\\Users\\AYUSH\\Desktop\\Grocery Store\\Bills\\{filename}.txt") as f:
                                str = f.read()
                                self.bill_text1.delete(1.0,END)
                                self.bill_text1.insert(END,str)

                        # self.GC.ttk.messagebox.showinfo("","found")
                else :
                        messagebox.showinfo("","not found")

#     def serach_bill_function(self) :
#                 found = False

#                 for i in os.listdir("Grocery Store/Bills/") :
#                         if i.split('.')[0] == self.search_bill.get():
#                                 f1=open(f"Grocery Store\\Bills\\{i}","r")
#                                 self.bill_text1.delete(1.0,END)
#                                 for d in f1:
#                                         self.bill_text1.insert(END,d)
#                                 f1.close()
#                                 found = True
#                 if found == False : 
#                         messagebox.showerror("Error","Bill Not Found...")  
                 

# function for permanant details on bill
    def bill_(self):

                z = random.randint(1111,9999)
                # self.bill_no = IntVar()
                self.bill_no = z
                self.bill_text1.delete(1.0,END)
                self.bill_text1.insert(END,"\t\t          Final Bill\n")
                self.bill_text1.insert(END,"\t\t    PA Super Market\n")
                self.bill_text1.insert(END,f"Bill Number- {self.bill_no}\t\t\t\t\tDate:-{self.date_now}\n")
                self.bill_text1.insert(END,f"Customer Name: {self.c_name.get()} \n")
                self.bill_text1.insert(END,f"Customer Phone: {self.c_phone.get()}\n")
                self.bill_text1.insert(END,f"Customer Email: {self.c_email.get()}@gmail.com\n")
                self.bill_text1.insert(END,"===============================================\n")
                self.bill_text1.insert(END,"Products\t\t          Quantity\t\t                     Price \n")
                self.bill_text1.insert(END,"===============================================\n")


# fucnction for selected category
    def Categories(self,event=""):
                if self.combo_categary.get() == "grocery":
                        self.combo_subcategary.config(value=self.grocery)
                        self.combo_subcategary.current(0)

# function for selected subcategory
    def product_set(self,event=""):
                # soap
                if self.combo_subcategary.get() == "soap":
                        self.combo_productcategary.config(value=self.soap)
                        self.combo_productcategary.current(0)
                # dals
                elif self.combo_subcategary.get() == "dals":
                        self.combo_productcategary.config(value=self.dals)
                        self.combo_productcategary.current(0)
                # rice
                elif self.combo_subcategary.get() == "rice":
                        self.combo_productcategary.config(value=self.rice)
                        self.combo_productcategary.current(0)
                # wheat
                elif self.combo_subcategary.get() == "wheat":
                        self.combo_productcategary.config(value=self.wheat)
                        self.combo_productcategary.current(0)
                # biscuits
                elif self.combo_subcategary.get() == "biscuit":
                        self.combo_productcategary.config(value=self.biscuit)
                        self.combo_productcategary.current(0)
                # oil
                elif self.combo_subcategary.get() == "oil":
                        self.combo_productcategary.config(value=self.oil)
                        self.combo_productcategary.current(0)
                # sugar
                elif self.combo_subcategary.get() == "sugar":
                        self.combo_productcategary.config(value=self.sugar)
                        self.combo_productcategary.current(0)
                # salt
                elif self.combo_subcategary.get() == "salt":
                        self.combo_productcategary.config(value=self.salt)
                        self.combo_productcategary.current(0)
                # tea
                elif self.combo_subcategary.get() == "tea":
                        self.combo_productcategary.config(value=self.tea)
                        self.combo_productcategary.current(0)
    
# function to set price of selected product
    
    def price_qty_set(self,event=""):
    
                if self.combo_productcategary.get() == "rin":
                        self.combo_price.config(value=self.rin)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
    
                elif self.combo_productcategary.get() == "vim dishwash":
                        self.combo_price.config(value=self.vimdishwash)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "santoor":
                        self.combo_price.config(value=self.santoor)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "pears":
                        self.combo_price.config(value=self.pears)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "colgate":
                        self.combo_price.config(value=self.colgate)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "vim powder":
                        self.combo_price.config(value=self.vimpowder)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "rin powder":
                        self.combo_price.config(value=self.rinpowder)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "turdal":
                        self.combo_price.config(value=self.turdal)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "mugdal":
                        self.combo_price.config(value=self.mugdal)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "masurdal":
                        self.combo_price.config(value=self.masurdal)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "watana":
                        self.combo_price.config(value=self.watana)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "pavata":
                        self.combo_price.config(value=self.pavata)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "chana":
                        self.combo_price.config(value=self.chana)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "onam":
                        self.combo_price.config(value=self.onam)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "ashirwad":
                        self.combo_price.config(value=self.ashirwad)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "basmati":
                        self.combo_price.config(value=self.basmati)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "ashirwad":
                        self.combo_price.config(value=self.ashirwad_wheat)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "annapurna":
                        self.combo_price.config(value=self.annapurna)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "parachute":
                        self.combo_price.config(value=self.parachute)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "dabour amla":
                        self.combo_price.config(value=self.dabour_amla)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "shikekai":
                        self.combo_price.config(value=self.shikekai)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "parale":
                        self.combo_price.config(value=self.parale)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "marie":
                        self.combo_price.config(value=self.marie)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "burbon":
                        self.combo_price.config(value=self.burbon)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "nutrichoice":
                        self.combo_price.config(value=self.nutrihoice)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "madhur":
                        self.combo_price.config(value=self.madhur)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "tata":
                        self.combo_price.config(value=self.tata)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "red label":
                        self.combo_price.config(value=self.redlabel)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "HP":
                        self.combo_price.config(value=self.HP)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)
                
                elif self.combo_productcategary.get() == "taj":
                        self.combo_price.config(value=self.taj)
                        self.combo_price.current(0)
                        self.product_quantity.set(1)

# function for clear button
    def clear_function(self):
        self.bill_text1.delete(1.0,END)
        # self.customer_name.set("")
        # self.customer_phone.set("")
        # self.customer_email.set("")


        self.product_category.set("")
        self.product_subcategory.set("")
        self.product_name.set("")
        self.product_quantity.set(0)
        self.combo_price.config(value=0)
        self.product_price.set(0)
        
        self.bill_no=0

        self.search_bill.set(0)

        self.bill_subtotal.set(0)
        self.bill_gst.set(0)
        self.bill_total.set(0)

        self.total_list=[0]
         
        self.bill_()


# function exit
    
    def pay(self):
        # import loginPage
        
        import paypage 

        self.new_window = Toplevel(self.GC)
        self.payment = paypage.PAYMENT(self.new_window)
        
    def exit(self):
        import loginPage

        self.GC.destroy()
        self.Login_window = Tk()
        obj = loginPage.LogInPage(self.Login_window)
        
        # self.GC.destroy()
        # self.payment_window=Tk()
        # obj = paypage.PAYMENT(self.payment_window) 
 
if __name__ == "__main__":
    GC=Tk()
    obj=Store(GC)
    GC.mainloop()

