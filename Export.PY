from docx import Document

def create_qcm():
    # Créer un nouveau document Word
    doc = Document()

    # Ajouter un titre
    doc.add_heading('Questionnaire à Choix Multiples', 0)

    # Ajouter des questions et des choix
    questions = [
        {
            "question": "Quelle est la capitale de la France ?",
            "choices": ["A. Paris", "B. Londres", "C. Berlin", "D. Madrid"]
        },
        {
            "question": "Quelle est la couleur du ciel par temps clair ?",
            "choices": ["A. Bleu", "B. Vert", "C. Rouge", "D. Jaune"]
        },
        {
            "question": "Combien de continents y a-t-il sur Terre ?",
            "choices": ["A. 5", "B. 6", "C. 7", "D. 8"]
        }
    ]

    for q in questions:
        doc.add_paragraph(q["question"], style='List Number')
        for choice in q["choices"]:
            doc.add_paragraph(choice, style='List Bullet')

    # Enregistrer le document
    doc.save('QCM.docx')

if __name__ == "__main__":
    create_qcm()