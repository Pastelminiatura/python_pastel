import tkinter as tk
from tkinter import ttk
from playsound import playsound


# root window
root = tk.Tk()
root.geometry('700x300')
root.resizable(True, True)
root.title('Batidas nice')

test = tk.Label(
    root, 
    text="red", 
    bg="red", 
    fg="white")
test.pack(
    padx=5, 
    pady=15, 
    side=tk.LEFT)

exit_button = ttk.Button(
    root,
    text='vai tombar',
    command=lambda: playsound("batida.mp3")
    
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

exit_button2 = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button2.pack(
    ipadx=5,
    ipady=5,
    expand=True
)



root.mainloop()