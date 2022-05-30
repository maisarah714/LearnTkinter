import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(height=500, width=600)

label = tkinter.Label(text="I am Label", font=("Arial", 18, "bold"))
label.pack()


def button_clicked():
    label['text'] = input.get()



button = tkinter.Button(text="Click Me!", command=button_clicked)
button.pack()

input = tkinter.Entry()
input.pack()

window.mainloop()
