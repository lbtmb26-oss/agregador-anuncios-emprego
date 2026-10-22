"""Ponto de entrada do Agregador de Anúncios de Emprego."""
from dados import carregar_ofertas_exemplo
from pesquisa import pesquisar_ofertas, mostrar_ofertas


def main():
    ofertas = carregar_ofertas_exemplo()

    print("\n=== Agregador de Anúncios de Emprego ===")
    cargo = input("Cargo (Enter para não filtrar): ").strip()
    localizacao = input("Localização (Enter para não filtrar): ").strip()
    area = input("Área profissional (Enter para não filtrar): ").strip()

    resultados = pesquisar_ofertas(
        ofertas,
        cargo=cargo,
        localizacao=localizacao,
        area=area,
    )

    mostrar_ofertas(resultados)


if __name__ == "__main__":
    main()
