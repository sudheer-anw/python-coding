from tkinter import *
window = Tk()
window.title("GUI")
window.minsize(width=500,height=500)
#label
my_label =Label(text = "i'am a Lable",font=("arial",24,"italic"))
my_label.grid(column=0,row=0)

my_label["text"] ="new_text"
my_label.config(text="new_text")

#button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print(new_text)

button = Button(text="click me",command=button_clicked) 
button.grid(column=1,row=1)

#entry
input = Entry(width=30)
input.grid(column=2,row=2)






























window.mainloop()




