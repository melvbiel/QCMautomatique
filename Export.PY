import QCM
from docx import Document
from docx.shared import Inches, Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def format_paysage(doc):
    section = doc.sections[0]
    section.orientation = 1  # Paysage
    section.page_width, section.page_height = section.page_height, section.page_width
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    
    # Définir la mise en page en deux colonnes après le heading
    sectPr = section._sectPr
    cols = OxmlElement('w:cols')
    cols.set(qn('w:num'), '2')  # Deux colonnes
    cols.set(qn('w:space'), '720')  # Espacement entre les colonnes
    sectPr.append(cols)

def set_line_spacing(paragraph, spacing=1.15, before=0, after=0):
    p_pr = paragraph._element.get_or_add_pPr()
    spacing_elem = OxmlElement('w:spacing')
    spacing_elem.set(qn('w:line'), str(int(spacing * 240)))  # 1.15 interligne
    spacing_elem.set(qn('w:before'), str(before))  # Réduction espace avant
    spacing_elem.set(qn('w:after'), str(after))  # Réduction espace après
    p_pr.append(spacing_elem)

def create_qcm():
    questions = QCM.lire_questionnaire('QCM_cinema.txt')
    questions_selectionnees = QCM.selectionner_questions(questions, 20)
    questions_melangees = QCM.melanger_reponses(questions_selectionnees)
    
    doc_questions = Document()
    format_paysage(doc_questions)  # Format paysage
    doc_questions.add_heading('Questionnaire à Choix Multiples', 0)
    doc_questions.add_paragraph()  # Ajoute un espace après le titre pour éviter l'écrasement
    
    doc_reponses = Document()
    doc_reponses.add_heading('Réponses du Questionnaire', 0)
    
    reponses_text = []
    
    for index, q in enumerate(questions_melangees):
        p_question = doc_questions.add_paragraph()
        run_question = p_question.add_run(f"{index + 1}. {q['question']}")
        run_question.font.size = Pt(9)
        set_line_spacing(p_question, 1.15, before=10, after=10)
        
        for k, choice in enumerate(q['reponses'], 1):
            lettre = chr(96 + k)
            p = doc_questions.add_paragraph(style='List Bullet')
            run = p.add_run(f"{lettre}. {choice}")
            run.font.size = Pt(9)
            set_line_spacing(p, 1.15, before=5, after=5)
        
        doc_questions.add_paragraph()  # Ajout d'un saut de ligne après chaque question
        
        if q['bonne_reponse'] in q['reponses']:
            reponses_text.append(chr(96 + q['reponses'].index(q['bonne_reponse']) + 1))
    
    doc_reponses.add_paragraph("Réponses :")
    doc_reponses.add_paragraph(", ".join(reponses_text))
    
    doc_questions.save('QCM_Questions.docx')
    doc_reponses.save('QCM_Reponses.docx')

create_qcm()
print("Fichiers créés avec succès !")

