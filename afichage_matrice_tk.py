#-------------------------------------------------------------------------------
# Name:        afichage_matr
# Purpose:
#
# Author:      Elizabeth S
#
# Created:     10.02.2023
# Copyright:   (c) Elizabeth S 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from numpy import *
from matrices_cal import *


def get_matrice(mat):
    matrice = []
    idx = 0

    for i in mat.get("1.0", END).splitlines():
        if i != '':
            matrice.append([])
            for j in i.split(","):
                if j.lstrip("-").isnumeric():
                    matrice[idx].append((int(j)))
            idx += 1
    return matrice

def result(field, result):
    field.insert(END, result)

# fonction pour appeler fonction addition en appyant le bouton "Addition Matrices"
def result_add_matrice():
    mat_1 = get_matrice(labela)
    mat_2 = get_matrice(labelb)
    matrice = add_matrice(mat_1, mat_2)
    result_ans.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

# fonction pour appeler fonction multiplication_par_scalaire en appyant le bouton "Multiplication par scalaire"
def result_multiplication_mat_scal():
    mat = get_matrice(labela)
    matrice = multiplication_mat_scal(mat, int(scalaire.get()))
    result_ans.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

# fonction pour appeler fonction transition_matrice en appyant le bouton
def resultat_transition_matrice():
    mat = get_matrice(labela)
    matrice = transition_matrice(mat)
    result_ans.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")
def resultat_transition_matrice_b():
    mat = get_matrice(labelb)
    matrice = transition_matrice(mat)
    result_ans.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

def resultat_multipli_matrices():
    mat_1 = get_matrice(labela)
    mat_2 = get_matrice(labelb)
    matrice = multiplication_matrs(mat_1, mat_2)
    result_ans.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")



# fonction pour appeler fonction calcul_inversion_matrice_carre en appyant le bouton
def resultat_inversion_matrice():
    mat1 = get_matrice(labela)
    matrice = matrice_inverse(mat1)
    result_ans.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")



#création de la fenetre principale (main window)
Mafenetre = Tk()
Mafenetre.geometry("1000x1000")
Mafenetre.title('WINGS Matrice Analog')
Mafenetre.config(bg = "#21618c")




#création de la fenetre pour les entrées
entrees = Frame(Mafenetre, bg='#2874a6',width=1000, height=250)
entrees.propagate(False)
entrees.pack(side = TOP, padx = 5, pady=5)


result_frame = Frame(Mafenetre, bg='#7FB3D5',width= 1000, height=250)
result_frame.pack(side = BOTTOM, padx=25, pady=10)

#création de la fenetre pour les calculs
calculs = Frame(Mafenetre,width= 950, height=450, bg='#D6EAF8')
calculs.pack(side = TOP, pady=10)

# creation les fenetres por saisir les matr

labela = Text(entrees, width=50,height=80)
labela.pack(side = LEFT,padx = 5, pady = 5)

labelb = Text(entrees,width=50,height=80)
labelb.pack(side = LEFT, padx = 110, pady = 5)
#création de la fenetre pour l'affichage
result_ans = Text(result_frame, width= 60,height = 15 )
result_ans.pack(side = LEFT,padx=250,pady=5)
result_frame.propagate(False)
#creation scalaire
frame_scalaire = Frame(calculs, width=80,height=50 ,bg="#F0E9F7")
frame_scalaire.pack(anchor=NW, padx=5, pady=5)
frame_scalaire.propagate(False)
label_scalaire = Label(frame_scalaire, text="Scalaire :", bg="#DBC0F7")
label_scalaire.pack(anchor=W)
scalaire = Entry(frame_scalaire, width=10)
scalaire.pack(anchor=NW, padx=5, pady=5)
#partie calculs
BoutonAddition = Button(calculs,text='Addition',command=result_add_matrice)
BoutonAddition.pack(side = LEFT, padx = 10, pady = 10)

BoutonMultiplicationSc = Button(calculs,text='Multiplication_sc',command=result_multiplication_mat_scal)
BoutonMultiplicationSc.pack(side = LEFT, padx = 5, pady = 5)

