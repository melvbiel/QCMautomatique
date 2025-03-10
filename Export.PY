def poser_question(question, choix, reponse_correcte):
    print(question)
    for i, choix in enumerate(choix):
        print(f"{i + 1}. {choix}")
    reponse = int(input("Votre réponse (1-4): "))
    return reponse == reponse_correcte

def main():
    score = 0
    questions = [
        ("Quelle est la capitale de la France ?", ["Paris", "Londres", "Berlin", "Madrid"], 1),
        ("Quelle est la couleur du ciel ?", ["Rouge", "Vert", "Bleu", "Jaune"], 3),
        ("Combien font 2 + 2 ?", ["3", "4", "5", "6"], 2),
        ("Quel est le plus grand océan ?", ["Atlantique", "Pacifique", "Indien", "Arctique"], 2)
    ]

    for question, choix, reponse_correcte in questions:
        if poser_question(question, choix, reponse_correcte):
            print("Bonne réponse !")
            score += 1
        else:
            print("Mauvaise réponse.")

    print(f"Votre score final est de {score} sur {len(questions)}.")

if __name__ == "__main__":
    main()