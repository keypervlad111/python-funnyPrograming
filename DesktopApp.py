import tkinter as tk

window=tk.Tk()
window.title(" Pythonista Planet Desktop App ")
window.geometry("600x400")
newlabel = tk.Label(text = "Visit to python desktop app")
newlabel.grid(column=0,row=0)

button1=tk.Button(window,text="Linkedin",bg="orange")
button1.grid(column=1,row=1)
button2=tk.Button(window,text="Facebook",bg="pink")
button2.grid(column=3,row=1)

window.mainloop()