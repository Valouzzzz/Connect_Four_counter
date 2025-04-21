'''
    [5, 5, 5, 5, 5, 5, 5]
    [4, 4, 4, 4, 4, 4, 4]
    [3, 3, 3, 3, 3, 3, 3]
    [2, 2, 2, 2, 2, 2, 2]
    [1, 1, 1, 1, 1, 1, 1]
    [0, 0, 0, 0, 0, 0, 0]
    [A, B, C, D, E, F, G]
'''

A = ['3', '4', '5', '5', '4', '3']
B = ['4', '6', '8', '8', '6', '4']
C = ['5', '8', '11', '11', '8', '5']
D = ['7', '10', '14', '14', '10', '7']
E = ['5', '8', '11', '11', '8', '5']
F = ['4', '6', '8', '8', '6', '4']
G = ['3', '4', '5', '5', '4', '3']

a = b = c = d = e = f = g = 0
x = 0

coup_colone_A = []
coup_colone_B = []
coup_colone_C = []
coup_colone_D = []
coup_colone_E = []
coup_colone_F = []
coup_colone_G = []

def safe_get(lst, index):
    return lst[index] if index < len(lst) else "X"

def resulta():
    print(f"A[{a}] = {safe_get(A, a)}, B[{b}] = {safe_get(B, b)}, C[{c}] = {safe_get(C, c)}, D[{d}] = {safe_get(D, d)}, E[{e}] = {safe_get(E, e)}, F[{f}] = {safe_get(F, f)}, G[{g}] = {safe_get(G, g)}")
print("Tu peux jouer :")
resulta()

def detecter_triple_J_horizontal():
    lignes = 6
    colonnes_coups = [
        coup_colone_A,
        coup_colone_B,
        coup_colone_C,
        coup_colone_D,
        coup_colone_E,
        coup_colone_F,
        coup_colone_G,
    ]

    for ligne in range(lignes):
        for col in range(len(colonnes_coups) - 2):
            try:
                if (
                    colonnes_coups[col][ligne] == 'J' and
                    colonnes_coups[col + 1][ligne] == 'J' and
                    colonnes_coups[col + 2][ligne] == 'J'
                ):
                    return True
            except IndexError:
                continue
    return False

def contrer_triple_J_diagonal():
    colonnes = [
        coup_colone_A,
        coup_colone_B,
        coup_colone_C,
        coup_colone_D,
        coup_colone_E,
        coup_colone_F,
        coup_colone_G,
    ]
    noms_colonnes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    indices = [a, b, c, d, e, f, g]

    lignes = 6

    for ligne in range(lignes):
        for col in range(5):
            try:
                if (
                    colonnes[col][ligne] == 'J' and
                    colonnes[col + 1][ligne + 1] == 'J' and
                    colonnes[col + 2][ligne + 2] == 'J'
                ):
                    if col > 0 and len(colonnes[col - 1]) == ligne - 1:
                        colonnes[col - 1].append('I')
                        print(f"IA : Je contre en colonne {noms_colonnes[col - 1]} à la ligne {ligne - 1}")
                        mettre_a_jour_index(noms_colonnes[col - 1])
                        return True
                    if col + 3 < 7 and len(colonnes[col + 3]) == ligne + 3:
                        colonnes[col + 3].append('I')
                        print(f"IA : Je contre en colonne {noms_colonnes[col + 3]} à la ligne {ligne + 3}")
                        mettre_a_jour_index(noms_colonnes[col + 3])
                        return True
            except IndexError:
                continue

            try:
                if (
                    colonnes[col][ligne + 2] == 'J' and
                    colonnes[col + 1][ligne + 1] == 'J' and
                    colonnes[col + 2][ligne] == 'J'
                ):
                    if col > 0 and len(colonnes[col - 1]) == ligne + 3:
                        colonnes[col - 1].append('I')
                        print(f"IA : Je contre en colonne {noms_colonnes[col - 1]} à la ligne {ligne + 3}")
                        mettre_a_jour_index(noms_colonnes[col - 1])
                        return True
                    if col + 3 < 7 and len(colonnes[col + 3]) == ligne - 1:
                        colonnes[col + 3].append('I')
                        print(f"IA : Je contre en colonne {noms_colonnes[col + 3]} à la ligne {ligne - 1}")
                        mettre_a_jour_index(noms_colonnes[col + 3])
                        return True
            except IndexError:
                continue

    return False



