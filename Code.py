'''

Programme Python 
Quizz sur les capitales du monde avec des données CSV


Réalisé par Lana Linord et Nathan Bosy


'''




'''
I - Importation des bibliothèques
'''

from random import *                                             # Pour les fonctions aléatoires
from tkinter import *                                            # Pour l'interface graphique utilisateur

import os                                                        # Pour redémarer le programme
import sys                                                       # Idem






'''
II - Fonction qui charge note fichier CSV dans un dictionnaire
'''

def load() :
    
    file = open('capitales.csv', 'r')                            # On ouvre le fichier, en lecture seulement
    
    dict = {}                                                    # Création de notre dictionnaire

    for line in file.readlines() :                               # Création d'une boucle pour remplir le dictionaire ligne par ligne
        
        pos1 = line.find(';')                                    # On cherche la position du séparateur
        pos2 = line.find('\n')                                   # On cherche maintenant la position de la fin de ligne
        country = line[:pos1]                                    # On ajoute les caractère avant le séparateur dans pays
        capital = line[pos1+1:pos2]                              # Puis dans capitale tout le reste jusqu'à la fin de la ligne
        
        dict[country]=capital                                    # On rajouter nos valeurs dans le dictionnaire
        
    return dict                                                  # On renvoie le dictionnaire au complet une fois la boucle terminée





'''
III - Fonction qui créer les variables
'''

def intro() :
    
    global already_use,good_answer,values,length,country,capital # On utilise 6 variables globales
    entry.delete(0,END)                                          # On supprime la zone de texte

    already_use = []                                             # Tableau qui ajoute les questions déjà posées
    good_answer = 0                                              # Variable qui comptabilise le nombre de bonnes réponses
    values = load()                                              # Variable qui permet de récuprer le dictionnaire du CSV
    length = len(values)                                         # Variable qui va calculer la longueur du dictionnaire
    
    country = list(values.keys())                                # Convertion des clés de notre dictionnaire en liste
    capital = list(values.values())                              # Même chose pour les valeurs cette fois-ci

    label.configure(text='Combien veux-tu de questions ?'
                    ,fg='black')                                 # Texte qui demande le nombre de questions
    button.configure(text='Valider',command=nb_questions)        # Bouton qui actionne la prochaine fonction



'''
IV - Fonction demande le nombre ques questions
'''

def nb_questions() :                                              
    global nb_questions                                          # Création de la variable
    if int(entry.get()) >= 197 or int(entry.get()) <= 0 :        # Si le nombre est pas dans l'intervalle
        label.configure(text='Le nombre doit être compris entre 0 et %s' % (len(values)))
    else :
        nb_questions = int(entry.get())                          # On définit la variable comme une entrée de nombre entier
        entry.delete(0,END)                                      # On supprime la zone de texte
        quizz()                                                  # On utilise la fonction qui va suivre :





'''
V - Fonction qui attend la réponse, comptabilise puis propose de rejouer
'''

def quizz() :
    
    if len(already_use)<nb_questions :                           # Création d'une boucle avec le nombre de questions demandées
        global j                                                 # Utilisation de la variable globale
        
        j = randint(0,length-1)                                  # Utilisation de l'aléatoire par rapport aux nombre de valeurs
        
        while j in already_use :                                 # Si l'aléatoire tombe sur une question déjà posée
            j = randint(0,length-1)                              # On réutilise l'aléatoire
            
        already_use.append(j)                                    # On ajoute la valeure obtenue dans notre liste de questions déjàs posées
        
        label.configure(text='%s ?' % (country[j]),
                        fg='black')                              # Texte qui demande la capitale du pays
        button.configure(command=check)                          # Utilisation de la fonction pour vérifier la réponse
        
        
    elif good_answer<=1 :                                        # Si il n'y a qu'une ou zéro bonne réponse
        label.configure(text='Tu as eu %d bonne réponse sur %d, tu peux faire mieux !'
                        % (good_answer,nb_questions),fg="black") # Texte de fin de partie (signulier)
        button.configure(text='Rejouer',command=restart)         # Bouton qui propose de rejouer

    else :                                                       # Si plus qu'une bonne réponse
        label.configure(text='Tu as eu %d bonnes réponses sur %d !'
                        % (good_answer,nb_questions),fg="black") # Texte de fin de partie (pluriel)
        button.configure(text='Rejouer',command=restart)         # Bouton qui propose de rejouer





'''
VI - Fonction qui redémarre le prgramme
'''

def restart():      
    os.execl(sys.executable,                                     # Execute l'executable python
             os.path.abspath(__file__),                          # Le fichier actuel
             *sys.argv)                                          # Avec les arguments actuels




'''
VII - Fonction qui vérifie la réponse et qui ajoute un commentaire
'''

def check() :
    reponse = entry.get()                                        # Créer la variable de notre réponse pour vérifier
    entry.delete(0,END)                                          # On supprime la zone de texte
    
    if reponse.lower() == capital[j].lower():                    # Si c'est la bonne réponse (on transforme tout en minuscule) :
        global good_answer                                       # On utilise la valeure globale...
        good_answer += 1                                         # ...et on lui rajoute 1
        label.configure(text='Bonne réponse !',fg='green')       # Puis on affiche un message
        button.configure(text='Suivant',command=quizz)           # Création du bouton suivant
        
    else :                                                       # Si ce n'est pas la bonne réponse :
        label.configure(text="Loupé, c'était %s !" % capital[j]
                        ,fg='red')                               # On affiche la bonne réponse
        button.configure(text='Suivant',command=quizz)           # Création du bouton suivant





'''
VIII - Création de l'interface graphique utilisateur
'''

gui = Tk()                                                       # Création de la fenêtre
gui.title('Quizz des capitales')                                 # On nomme la fenêtre
gui.geometry('500x400')                                          # On définit la taille
gui.resizable(height=False,width=False)                          # On désactive le fait de pouvoir modifier la taille
gui.configure(bg='white')                                        # On met le fond en blanc



# Titre principal
title = Label(gui,text='Bienvenue sur le quizz des capitales !',
                    font=('Segoe UI Black',20),                  
                    bg='white')                                  # On rentre le texte, la police, sa taille, et la couleur
title.grid(column=0,row=0,sticky='n')                            # On place l'élément dans notre fenêtre


# Sous-titre
text=Label(gui,text='Ton but est de trouver le plus de capitales possible\n\n\n',
           font=('Segoe UI',14),
           bg='white')
text.grid(column=0,row=1,sticky='n')


# Texte qui nous sert pour les questions
label = Label(gui)
label.configure(font=('Segoe UI',14),bg='white')
label.grid(column=0,row=2,sticky='n')


# Entrée utilisateur
entry = Entry(gui)
entry.grid(column=0,row=3,sticky='n')


# Bouton pour valider
button = Button(gui,text='Commencer !',command=intro)
button.grid(column=0,row=4,sticky='n')


# Bouton pour arrêter
quit = Button(gui,text='Quitter',command=gui.destroy)
quit.grid(column=0,row=5,sticky='n')


# Crédits
credits=Label(gui,text='\n\n\n\n\n\n\n\n\nRéalisé par Lana Linord et Nathan Bosy',
           font =('Segoe UI',8),
           bg='white')
credits.grid(column=0,row=6,sticky='s')



# Fonction pour maintenir l'interface ouverte en boucle
gui.mainloop()