import random


def lire_questionnaire(fichier):
    with open(fichier, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    questions = [] #stocks les questions et réponses sous forme de dictionnaire
    current_question = None #variable temporaire servant à traiter la question et ses réponses
    for line in lines:
        line = line.strip() #supprime les espaces blanc en début et fin de lignes
        if line:  # Si la ligne n'est pas vide
            if current_question is None:
                current_question = {'question': line, 'reponses': []} #liste contenant la question actuelle et liste vide pour stocker ses réponses
            else:
                current_question['reponses'].append(line)
        else:  # Ligne vide indique la fin d'une question
            if current_question:
                questions.append(current_question)
                current_question = None
    if current_question:  # Ajouter la dernière question si le fichier ne se termine pas par une ligne vide
        questions.append(current_question)
    return questions

def selectionner_questions(questions, nombre=20):
    return random.sample(questions, nombre) #échantillon aléatoire sans remise

def melanger_reponses(questions):
    for question in questions:
        random.shuffle(question['reponses']) #mélange la liste des réponses possible
    return questions

def afficher_questionnaire(questions):
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        for j, reponse in enumerate(question['reponses'], 1):
            print(f"  {j}. {reponse}")
        print()

# Exemple d'utilisation
fichier_questionnaire = 'QCM_cinema.txt'
questions = lire_questionnaire(fichier_questionnaire)
questions_selectionnees = selectionner_questions(questions, 20)
questions_melangees = melanger_reponses(questions_selectionnees)
afficher_questionnaire(questions_melangees)