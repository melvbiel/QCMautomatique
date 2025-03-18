import random
import tkinter as tk
from tkinter import messagebox

def lire_questionnaire(fichier):
    with open(fichier, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    questions = [] #stocks les questions et réponses sous forme de dictionnaire
    current_question = None #variable temporaire servant à traiter la question et ses réponses
    for line in lines:
        line = line.strip() #supprime les espaces blancs en début et fin de lignes
        if line:  #Si la ligne n'est pas vide
            if current_question is None:
                current_question = {'question': line, 'reponses': [], 'bonne_reponse': None} #liste contenant la question actuelle, la liste vide pour stocker ses réponses
            elif len(current_question['reponses']) == 4:
                numr = int(line)
                current_question['bonne_reponse'] = current_question['reponses'][numr-1]
            else:
                current_question['reponses'].append(line)
        else:  #Ligne vide indique la fin d'une question
            if current_question:
                questions.append(current_question)
                current_question = None
    if current_question:  #Ajouter la dernière question si le fichier ne se termine pas par une ligne vide
        questions.append(current_question)
    return questions

def selectionner_questions(questions, nombre):
    return random.sample(questions, nombre) #échantillon aléatoire sans remise

def melanger_reponses(questions):
    for question in questions:
        random.shuffle(question['reponses']) #mélange la liste des réponses possibles
        compteur = 0
        for reponse in question['reponses']:
            compteur += 1
            if reponse == question['bonne_reponse']:
                question['bonne_reponse_index'] = compteur  #Stocke le nouvel index correct
    return questions

def afficher_questionnaire(questions):
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        for j, reponse in enumerate(question['reponses'], 1):
            print(f"  {j}. {reponse}")
        print(f"  Bonne réponse : {question['bonne_reponse_index']}")
        print()

def generer_questionnaires():
    try:
        nombre_questionnaires = int(entree_nombre.get())
        for _ in range(nombre_questionnaires):
            questions_selectionnees = selectionner_questions(questions, 20)
            questions_melangees = melanger_reponses(questions_selectionnees)
            afficher_questionnaire(questions_melangees)
        messagebox.showinfo("Succès", f"{nombre_questionnaires} questionnaires générés avec succès!")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

# Interface Tkinter
root = tk.Tk()
root.title("Générateur de Questionnaires")

# Centrer la fenêtre
largeur_fenetre = 400  # Largeur de la fenêtre
hauteur_fenetre = 200  # Hauteur de la fenêtre

# Obtenir la largeur et la hauteur de l'écran
largeur_ecran = root.winfo_screenwidth()
hauteur_ecran = root.winfo_screenheight()

# Calculer la position x et y pour centrer la fenêtre
x = (largeur_ecran // 2) - (largeur_fenetre // 2)
y = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

# Définir la géométrie de la fenêtre
root.geometry(f'{largeur_fenetre}x{hauteur_fenetre}+{x}+{y}')

tk.Label(root, text="Nombre de questionnaires:",bg="greenyellow",).pack()
entree_nombre = tk.Entry(root)
entree_nombre.pack()

bouton_generer = tk.Button(root, text="Générer", command=generer_questionnaires,fg="red",relief=tk.RAISED)
bouton_generer.pack()

# Charger les questions
fichier_questionnaire = 'QCM_cinema.txt'
questions = lire_questionnaire(fichier_questionnaire)

root.mainloop()