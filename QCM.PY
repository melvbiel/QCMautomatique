def poser_question(question, choix, bonne_reponse):
    print(question)
    for i, choix in enumerate(choix):
        print(f"{i + 1}. {choix}")
    reponse = int(input("Votre réponse (1-4): "))
    return reponse == bonne_reponse

def lancer_qcm():
    questions = [
        {
            "question": "Quelle est la capitale de la France ?",
            "choix": ["Paris", "Londres", "Berlin", "Madrid"],
            "bonne_reponse": 1
        },
        {
            "question": "Quelle est la couleur du ciel ?",
            "choix": ["Rouge", "Vert", "Bleu", "Jaune"],
            "bonne_reponse": 3
        }
    ]
    
    score = 0
    for q in questions:
        if poser_question(q["question"], q["choix"], q["bonne_reponse"]):
            print("Bonne réponse !")
            score += 1
        else:
            print("Mauvaise réponse.")
    
    print(f"Votre score final est de {score}/{len(questions)}")

if __name__ == "__main__":
    lancer_qcm()