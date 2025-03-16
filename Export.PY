import QCM
from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement, ns

def set_landscape(doc):
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
    set_landscape(doc_questions)  # Définir en paysage
    doc_questions.add_heading('Questionnaire à Choix Multiples', 0)
    
    table = doc_questions.add_table(rows=0, cols=2)
    table.autofit = True
    
    doc_reponses = Document()
    doc_reponses.add_heading('Réponses du Questionnaire', 0)
    
    reponses_text = []
    
    for i in range(0, len(questions_melangees), 5):
        row_cells = table.add_row().cells
        
        for col in range(2):
            if i + col * 5 < len(questions_melangees):
                q = questions_melangees[i + col * 5]
                question_text = f"{i + col * 5 + 1}. {q['question']}\n"
                for j, choice in enumerate(q['reponses'], 1):
                    lettre = chr(96 + j)  # Convertir 1 -> 'a', 2 -> 'b', etc.
                    question_text += f"{lettre}. {choice}\n"
                    if choice == q['bonne_reponse']:
                        reponses_text.append(lettre)
                row_cells[col].text = question_text
    
    doc_reponses.add_paragraph("Réponses :")
    doc_reponses.add_paragraph(", ".join(reponses_text))
    
    # Enregistrer les fichiers
    doc_questions.save('QCM_Questions.docx')
    doc_reponses.save('QCM_Reponses.docx')

create_qcm()
print("Fichiers créés avec succès.")

