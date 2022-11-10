from tkinter import *

root = Tk()

root.title("ALLOCATION")
root.geometry("400x500")

label1 = Label(root,text="Hospital is City Care")
label1.place(relx=0.2,rely=0.2,anchor=CENTER)

input1 = Entry(root)
input1.place(relx=0.8,rely=0.2,anchor=CENTER)

label_show_1 = Label(root,text="")
label_show_1.place(relx=0.2,rely=0.3,anchor=CENTER)

label2 = Label(root,text="IT company is Dotcom Services")
label2.place(relx=0.2,rely=0.4,anchor=CENTER)

input2 = Entry(root)
input2.place(relx=0.8,rely=0.4,anchor=CENTER)

label_show_2 = Label(root,text="")
label_show_2.place(relx=0.2,rely=0.5,anchor=CENTER)

label3 = Label(root,text="Chemical Engineering company is Air Liquide")
label3.place(relx=0.2,rely=0.6,anchor=CENTER)

input3 = Entry(root)
input3.place(relx=0.8,rely=0.6,anchor=CENTER)

label_show_3 = Label(root,text="")
label_show_3.place(relx=0.2,rely=0.7,anchor=CENTER)



def show():
    t1 = input1.get()
    t2 = input2.get()
    t3 = input3.get()
    label_show_1["text"]=t1 + " is allocated to City Center"
    label_show_2["text"]=t2 + " is allocated to Dotcom Services"
    label_show_3["text"]=t3 + " is allocated to Air Liquide"

btn = Button(root,text="Assign",command=show)
btn.place(relx=0.2,rely=0.8,anchor=CENTER)


root.mainloop()

