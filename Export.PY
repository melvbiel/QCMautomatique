import QCM
from docx import Document
from docx.shared import Inches, Pt

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
    
    doc_questions = Document()
    format_paysage(doc_questions)  # Format paysage
    doc_questions.add_heading('Questionnaire à Choix Multiples', 0)
    
    doc_reponses = Document()
    doc_reponses.add_heading('Réponses du Questionnaire', 0)
    
    reponses_text = []
    table = doc_questions.add_table(rows=10, cols=2)
    table.autofit = False
    
    col_width = Inches(3.0)
    spacing = Inches(1.5)
    
    for row in table.rows:
        row.cells[0].width = col_width
        row.cells[1].width = col_width
        row.cells[1].paragraphs[0].add_run("\t" * 5)  # Ajout d'un espace entre les colonnes
    
    for i in range(10):  # 10 lignes par page (2 colonnes, total 20 questions)
        for j in range(2):  # 2 colonnes
            index = i + j * 10  # Placement des questions en quinconce
            if index < len(questions_melangees):
                q = questions_melangees[index]
                cell = table.cell(i, j)
                p_question = cell.add_paragraph()
                run_question = p_question.add_run(f"{index + 1}. {q['question']}")
                run_question.font.size = Pt(9)
                
                for k, choice in enumerate(q['reponses'], 1):
                    lettre = chr(96 + k)
                    p = cell.add_paragraph()
                    run = p.add_run(f"□ {lettre}. {choice}")
                    run.font.size = Pt(9)
                    p.paragraph_format.left_indent = Inches(0.25)
                    
                    if choice == q['bonne_reponse']:
                        reponses_text.append(lettre)
    
    doc_reponses.add_paragraph("Réponses :")
    doc_reponses.add_paragraph(", ".join(reponses_text))
    
    doc_questions.save('QCM_Questions.docx')
    doc_reponses.save('QCM_Reponses.docx')

create_qcm()
print("Fichiers créés avec succès !")