def contrer_triple_J_horizontal():
    colonnes = [
        coup_colone_A,
        coup_colone_B,
        coup_colone_C,
        coup_colone_D,
        coup_colone_E,
        coup_colone_F,
        coup_colone_G,
    ]
    noms_colonnes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    indices = [a, b, c, d, e, f, g]
    hauteurs = [len(col) for col in colonnes]
    max_lignes = max(hauteurs)

    for ligne in range(max_lignes):
        for i in range(5): 
            try:
                if (
                    colonnes[i][ligne] == 'J' and
                    colonnes[i+1][ligne] == 'J' and
                    colonnes[i+2][ligne] == 'J'
                ):
                    if i > 0 and len(colonnes[i-1]) == ligne:
                        colonnes[i-1].insert(ligne, 'I')
                        print(f"IA : Je contre en colonne {noms_colonnes[i-1]} à la ligne {ligne}")
                        mettre_a_jour_index(noms_colonnes[i-1])
                        return True
                    if i+3 < len(colonnes) and len(colonnes[i+3]) == ligne:
                        colonnes[i+3].insert(ligne, 'I')
                        print(f"IA : Je contre en colonne {noms_colonnes[i+3]} à la ligne {ligne}")
                        mettre_a_jour_index(noms_colonnes[i+3])
                        return True
            except IndexError:
                continue
    return False


def mettre_a_jour_index(nom_colonne):
    global a, b, c, d, e, f, g
    if nom_colonne == 'A':
        a += 1
    elif nom_colonne == 'B':
        b += 1
    elif nom_colonne == 'C':
        c += 1
    elif nom_colonne == 'D':
        d += 1
    elif nom_colonne == 'E':
        e += 1
    elif nom_colonne == 'F':
        f += 1
    elif nom_colonne == 'G':
        g += 1



def IA_Grande_Val():
    global a, b, c, d, e, f, g

    colonnes_donnees = {
        "A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G
    }
    indices = {
        "A": a, "B": b, "C": c, "D": d, "E": e, "F": f, "G": g
    }
    colonnes_coups = {
        "A": coup_colone_A, "B": coup_colone_B, "C": coup_colone_C,
        "D": coup_colone_D, "E": coup_colone_E, "F": coup_colone_F,
        "G": coup_colone_G
    }

    valeurs = {
        lettre: int(col[indices[lettre]]) if indices[lettre] < len(col) else -1
        for lettre, col in colonnes_donnees.items()
    }

    sorted_valeurs = sorted(valeurs.items(), key=lambda x: x[1], reverse=True)

    triple_J_detecte = {
        col: any(coups[i:i+3] == ['J', 'J', 'J'] for i in range(len(coups) - 2))
        for col, coups in colonnes_coups.items()
    }
    contrer_detecte = {
        col: any(coups[i:i+4] == ['J', 'J', 'J', 'I'] for i in range(len(coups) - 3))
        for col, coups in colonnes_coups.items()
    }

    triple_J_horizontal = detecter_triple_J_horizontal()

    for col in colonnes_donnees:
        if triple_J_detecte[col] and not contrer_detecte[col] and indices[col] < len(colonnes_donnees[col]):
            indices[col] += 1
            colonnes_coups[col].insert(indices[col], "I")
            print(f"IA : Je bloque en jouant colonne {col} (valeur = {valeurs[col]})")
            break
        
    if contrer_triple_J_horizontal():
        return
    if contrer_triple_J_diagonal():
        return

    elif not contrer_triple_J_horizontal or not triple_J_detecte[col] and not contrer_detecte[col] and indices[col] < len(colonnes_donnees[col]) :
        for col, val in sorted_valeurs:
            if indices[col] < len(colonnes_donnees[col]):
                indices[col] += 1
                colonnes_coups[col].insert(indices[col], "I")
                print(f"IA : Je joue la colonne {col} (valeur = {val})")
                break
        else:
            print("IA : Aucune colonne disponible pour jouer (toutes pleines).")

    a, b, c, d, e, f, g = indices["A"], indices["B"], indices["C"], indices["D"], indices["E"], indices["F"], indices["G"]


while x == 0:
    print(end='\n')
    
    IA_Grande_Val()
    resulta()
    print(coup_colone_A, coup_colone_B, coup_colone_C, coup_colone_D, coup_colone_E, coup_colone_F, coup_colone_G)
    
    question = input("Tu veux jouer quoi ? ").upper()

    if question == "A" and a < len(A):
        a += 1
        coup_colone_A.insert(a, "J")
    elif question == "B" and b < len(B):
        b += 1
        coup_colone_B.insert(b, "J")
    elif question == "C" and c < len(C):
        c += 1
        coup_colone_C.insert(c, "J")
    elif question == "D" and d < len(D):
        d += 1
        coup_colone_D.insert(d, "J")
    elif question == "E" and e < len(E):
        e += 1
        coup_colone_E.insert(e, "J")
    elif question == "F" and f < len(F):
        f += 1
        coup_colone_F.insert(f, "J")
    elif question == "G" and g < len(G):
        g += 1
        coup_colone_G.insert(g, "J")
    else:
        print("Cette colonne est déjà pleine ou invalide.")
        continue
    
    
    

