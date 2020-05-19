from tkinter import *

window = Tk()
window.title("Test Program")
window.geometry('300x300')

lblTxt = StringVar()
lblTxt.set("Hello, World!")
lbl = Label(window, textvariable=lblTxt)
lbl.grid(column=0, row=0, padx=5, pady=5)


txtBox = Entry(window)
txtBox.grid(column=0, row=1, padx=5, pady=5)

def ButtonTextSwap():
	lblTxt.set(txtBox.get())
	
def CalculateNumber():
	texttest = txtBox.get()
	if (texttest.isnumeric()) == True:
		Num = int(txtBox.get()) * 3
		lblTxt.set(Num)
	else:
		lblTxt.set("Invalid Input!")

txtBtn = Button(window, text="Textbox -> Label", command = ButtonTextSwap)
txtBtn.grid(column=0, row=3, padx=5, pady=5)

txtBtn2 = Button(window, text="Multiply Number", command = CalculateNumber)
txtBtn2.grid(column=0, row=4, padx=5, pady=5)

window.mainloop()