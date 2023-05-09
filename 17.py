from tkinter import*
tk=Tk()
tk.geometry("600x600")
def btn1_click():
    lbl2=Label(text="привіт "+ent.get()+"!")
    lbl2.place(x=150,y=150)
def btn2_click():
    print("прощавай ", ent.get(),"!",sep="")
btn1=Button(text="привітання",command=btn1_click)
btn1.place(x=75,y=75,width=100,height=50)
btn2=Button(text="прощання",command=btn2_click)
btn2.place(x=225,y=75,width=100,height=50)
ent=Entry(bd=1)
ent.place(x=225,y=25,width=100,height=30)
lbl1=Label(text="ваше імя:") 
lbl1.place(x=75,y=25,width=100,height=30)

lbl1.pack()
btn1.pack()
ent.pack()
btn2.pack()