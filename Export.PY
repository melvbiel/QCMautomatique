import QCM
from docx import Document

def create_qcm():
    questions = QCM.lire_questionnaire('QCM_cinema.txt')
    questions_selectionnees = QCM.selectionner_questions(questions, 20)
    questions_melangees = QCM.melanger_reponses(questions_selectionnees)
    
    # Créer le document pour l'élève
    doc_questions = Document()
    doc_questions.add_heading('Questionnaire à Choix Multiples', 0)
    
    doc_reponses = Document()
    doc_reponses.add_heading('Réponses du Questionnaire', 0)
    
    reponses_text = []
    
    for i, q in enumerate(questions_melangees, 1):
        doc_questions.add_paragraph(f"{i}. {q['question']}", style='List Number')
        for j, choice in enumerate(q['reponses'], 1):
            lettre = chr(96 + j)  # Convertir 1 -> 'a', 2 -> 'b', etc.
            doc_questions.add_paragraph(f"{lettre}. {choice}", style='List Bullet')
            
            if choice == q['bonne_reponse']:
                reponses_text.append(lettre)
    
    doc_reponses.add_paragraph("Réponses :")
    doc_reponses.add_paragraph(", ".join(reponses_text))
    
    # Enregistrer les fichiers
    doc_questions.save('QCM_Questions.docx')
    doc_reponses.save('QCM_Reponses.docx')

create_qcm() # Pour créer le fichier taper dans le terminal: python Export.PY
