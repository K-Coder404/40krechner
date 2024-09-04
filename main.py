#main.py
import probabilities as p
import tkinter as tk

def main_rechner():
    attacks, bs_ws, s, ap, d = a_profile()
    t, sv, inv, fnp = d_profile()
    sustained_hits_nr = sustain_return() # Benötigt, damit leeres Feld nicht None ergibt
    devastating_wounds, lethal_hits, sustained_hits = keywords_return() 
    probability_to_crit_hit = p.probability_critical_hit()
    probability_to_hit = p.probability_hit(bs_ws)
    probability_to_wound = p.probability_wound(s,t)
    average_hits = p.calculus_hit(attacks, probability_to_hit)
    average_hits_mod, sustained_hits = p.sustained_hits_calc(average_hits, sustained_hits, sustained_hits_nr, probability_to_crit_hit)
    average_wounds = p.calculus_wound(average_hits_mod, probability_to_wound)
    devastating_wounds, average_wounds = p.devastating_wounds(average_wounds, devastating_wounds, probability_to_crit_hit)
    probability_to_inv = p.probability_inv(inv)
    probability_to_sv = p.probability_sv(sv, ap)
    probability_to_defend = p.decider(probability_to_inv, probability_to_sv)
    probability_to_feel_no_pain = p.probability_feel_no_pain(fnp)
    average_saves = p.calculus_saves(probability_to_defend, average_wounds)
    true_wounds = p.true_wounds(average_wounds, average_saves, devastating_wounds)
    average_damage, feel_no_pain_saves = p.calculus_damage(d, probability_to_feel_no_pain, true_wounds)
    label_ergebnis.config(text=f"Average Damage: {average_damage}" 
                          f"\nAverage hits: {average_hits}"
                          f"\nSustained hits: {sustained_hits}"
                          f"\nAverage wounds:  {average_wounds}"
                          f"\nDevastating wounds: {devastating_wounds}"
                          f"\nSaves: {average_saves}"
                          f"\nFeel No Pain: {feel_no_pain_saves}")

# Erstellen des Hauptfensters
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Damage Calculator v.01")
    root.geometry("750x400")  # Fenstergröße festlegen
#####################################################################################################
#####################################################################################################
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

label_platzhalter1 =tk.Label(root, text = "              ")
label_platzhalter1.grid(row=9, column=0)

label_platzhalter2=tk.Label(root, text="___")
label_platzhalter2.grid(row=2, column=6, sticky="ew")

label_platzhalter3=tk.Label(root, text="___")
label_platzhalter3.grid(row=2, column=9, sticky="ew")


#Erstellen der Label für Defender
#####################################################################################################
defenders_profile = tk.Label(root, text="Defender's Profile:")
defenders_profile.grid(row=6, column =0)

#Thoughness Widget
label_T = tk.Label(root, text= "T")
label_T.grid(row=7, column=1, sticky="ew",padx=12)
entry_T = tk.Entry(root, width=3)
entry_T.grid(row=8, column=1, sticky="ew",padx=12)

#Saving Throw Widget
label_SV = tk.Label(root, text= "SV")
label_SV.grid(row=7, column=2, sticky="ew",padx=12)
entry_SV = tk.Entry(root, width=3)
entry_SV.grid(row=8, column=2, sticky="ew",padx=12)

#Invulnerable Save Widget
label_INV = tk.Label(root, text= "INV")
label_INV.grid(row=7, column=3, sticky="ew",padx=12)
entry_INV = tk.Entry(root, width=3)
entry_INV.grid(row=8, column=3, sticky="ew",padx=12)

#FeelNoPain Widget
label_FNP = tk.Label(root, text= "FNP")
label_FNP.grid(row=7, column=4, sticky="ew",padx=12)
entry_FNP = tk.Entry(root, width=3)
entry_FNP.grid(row=8, column=4, sticky="ew",padx=12)

#####################################################################################################
#####################################################################################################

#Defender's profil
def d_profile():
    t = int(entry_T.get())
    sv = int(entry_SV.get())
    inv = int(entry_INV.get())
    fnp = int(entry_FNP.get())
    return t, sv, inv, fnp

