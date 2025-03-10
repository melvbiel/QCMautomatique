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
        },
        {
            "question": "Quelle est la plus grande planète du système solaire ?",
            "choices": ["A. Terre", "B. Mars", "C. Jupiter", "D. Saturne"]
        },
        {
            "question": "Quelle est la langue officielle du Brésil ?",
            "choices": ["A. Espagnol", "B. Portugais", "C. Anglais", "D. Français"]
        },
        {
            "question": "Quel est l'élément chimique dont le symbole est O ?",
            "choices": ["A. Or", "B. Oxygène", "C. Osmium", "D. Oganesson"]
        },
        {
            "question": "Quelle est la monnaie utilisée au Japon ?",
            "choices": ["A. Yuan", "B. Dollar", "C. Yen", "D. Won"]
        },
        {
            "question": "Quel est le plus grand océan de la Terre ?",
            "choices": ["A. Atlantique", "B. Indien", "C. Arctique", "D. Pacifique"]
        },
        {
            "question": "Quelle est la vitesse de la lumière ?",
            "choices": ["A. 300 000 km/s", "B. 150 000 km/s", "C. 450 000 km/s", "D. 600 000 km/s"]
        },
        {
            "question": "Qui a peint la Joconde ?",
            "choices": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Léonard de Vinci", "D. Claude Monet"]
        },
        {
            "question": "Quelle est la capitale de l'Australie ?",
            "choices": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"]
        },
        {
            "question": "Quel est le plus long fleuve du monde ?",
            "choices": ["A. Amazone", "B. Nil", "C. Yangtsé", "D. Mississippi"]
        },
        {
            "question": "Quelle est la plus haute montagne du monde ?",
            "choices": ["A. K2", "B. Kangchenjunga", "C. Lhotse", "D. Everest"]
        },
        {
            "question": "Quel est le symbole chimique de l'eau ?",
            "choices": ["A. H2O", "B. CO2", "C. O2", "D. H2"]
        },
        {
            "question": "Quelle est la capitale de l'Italie ?",
            "choices": ["A. Rome", "B. Milan", "C. Naples", "D. Venise"]
        },
        {
            "question": "Quel est le plus grand désert du monde ?",
            "choices": ["A. Sahara", "B. Gobi", "C. Kalahari", "D. Antarctique"]
        },
        {
            "question": "Quelle est la capitale de l'Espagne ?",
            "choices": ["A. Barcelone", "B. Madrid", "C. Séville", "D. Valence"]
        },
        {
            "question": "Quel est le plus grand pays du monde par superficie ?",
            "choices": ["A. Canada", "B. Chine", "C. États-Unis", "D. Russie"]
        },
        {
            "question": "Quelle est la capitale de l'Allemagne ?",
            "choices": ["A. Munich", "B. Francfort", "C. Berlin", "D. Hambourg"]
        },
        {
            "question": "Quel est le plus petit pays du monde ?",
            "choices": ["A. Monaco", "B. Vatican", "C. Nauru", "D. Saint-Marin"]
        },
    ]
    questions2 = [
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
        },
        {
            "question": "Quelle est la plus grande planète du système solaire ?",
            "choices": ["A. Terre", "B. Mars", "C. Jupiter", "D. Saturne"]
        },
        {
            "question": "Quelle est la langue officielle du Brésil ?",
            "choices": ["A. Espagnol", "B. Portugais", "C. Anglais", "D. Français"]
        },
        {
            "question": "Quel est l'élément chimique dont le symbole est O ?",
            "choices": ["A. Or", "B. Oxygène", "C. Osmium", "D. Oganesson"]
        },
        {
            "question": "Quelle est la monnaie utilisée au Japon ?",
            "choices": ["A. Yuan", "B. Dollar", "C. Yen", "D. Won"]
        },
        {
            "question": "Quel est le plus grand océan de la Terre ?",
            "choices": ["A. Atlantique", "B. Indien", "C. Arctique", "D. Pacifique"]
        },
        {
            "question": "Quelle est la vitesse de la lumière ?",
            "choices": ["A. 300 000 km/s", "B. 150 000 km/s", "C. 450 000 km/s", "D. 600 000 km/s"]
        },
        {
            "question": "Qui a peint la Joconde ?",
            "choices": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Léonard de Vinci", "D. Claude Monet"]
        },
        {
            "question": "Quelle est la capitale de l'Australie ?",
            "choices": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"]
        },
        {
            "question": "Quel est le plus long fleuve du monde ?",
            "choices": ["A. Amazone", "B. Nil", "C. Yangtsé", "D. Mississippi"]
        },
        {
            "question": "Quelle est la plus haute montagne du monde ?",
            "choices": ["A. K2", "B. Kangchenjunga", "C. Lhotse", "D. Everest"]
        },
        {
            "question": "Quel est le symbole chimique de l'eau ?",
            "choices": ["A. H2O", "B. CO2", "C. O2", "D. H2"]
        },
        {
            "question": "Quelle est la capitale de l'Italie ?",
            "choices": ["A. Rome", "B. Milan", "C. Naples", "D. Venise"]
        },
        {
            "question": "Quel est le plus grand désert du monde ?",
            "choices": ["A. Sahara", "B. Gobi", "C. Kalahari", "D. Antarctique"]
        },
        {
            "question": "Quelle est la capitale de l'Espagne ?",
            "choices": ["A. Barcelone", "B. Madrid", "C. Séville", "D. Valence"]
        },
        {
            "question": "Quel est le plus grand pays du monde par superficie ?",
            "choices": ["A. Canada", "B. Chine", "C. États-Unis", "D. Russie"]
        },
        {
            "question": "Quelle est la capitale de l'Allemagne ?",
            "choices": ["A. Munich", "B. Francfort", "C. Berlin", "D. Hambourg"]
        },
        {
            "question": "Quel est le plus petit pays du monde ?",
            "choices": ["A. Monaco", "B. Vatican", "C. Nauru", "D. Saint-Marin"]
        },
    ]
    questions3 = [
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
        },
        {
            "question": "Quelle est la plus grande planète du système solaire ?",
            "choices": ["A. Terre", "B. Mars", "C. Jupiter", "D. Saturne"]
        },
        {
            "question": "Quelle est la langue officielle du Brésil ?",
            "choices": ["A. Espagnol", "B. Portugais", "C. Anglais", "D. Français"]
        },
        {
            "question": "Quel est l'élément chimique dont le symbole est O ?",
            "choices": ["A. Or", "B. Oxygène", "C. Osmium", "D. Oganesson"]
        },
        {
            "question": "Quelle est la monnaie utilisée au Japon ?",
            "choices": ["A. Yuan", "B. Dollar", "C. Yen", "D. Won"]
        },
        {
            "question": "Quel est le plus grand océan de la Terre ?",
            "choices": ["A. Atlantique", "B. Indien", "C. Arctique", "D. Pacifique"]
        },
        {
            "question": "Quelle est la vitesse de la lumière ?",
            "choices": ["A. 300 000 km/s", "B. 150 000 km/s", "C. 450 000 km/s", "D. 600 000 km/s"]
        },
        {
            "question": "Qui a peint la Joconde ?",
            "choices": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Léonard de Vinci", "D. Claude Monet"]
        },
        {
            "question": "Quelle est la capitale de l'Australie ?",
            "choices": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"]
        },
        {
            "question": "Quel est le plus long fleuve du monde ?",
            "choices": ["A. Amazone", "B. Nil", "C. Yangtsé", "D. Mississippi"]
        },
        {
            "question": "Quelle est la plus haute montagne du monde ?",
            "choices": ["A. K2", "B. Kangchenjunga", "C. Lhotse", "D. Everest"]
        },
        {
            "question": "Quel est le symbole chimique de l'eau ?",
            "choices": ["A. H2O", "B. CO2", "C. O2", "D. H2"]
        },
        {
            "question": "Quelle est la capitale de l'Italie ?",
            "choices": ["A. Rome", "B. Milan", "C. Naples", "D. Venise"]
        },
        {
            "question": "Quel est le plus grand désert du monde ?",
            "choices": ["A. Sahara", "B. Gobi", "C. Kalahari", "D. Antarctique"]
        },
        {
            "question": "Quelle est la capitale de l'Espagne ?",
            "choices": ["A. Barcelone", "B. Madrid", "C. Séville", "D. Valence"]
        },
        {
            "question": "Quel est le plus grand pays du monde par superficie ?",
            "choices": ["A. Canada", "B. Chine", "C. États-Unis", "D. Russie"]
        },
        {
            "question": "Quelle est la capitale de l'Allemagne ?",
            "choices": ["A. Munich", "B. Francfort", "C. Berlin", "D. Hambourg"]
        },
        {
            "question": "Quel est le plus petit pays du monde ?",
            "choices": ["A. Monaco", "B. Vatican", "C. Nauru", "D. Saint-Marin"]
        },
    ]

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