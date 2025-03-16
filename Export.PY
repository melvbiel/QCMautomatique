import QCM
from docx import Document

def create_qcm():
    # Créer un nouveau document Word
    doc = Document()

    # Ajouter un titre
    doc.add_heading('Questionnaire à Choix Multiples', 0)

    # Ajouter des questions et des choix
   

    for q in questions:
        doc.add_paragraph(q["question"], style='List Number')
        for choice in q["choices"]:
            doc.add_paragraph(choice, style='List Bullet')

    for q in questions2:
        doc.add_paragraph(q["question"], style='List Number')
        for choice in q["choices"]:
            doc.add_paragraph(choice, style='List Bullet')
    
    for q in questions3:
        doc.add_paragraph(q["question"], style='List Number')
        for choice in q["choices"]:
            doc.add_paragraph(choice, style='List Bullet')

    # Enregistrer le document
    doc.save('QCM.docx')


create_qcm()
# Pour créer le fichier taper dans le terminal: python Export.PY