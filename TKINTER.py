import tkinter as tk
from tkinter import messagebox
import os
from Export_docx import create_qcm

def generer_questionnaires():
    nombre_questionnaires = entree_nombre.get()
    
    # Vérifier si l'entrée est un nombre valide supérieur à 0
    if nombre_questionnaires.isdigit() and int(nombre_questionnaires) > 0:
        nombre_questionnaires = int(nombre_questionnaires)
        
        # Générer les questionnaires
        for i in range(nombre_questionnaires):
            # Modifier les noms de fichiers pour chaque questionnaire
            fichier_questions = f"QCM_Questions_{i + 1}.docx"
            fichier_reponses = f"QCM_Reponses_{i + 1}.docx"
            
            # appeler create_qcm pour générer un questionnaire
            create_qcm()  #génère réponses et questions
            
            # vérifier si les fichiers générés existent pour éviter les écrasements
            if os.path.exists("QCM_Questions.docx"):
                os.rename("QCM_Questions.docx", fichier_questions)
            if os.path.exists("QCM_Reponses.docx"):
                os.rename("QCM_Reponses.docx", fichier_reponses)
            
            # Ouvrir les fichiers dans Word
            try:
                if os.name == 'nt':  #système Windows
                    os.startfile(fichier_questions)
                    os.startfile(fichier_reponses)
            except Exception as e:
                messagebox.showwarning("Avertissement", f"Impossible d'ouvrir les fichiers : {e}")
        
        messagebox.showinfo("Succès", f"{nombre_questionnaires} questionnaire(s) généré(s) avec succès !")
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide de questionnaires.")

# Interface Tkinter
root = tk.Tk()
root.title("Générateur de Questionnaires")

# Centrer la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 200
largeur_ecran = root.winfo_screenwidth()
hauteur_ecran = root.winfo_screenheight()
x = (largeur_ecran // 2) - (largeur_fenetre // 2)
y = (hauteur_ecran // 2) - (hauteur_fenetre // 2)
root.geometry(f'{largeur_fenetre}x{hauteur_fenetre}+{x}+{y}')

tk.Label(root, text="Nombre de questionnaires:", bg="greenyellow").pack()
entree_nombre = tk.Entry(root)
entree_nombre.pack()

bouton_generer = tk.Button(root, text="Générer", command=generer_questionnaires, fg="red", relief=tk.RAISED)
bouton_generer.pack()

root.mainloop()