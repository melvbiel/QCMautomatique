import QCM
from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement

def format_paysage(doc):
    section = doc.sections[0]
    section.orientation = 1  # Paysage
    section.page_width, section.page_height = section.page_height, section.page_width
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)

def create_qcm():
    questions = QCM.lire_questionnaire('QCM_cinema.txt')
    questions_selectionnees = QCM.selectionner_questions(questions, 20)
    questions_melangees = QCM.melanger_reponses(questions_selectionnees)
    
    # Créer le document pour l'élève
    doc_questions = Document()
    format_paysage(doc_questions)  # Définir en paysage
    doc_questions.add_heading('Questionnaire à Choix Multiples', 0)
    
    doc_reponses = Document()
    doc_reponses.add_heading('Réponses du Questionnaire', 0)
    
    reponses_text = []
    
    for i, q in enumerate(questions_melangees, 1):
        p_question = doc_questions.add_paragraph()
        run_question = p_question.add_run(f"{i}. {q['question']}")
        run_question.font.size = Pt(9)  # Définir la taille de la police à 9 points pour les questions
        
        for j, choice in enumerate(q['reponses'], 1):
            lettre = chr(96 + j)  # Convertir 1 -> 'a', 2 -> 'b', etc.
            p = doc_questions.add_paragraph()
            run = p.add_run(f"□ {lettre}. {choice}")
            run.font.size = Pt(9)  # Définir la taille de la police à 9 points pour les réponses
            p.paragraph_format.left_indent = Inches(0.25)  # Ajouter un alinéa
            
            if choice == q['bonne_reponse']:
                reponses_text.append(lettre)
    
    doc_reponses.add_paragraph("Réponses :")
    doc_reponses.add_paragraph(", ".join(reponses_text))
    
    # Enregistrer les fichiers
    doc_questions.save('QCM_Questions.docx')
    doc_reponses.save('QCM_Reponses.docx')

create_qcm()
print("Fichiers créés avec succès !")