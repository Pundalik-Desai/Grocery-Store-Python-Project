from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

class PAYMENT:
            
    def __init__(self,payment_window):
                    # usename = username_main
                    
        self.payment_window = payment_window
        self.payment_window.title('PAY')
        self.payment_window.geometry('800x400+300+100')
        self.payment_window.configure(background='white')
                    #self.payment_window.iconbitmap('favicon.ico')
# image frame 
        self.image_label_main = LabelFrame(self.payment_window,border=0,bg="white")
        self.image_label_main.place(x=0,y=0,height=402,width=402)
# image 
        self.i1 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\payment.png")
        self.i1.resize((400,400),Image.LANCZOS)
        self.i2 = ImageTk.PhotoImage(self.i1)
# image Label
        self.imageLabel_l2 = Label(self.image_label_main,image=self.i2)
        self.imageLabel_l2.place(x=2,y=2,width=400,height=400)

# main heading 
        self.text_label = Label(self.payment_window,text='PAYMENT',fg='darkseagreen',bg='white')
        self.text_label.place(x=520,y=10)
        self.text_label.config(font=('Tahoma',24,"bold"))

# account number label
        self.AccountNO_label = Label(self.payment_window,text='Account NO',fg='darkseagreen',bg='white')
        self.AccountNO_label.place(x=550,y=100)
        self.AccountNO_label.config(font=('Tahoma',12,"bold"))

# account number 
        self.AccountNO_input = Entry(self.payment_window,width=50,border=0)
        self.AccountNO_input.place(x=450,y=150)

        self.borderFrame = Frame(self.payment_window,bg="darkseagreen",height=2,borderwidth=3,width=300)
        self.borderFrame.place(x=450,y=170)

# account frame
        self.Amount_label = Label(self.payment_window,text='Enter amount',fg='darkseagreen',bg='white')
        self.Amount_label.place(x=550,y=200)
        self.Amount_label.config(font=('Tahoma',12,"bold"))

# amount input
        self.Amount_input = Entry(self.payment_window,width=50,border=0)
        self.Amount_input.place(x=450,y=250)
        borderFrame = Frame(self.payment_window,bg="darkseagreen",height=2,borderwidth=3,width=300)
        borderFrame.place(x=450,y=270)

# buttom
        Go_btn = Button(self.payment_window,text=' paytm karo',bg='darkseagreen',fg='black',width=20,height=2,command=self.handle_login)
        Go_btn.place(x=520,y=300)
        Go_btn.config(font=('Tahoma',10,"bold"))


# functions            
    def handle_login(self):
                account_no = self.AccountNO_input.get()
                amount= self.Amount_input.get()

                if account_no == 'prasad1234' and amount == '1234':
                    messagebox.showinfo('Yayyy','payment Successful')
                else:   
                    messagebox.showerror('Error','payment Failed')



if __name__ == "__main__":

    payment_window = Tk()
    obj  = PAYMENT(payment_window)
    payment_window.mainloop()
