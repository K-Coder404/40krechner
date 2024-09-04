import tkinter as tk

root = tk.Tk()
root.title("Mehrere Checkboxen in Tkinter")

# Checkbox 1 - Links oben
chk1_var = tk.IntVar()
chk1 = tk.Checkbutton(root, text="Option 1", variable=chk1_var)
chk1.grid(row=0, column=0, sticky='w', padx=10, pady=10)  # Links ausgerichtet

# Checkbox 2 - Rechts oben
chk2_var = tk.IntVar()
chk2 = tk.Checkbutton(root, text="Option 2", variable=chk2_var)
chk2.grid(row=0, column=1, sticky='e', padx=10, pady=10)  # Rechts ausgerichtet

# Checkbox 3 - Links unten
chk3_var = tk.IntVar()
chk3 = tk.Checkbutton(root, text="Option 3", variable=chk3_var)
chk3.grid(row=1, column=0, sticky='w', padx=10, pady=10)  # Links ausgerichtet

# Checkbox 4 - Rechts unten
chk4_var = tk.IntVar()
chk4 = tk.Checkbutton(root, text="Option 4", variable=chk4_var)
chk4.grid(row=1, column=1, sticky='e', padx=10, pady=10)  # Rechts ausgerichtet

root.mainloop()
