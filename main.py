

import random

noms_monstres = ["aryo", "momo","bigario" ]

stats = {
    "victoires": 0 ,
    "defaites": 0 ,
    "evites": 0
}
MAX_TOURS = 10
pv_hero = 20
tour = 1
monstres_vaincus = 0
monstres_evites = 0
defaites_combat = 0
monstres_evites = 0

def afficher_regles():
    print("\n--- RÈGLES DU JEU ---")
    print("Vous commencez avec 20 PV.")
    print("Combattre : 50% de chance de gagner (+3 PV). Sinon, vous perdez les PV de la force du monstre.")
    print(f"- Éviter : Vous fuyez mais perdez PV à coup sûr.")
    print(f"- But : Survivre à {MAX_TOURS} tours.")
    print("---------------------\n")

def afficher_etat(pv, tour):

    print(f"\n TOUR {tour}")
    print(f" Héros : {pv_hero} PV")

def combattre(pv):

    global pv_hero, stats

    monstre = random.choice(noms_monstres)
    force = random.randint(1,8)

    print(f"\n Un {monstre} apparaît ! Sa force est de {force}.")
    chance = random.randint(1, 2)
    force = 8
    if force > 7:
        pv_hero = pv_hero + force
        stats["vaincus"] += 1
        print(f"Victoire ! Vous tuez le {monstre} et gagnez 3 PV.")
    else:
        pv_hero = pv_hero - force
        stats["combat"] +=1
        print(f"Défaite ! Le {monstre} vous inflige {force} dégâts.")

def eviter(pv):
    global pv_hero, monstres_evites, stats
    penaltie = 2
    pv_hero = pv_hero - penaltie
    monstres_evites = monstres_evites + 1
    print(f"\Vous fuyez en courant ! Vous perdez -PV.")

print("Bienvenue dans le jeu de combat !")
afficher_regles()
while pv_hero > 0 and tour <= MAX_TOURS:
    afficher_etat(pv_hero, tour)

    choix = input("Que voulez-vous faire ? (combattre / eviter / regles):")
    if choix == "combattre":
        pv_hero = combattre(pv_hero)
        tour = tour + 1
    elif choix == "eviter":
        eviter()
        tour = tour + 1

    elif choix == "regles":
        afficher_regles()

    else:
        print("Option invalide ! Merci d'écrire exactement 'combattre', 'eviter' ou 'regles'.")


print("FIN DE LA PARTIE")

if pv_hero > 0:
    print("Félicitations, vous avez gangé l'aventure!")
else:
    print(" Dommage vous êtes mort au combat.")

print(f"\nTours survécus : {tour - 1}")
print(f"Monstres vaincus : {monstres_vaincus}")
print(f"Monstres évités : {monstres_evites}")
print(f"Défaites subies : {defaites_combat}")