"""Dados e funções de carregamento de ofertas de emprego."""

# Cada oferta é representada por um tuplo com:
# (cargo, localização, área, empresa, requisitos, fonte, url)
Oferta = tuple


def carregar_ofertas_exemplo():
    """Devolve uma lista de ofertas de exemplo para testar a aplicação.

    Estes dados são fictícios e servem apenas para o protótipo inicial.
    """
    return [
        (
            "Programador Python júnior",
            "Beja",
            "Informática",
            "TechSul",
            ["Conhecimentos de Python", "Conhecimentos de SQL", "Git"],
            "Site de empregos A",
            "https://example.com/oferta-python",
        ),
        (
            "Técnico de redes",
            "Évora",
            "Informática",
            "NetAlentejo",
            ["Redes de computadores", "Noções de Linux"],
            "Site de empregos B",
            "https://example.com/oferta-redes",
        ),
        (
            "Designer UI/UX",
            "Remoto",
            "Design",
            "Criativa Lda",
            ["Portefólio", "Ferramentas de design"],
            "Site de empregos A",
            "https://example.com/oferta-design",
        ),
        (
            "Assistente administrativo",
            "Beja",
            "Administração",
            "Alentejo Serviços",
            ["Organização", "Conhecimentos de informática"],
            "Site de empregos C",
            "https://example.com/oferta-administrativo",
        ),
    ]


def validar_oferta(oferta):
    """Confirma se uma oferta tem os campos essenciais preenchidos."""
    if not isinstance(oferta, tuple) or len(oferta) != 7:
        return False

    cargo, localizacao, area, empresa, requisitos, fonte, url = oferta
    return all([cargo, localizacao, area, empresa, requisitos, fonte, url])
