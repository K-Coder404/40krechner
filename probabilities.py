#probabilites.py
#Berechnung der Wahrscheinlichkeit für erfolgreichen Hit
def probability_critical_hit():
    probability_to_crit_hit = 1/6
    return probability_to_crit_hit

def probability_hit(bs_ws):
    if bs_ws < 1:
        return None  # Wenn bs_ws kleiner als 1 ist, gibt es keine gültige Berechnung
    
    probability_to_hit = (7 - bs_ws) / 6
    return probability_to_hit if 1 <= bs_ws <= 6 else None

#Berechnung der Wahrscheinlichkeit für erfolgreiche Verwundung
def probability_wound(s, t):
    if s == t:
        probability_to_wound = 3 / 6  # 4+
    elif s > t and s < 2 * t:
        probability_to_wound = 4 / 6  # 3+
    elif s < t:
        probability_to_wound = 2 / 6  # 5+
    elif t >= 2 * s:
        probability_to_wound = 1 / 6  # 6+
    elif s>= 2*t:
        probability_to_wound = 5 / 6 #2+
    else:    
        return None
    return probability_to_wound

#Berechnung der Wahrscheinlichkeit für erfolgreichen Rüstungswurf
def probability_sv(sv,ap):
    sv_modified = sv - ap
    if  sv_modified == 2:
        probability_to_save = 5/6   #2+
        return probability_to_save 
    elif sv_modified == 3:
        probability_to_save = 4/6   #3+
        return probability_to_save
    elif sv_modified == 4:
        probability_to_save = 3/6   #4+
        return probability_to_save
    elif sv_modified == 5:
        probability_to_save = 2/6   #5+
        return probability_to_save
    elif sv_modified == 6:
        probability_to_save = 1/6   #6
        return probability_to_save
    elif sv_modified >6:            #Sv auf 7 unmöglich, deshalb save prob 0%
        probability_to_save = 0
        return probability_to_save
    else:
        probability_to_save = 0
        return probability_to_save
    
def probability_feel_no_pain(fnp):
    if fnp <= 3:
        probability_to_feel_no_pain = 0
        return probability_to_feel_no_pain 
    if fnp >= 4 and fnp <=6:
        probability_to_feel_no_pain = (7 - fnp) / 6
        return probability_to_feel_no_pain


#Berechnung der Wahrscheinlichkeit für einen erfolgreichen invulnerable save - Wurf
def probability_inv(inv):
    if inv >= 1 and inv <= 6:
        probability_to_inv = (7 - inv) / 6
        return probability_to_inv
    else:
        probability_to_inv = 0   
        return probability_to_inv

# Funktion, die entscheidet, ob Rüstungswurf (sv) oder invulnerable save (inv) 
# zur Verteidigung benutzt wird
# Es wird immer das bessere Ergebnis benutzt!
def decider(probability_to_inv, probability_to_sv):
    if probability_to_inv >= probability_to_sv:
        probability_to_defend = probability_to_inv
        return probability_to_defend
    else:
        probability_to_defend = probability_to_sv
        return probability_to_defend

#Berechnung der durchschnittlichen Hits
def calculus_hit(attacks, probability_to_hit):
    average_hits = attacks*probability_to_hit
    return average_hits

def sustained_hits_calc(average_hits, sustained_hits, sustained_hits_nr, probability_to_crit_hit):
    if sustained_hits == True:
        sustained_hits = float(sustained_hits)
        sustained_hits = average_hits*probability_to_crit_hit
        sustained_hits *= sustained_hits_nr
        average_hits_mod = sustained_hits + average_hits
        return average_hits_mod, sustained_hits
    else:
        sustained_hits = 0
        average_hits_mod = sustained_hits + average_hits
        return average_hits_mod, sustained_hits

def devastating_wounds(average_wounds, devastating_wounds, probability_to_crit_hit):
    if devastating_wounds == True:
        devastating_wounds = float(devastating_wounds)
        devastating_wounds = probability_to_crit_hit*average_wounds
        average_wounds -= devastating_wounds
        return devastating_wounds, average_wounds
    else:
        devastating_wounds = 0
        average_wounds -= devastating_wounds
        return devastating_wounds, average_wounds

"""def lethal_hits(average_hits):
    if lethal_hits == True:
        lethal_hits = float(lethal_hits)
        lethal_hits = 1/6*average_hits
        return lethal_hits
    else:
        None"""

#Berechnung der Wunde/Wunden, die zugeführt werden
def calculus_wound(average_hits_mod, probability_to_wound):
    average_wounds = average_hits_mod*probability_to_wound
    return average_wounds

#Berechnung der Saves/Schaden, der verhindert wird
def calculus_saves(probability_to_defend, average_wounds):
    average_saves = average_wounds*probability_to_defend
    return average_saves

def true_wounds(average_wounds, average_saves, devastating_wounds):
    true_wounds = average_wounds - average_saves
    true_wounds = true_wounds + devastating_wounds    
    return true_wounds 

#Berechnung des durchschnittlichen Schadens
def calculus_damage(d, probability_to_feel_no_pain, true_wounds):
    if probability_to_feel_no_pain <=0:
        average_damage = d*true_wounds
        feel_no_pain_saves = 0
        return average_damage, feel_no_pain_saves
    elif probability_to_feel_no_pain >0:
        average_damage = d*true_wounds*probability_to_feel_no_pain
        feel_no_pain_saves = true_wounds-average_damage
        return average_damage, feel_no_pain_saves
    else:
        return None
