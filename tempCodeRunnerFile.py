from tkinter import *
from PIL import Image,ImageTk
class  Scroll:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x600+100+200")
        self.root.configure(bg="white")

        frame = LabelFrame(self.root,bg="white")
        frame.place(x=0,y=1,width=100,height=250)

        self.scr_bill =Scrollbar(frame,orient=VERTICAL)
        self.bill_text1 = Text(frame,yscrollcommand=self.scr_bill.set,bg="white",fg="blue",font=("times new roman",11,"bold"),state="normal")
        self.scr_bill.pack(side=RIGHT,fill=Y)
        self.scr_bill.config(command=self.bill_text1.yview)
        self.bill_text1.pack(fill=BOTH,expand=1)


        self.madhur_img1 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\madhur_sugar.jpg")
        self.madhur_img1.resize((100,100),Image.LANCZOS)
        self.madhur_img2 = ImageTk.PhotoImage(self.madhur_img1)

        self.madhur_lbl = Label(self.bill_text1,image=self.madhur_img2)
        self.madhur_lbl.place(x=0,y=0)
        
        self.madhur_img3 = Image.open("C:\\Users\\AYUSH\\Desktop\\Grocery Store\\image\\madhur_sugar.jpg")
        self.madhur_img3.resize((100,100),Image.LANCZOS)
        self.madhur_img4 = ImageTk.PhotoImage(self.madhur_img1)

        self.madhur_lbl1 = Label(self.bill_text1,image=self.madhur_img4)
        self.madhur_lbl1.place(x=0,y=100)

if __name__ == "__main__":
    root = Tk()
    obj = Scroll(root)
    root.mainloop()