"""Pesquisa, filtragem e apresentação de ofertas."""


def pesquisar_ofertas(ofertas, cargo="", localizacao="", area=""):
    """Filtra ofertas por cargo, localização e área, sem distinguir maiúsculas."""
    resultados = []

    for oferta in ofertas:
        nome_cargo, local, nome_area = oferta[0], oferta[1], oferta[2]

        if cargo and cargo.casefold() not in nome_cargo.casefold():
            continue
        if localizacao and localizacao.casefold() not in local.casefold():
            continue
        if area and area.casefold() not in nome_area.casefold():
            continue

        resultados.append(oferta)

    return resultados


def mostrar_ofertas(ofertas):
    """Mostra as ofertas encontradas no terminal."""
    if not ofertas:
        print("\nNão foram encontradas ofertas com esses critérios.")
        return

    print(f"\nForam encontradas {len(ofertas)} oferta(s):")
    for numero, oferta in enumerate(ofertas, start=1):
        cargo, local, area, empresa, requisitos, fonte, url = oferta
        print(f"\n{numero}. {cargo}")
        print(f"   Empresa: {empresa}")
        print(f"   Localização: {local} | Área: {area}")
        print(f"   Requisitos: {', '.join(requisitos)}")
        print(f"   Fonte: {fonte}")
        print(f"   Anúncio: {url}")
