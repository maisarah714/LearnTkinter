import tkinter

window = tkinter.Tk()
# window.minsize(width=500, height=600)
window.config(padx=20, pady=20)
window.title("Mile to KM Converter")

input = tkinter.Entry()
input.grid(row=0, column=1)


def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    km_label.config(text=km)


button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

text = tkinter.Label(text="Miles")
text.grid(row=0, column=2)

km_label = tkinter.Label(text="0")
km_label.grid(row=1, column=1)

text2 = tkinter.Label(text="KM")
text2.grid(row=1, column=2)

equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(row=1, column=0)


window.mainloop()
