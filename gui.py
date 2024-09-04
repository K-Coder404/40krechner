"""import tkinter as tk
from main import main_rechner

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Damage Calculator")
root.geometry("500x300")  # Fenstergröße festlegen

# Erstellen der Label für Attacker
# Erstellen der Entry-Felder darunter
attackers_profile = tk.Label(root, text="Attacker's Profile:")
attackers_profile.grid(row=0, column=0)

label_A = tk.Label(root, text= "A")
label_A.grid(row=1, column=1, sticky = "ew", padx = 12)
entry_A = tk.Entry(root, width=3)
entry_A.grid(row = 2, column = 1, sticky = "ew", padx = 12)

label_Bs_Ws = tk.Label(root, text = "BS\n/WS")
label_Bs_Ws.grid(row=1, column =2, sticky="ew", padx=12)
entry_Bs_Ws = tk.Entry(root, width=3)
entry_Bs_Ws.grid(row=2, column=2, sticky="ew",padx=12)

label_S =tk.Label(root, text = "S")
label_S.grid(row = 1, column = 3, sticky="ew",padx=12)
entry_S = tk.Entry(root, width=3)
entry_S.grid(row=2, column=3, sticky="ew",padx=12)

label_AP = tk.Label(root, text = "AP")
label_AP.grid(row = 1, column = 4, sticky="ew",padx=12)
entry_AP = tk.Entry(root, width=3)
entry_AP.grid(row=2, column=4, sticky="ew",padx=12)

label_D = tk.Label(root, text = "D")
label_D.grid(row = 1, column = 5, sticky="ew",padx=12)
entry_D = tk.Entry(root, width=3)
entry_D.grid(row=2, column=5, sticky="ew",padx=12)

#Attacker's profile
def a_profile():
    attacks = int(entry_A.get())
    bs_ws = int(entry_Bs_Ws.get())
    s = int(entry_S.get())
    ap = int(entry_AP.get())
    d = int(entry_D.get())
    return attacks, bs_ws, s, ap, d

#Platzhalter
label_platzhalter =tk.Label(root, text = "              ")
label_platzhalter.grid(row=5, column=0)

label_platzhalter =tk.Label(root, text = "              ")
label_platzhalter.grid(row=9, column=0)

#Erstellen der Label für Defender
defenders_profile = tk.Label(root, text="Defender's Profile:")
defenders_profile.grid(row=6, column =0)

label_T = tk.Label(root, text= "T")
label_T.grid(row=7, column=1, sticky="ew",padx=12)
entry_T = tk.Entry(root, width=3)
entry_T.grid(row=8, column=1, sticky="ew",padx=12)

label_SV = tk.Label(root, text= "SV")
label_SV.grid(row=7, column=2, sticky="ew",padx=12)
entry_SV = tk.Entry(root, width=3)
entry_SV.grid(row=8, column=2, sticky="ew",padx=12)

label_INV = tk.Label(root, text= "INV")
label_INV.grid(row=7, column=3, sticky="ew",padx=12)
entry_INV = tk.Entry(root, width=3)
entry_INV.grid(row=8, column=3, sticky="ew",padx=12)

#Defender's profil
def d_profile():
    t = int(entry_T.get())
    sv = int(entry_SV.get())
    inv = int(entry_INV.get())
    return t, sv, inv


#Button zum Ausrechnen
rechner = tk.Button(root, text = "ATTACK", command=main_rechner)
rechner.grid(row=10, column= 0)


#Ausgabefeld des Ergebnisses
label_ergebniss = tk.Label(root, text="")





# Hauptschleife starten
root.mainloop()
"""