def toggle_entry_state():
    if check_sustained.get() == True:
        entry_sustained_hits.config(state='normal')  # Entry aktivieren
    else:
        entry_sustained_hits.delete(0, tk.END)
        entry_sustained_hits.config(state='disabled') # Entry deaktivieren
    if check_melta.get() == True:
        entry_melta_damage.config(state='normal')
    else:
        entry_melta_damage.config(state='disabled')
    if check_anti_inf.get() == True:
        entry_anti_infantry.config(state="normal")
    else:
        entry_anti_infantry.config(state="disabled")
    if check_anti_fly.get() == True:
        entry_anti_flyer.config(state="normal")
    else:
        entry_anti_flyer.config(state="disabled")

def keywords_return():
    devastating_wounds = bool(check_devastating.get())
    lethal_hits = bool(check_lethal.get())
    sustained_hits = bool(check_sustained.get())
    return devastating_wounds, lethal_hits, sustained_hits

def sustain_return():
    if check_sustained.get() == True:
        sustained_hits_nr = int(entry_sustained_hits.get())
        return sustained_hits_nr
    else:
        sustained_hits_nr = 0
        return sustained_hits_nr
        
    
#Checkboxen für Keywords-Modifier
#Devastating Wounds, Sustained Hits(x), Lethal hits, Rapid Fire(x), Twin-Linked
check_devastating = tk.BooleanVar()
check_devastating_wounds = tk.Checkbutton(root, text="Devastating Wounds", variable=check_devastating)
check_devastating_wounds.grid(row=1, column=7, sticky="ws")

#Checkbox und Entryfeld für Sustained Hits Keyword-Widget
check_sustained = tk.BooleanVar() #möchte den wert der in der checkbox gespeichert werden, als Boolean haben
check_sustained_hits = tk.Checkbutton(root, text="Sustained Hits", variable=check_sustained, command=toggle_entry_state)
check_sustained_hits.grid(row=2, column=7, sticky="w")
entry_sustained_hits = tk.Entry(root, width=2, state="disabled")
entry_sustained_hits.grid(row=2, column=8, sticky="e")

#Checkbox für Lethal Hits Keyword-Widget
check_lethal = tk.BooleanVar()
check_lethal_hits = tk.Checkbutton(root, text="Lethal Hits")
check_lethal_hits.grid(row=3, column=7, sticky="w")

#Checkbox und Entryfeld für Melta Keyword-Widget
check_melta= tk.BooleanVar() #möchte den wert der in der checkbox gespeichert werden, als Boolean haben
check_melta_damage = tk.Checkbutton(root, text="Melta", variable=check_melta, command=toggle_entry_state)
check_melta_damage.grid(row=4, column=7, sticky="w")
entry_melta_damage = tk.Entry(root, width=2, state="disabled")
entry_melta_damage.grid(row=4, column=8, sticky="e")

check_anti_inf=tk.BooleanVar()
check_anti_infantry =tk.Checkbutton(root, text="Anti-Infantry     ", variable=check_anti_inf, command=toggle_entry_state)
check_anti_infantry.grid(row=2, column=10, sticky="w")
entry_anti_infantry = tk.Entry(root, width=2, state="disabled")
entry_anti_infantry.grid(row=2, column=10, sticky="e")

check_anti_fly=tk.BooleanVar()
check_anti_flyer =tk.Checkbutton(root, text="Anti-Fly     ", variable=check_anti_fly, command=toggle_entry_state)
check_anti_flyer.grid(row=3, column=10, sticky="w")
entry_anti_flyer = tk.Entry(root, width=2, state="disabled")
entry_anti_flyer.grid(row=3, column=10, sticky="e")


check_torrent=tk.BooleanVar()
check_torrent_weapon = tk.Checkbutton(root, text="Torrent", variable=check_torrent, command=toggle_entry_state)
check_torrent_weapon.grid(row=1, column=10, sticky="ws")


#Button zum Ausrechnen
rechner = tk.Button(root, text = "ATTACK", command=main_rechner)
rechner.grid(row=10, column= 0)

#Ausgabefeld des Ergebnisses
label_ergebnis = tk.Label(root, text= "Average Damage: ")
label_ergebnis.grid(row=11, column=0)

# Hauptschleife starten
root.mainloop()






