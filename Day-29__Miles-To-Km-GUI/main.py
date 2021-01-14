import tkinter

window = tkinter.Tk()
window.title("Miles to Km")
window.config(padx=20,pady=20)

km = 0

miles_label = tkinter.Label(text="Miles",font=("Arial",14,"bold"))
miles_label.grid(column=2,row=0)

input = tkinter.Entry(width="10")
input.grid(column=1,row=0)

is_equal_to_label = tkinter.Label(text="is equal to",font=("Arial",14,"bold"))
is_equal_to_label.grid(column=0,row=1)

km = tkinter.Label(text=0,font=("Arial",14,"bold"))
km.grid(column=1,row=1)

km_label = tkinter.Label(text="Km",font=("Arial",14,"bold"))
km_label.grid(column=2,row=1)

def calculate():
    km["text"] = int(int(input.get())/0.62137)

button = tkinter.Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)


window.mainloop()