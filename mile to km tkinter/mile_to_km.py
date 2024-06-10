import tkinter

#Window Size
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=100, pady=100)

def replace():
    miles = float(input.get())  # Convert the input to float
    km = round(miles * 1.609)
    sentence.config(text=f"{miles} Miles is equal to {km} Km")

#Input
input = tkinter.Entry()
input.grid(row=0, column=1)

sentence = tkinter.Label(text="Miles is equal to 0 Km")
sentence.grid(row=1, column=1)


calculate = tkinter.Button(text="Calculate", command=replace)
calculate.grid(row=2,column=1)


window.mainloop()

