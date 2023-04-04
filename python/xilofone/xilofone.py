import tkinter as tk
from tkinter import ttk
from playsound import playsound



root = tk.Tk()
root.geometry('920x1080')
root.resizable(True, True)
root.title('Batidas nice')


vai_tombar = ttk.Button(
    root,
    text='vai tombar',
    command=lambda: playsound("C:\\Users\\ADM\\Desktop\\patas\\progamação\\python\\vai_tomar.mp3", block=False),

    
)
vai_tombar.pack(
    padx=5,
    pady=5,
    expand=False,
    side=tk.LEFT,
    
)

do = ttk.Button(
    root,
    text='dó',
)
do.pack(
    ipadx=1,
    ipady=500,
    padx=5,
    pady=5,
    expand=False, 
    side=tk.LEFT,  
)

re = ttk.Button(
    root,
    text='re',
)
re.pack(
    ipadx=1,
    ipady=400,
    padx=5,
    pady=5,
    expand=False, 
    side=tk.LEFT,  
)

mi = ttk.Button(
    root,
    text='mi',
)
mi.pack(
    ipadx=1,
    ipady=300,
    padx=5,
    pady=5,
    expand=False, 
    side=tk.LEFT,  
)

fa = ttk.Button(
    root,
    text='fa',
)
fa.pack(
    ipadx=1,
    ipady=200,
    padx=5,
    pady=5,
    expand=False,  
    side=tk.LEFT,
)

sol = ttk.Button(
    root,
    text='sol',
)
sol.pack(
    ipadx=1,
    ipady=100,
    padx=5,
    pady=5,
    expand=False,
    side=tk.LEFT,   
)

la = ttk.Button(
    root,
    text='la',
)
la.pack(
    ipadx=1,
    ipady=50,
    padx=5,
    pady=5,
    expand=False,
    side=tk.LEFT,   
)

exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
exit_button.pack(
    padx=5,
    pady=5,
    expand=False,
    side=tk.LEFT,
)

paro = ttk.Button(
    root,
    text='PAAAARRAAAA',
    command=lambda: playsound(None)
)
paro.pack(
    padx=5,
    pady=5,
    expand=False,
    side=tk.LEFT,
)

cara_de_pedra = ttk.Button(
    root,
    text='PAAAARRAAAA',
    command=lambda: playsound("C:\\Users\\ADM\\Desktop\\patas\\sons\\CARA DE PEDRA -.mp3", block=False),
)
cara_de_pedra.pack(
    padx=5,
    pady=5,
    expand=False,
)


root.mainloop()