BoutonMultiplicationM = Button(calculs,text='Multiplication_matrices',command=resultat_multipli_matrices)
BoutonMultiplicationM.pack(side = LEFT, padx = 5, pady = 10)
'''BoutonDeterminantA = Button(calculs,text='DeterminantA',command=resultat_elimination_matrices,fg ="white",bg="#5955D3")
BoutonDeterminantA.pack(side = LEFT, padx = 4, pady = 4)
BoutonDeterminantB = Button(calculs,text='DeterminantB',command=resultat_elimination_matrices,fg ="white",bg="#5955D3")
BoutonDeterminantB.pack(side = LEFT, padx = 6, pady = 6)'''

BoutonQuitter = Button(calculs, text = 'Quitter', command= Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT)

BoutonInverseA = Button(calculs, text = 'Inversion de A', command = resultat_inversion_matrice)
BoutonInverseA.pack(side = LEFT,padx = 5, pady = 5)
BoutonInverseB = Button(calculs, text = 'Inversion de B', command = resultat_inversion_matrice)
BoutonInverseB.pack(side = LEFT,padx = 5, pady = 5)

BoutonTransA = Button(calculs, text = 'Transposé de A', command = resultat_transition_matrice)
BoutonTransA.pack(side = LEFT,padx = 5, pady = 5)
BoutonTransB = Button(calculs, text = 'Transposé de B', command = resultat_transition_matrice_b)
BoutonTransB.pack(side = LEFT,padx = 5, pady = 5)

'''
def len_matrices_egal(mat_a, mat_b):
    """Si la dimentions sont identiques"""
    if len(mat_a) == len(mat_b) and len(mat_a[0]) == len(mat_b[0]):
        return True
    else:
        return False

#Addition les deux matrices le même dimention
def add_matrice(mat_a, mat_b):
    result = []
    if len_matrices_egal(mat_a, mat_b):
       for i in range(0,len(mat_a)):
        vase = []
        for j in range(0,len(mat_a[i])):
            vase.append(mat_a[i][j] + mat_b[i][j])
            result.append(vase)
        return  result
    else:
        return "Les dimention des matrices sont differents."





#Multiplication d'une matrice par un scalaire
def multiplication_mat_scal(matrice,lam):
    result = []

    for i in range(0,len(matrice)):
        mat = []
        for j in range(0,len(matrice[i])):
            mat.append(matrice[i][j] * int(lam))
        result.append(mat)
    return  result



#Retourne la multiplication de matrices
def verifier_matrices_pour_multiplication(mat_a, mat_b):
    if len(mat_a[0]) == len(mat_b):
        return True
    else:
        return False



# Retourne la multiplication de matrices
def multiplication_matrs(a,b):
    result_m = []
    if verifier_matrices_pour_multiplication(a,b):
       for i in range(0,len(a)):
        vase = []
        for j in range(0,len(a[0])): # mb 0
            total = 0
            for k in range(0,len(a[i])):
                total = total +a[i][k]*b[k][j]
            vase.append(total)
        result_m.append(vase)
    return result_m


#Colonnes devient de lignes, lignes devient les colonnes
def transition_matrice(matrice):
   result_m = []

   for j in range(len(matrice[0])):
        tr = []
        for i in range(len(matrice)):
            tr.append(matrice[i][j])
        result_m.append(tr)
   return result_m


def calcul_determinant_matrice2(matrice):
    if len(matrice) == 2 and len(matrice[0]) == 2:
       for i in range(0,len(matrice)):
        for j in range(0,len(matrice[i])):
            det=matrice[0][0]*matrice[1][1]- matrice[1][0]*matrice[0][1]
    return det

def matrice_inverse(mat_or):
    det = calcul_determinant_matrice2(mat_or)
    if det != 0:
        tmp = mat_or[0][0]
        mat_or[0][0] = mat_or[1][1]
        mat_or[1][1] = tmp

        mat_or[0][1]*=-1
        mat_or[1][0]*=-1

        mati = []
        for ligne in mat_or:
            matj = []
            for element in ligne:
                matj.append(element*int(1/det))
            mati.append(matj)
        return mati
    else:
        print("Operation impossible.Le determinant est égale a zero")
        return None

#mat1 = [[1,2],[4,5]]

def verifier_que_matrice_carre(matrice):
    if len(matrice) == len(matrice[0]) == 2:
        return True
    else:
        return False
'''

Mafenetre.mainloop()