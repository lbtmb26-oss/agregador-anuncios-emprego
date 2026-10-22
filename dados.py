"""
dados.py

Dados utilizados pela aplicação.

Cada oferta é um tuplo:
    (cargo, localizacao, area, empresa, requisitos, fonte)

Todas as ofertas ficam numa lista.
Nesta fase são dados de exemplo; mais tarde virão do scraping e de ficheiros CSV/JSON.
"""

OFERTAS = [
    ("Programador Python júnior", "Beja", "Informática", "TechSul",
     ("Python", "SQL", "Git"), "Site de empregos A"),

    ("Técnico de redes", "Évora", "Informática", "NetAlentejo",
     ("Redes", "Cisco"), "Site de empregos B"),

    ("Designer UI/UX", "Remoto", "Design", "Criativa Lda",
     ("Figma", "Portefólio"), "Site de empregos C"),

    ("Assistente administrativo", "Beja", "Administração", "Alentejo Serviços",
     ("12.º ano", "Informática na ótica do utilizador"), "Site de empregos A"),
]
