# Agregador de Anúncios de Emprego — Grupo 22

## Elementos
- Tiago Marcos
- Luís Belo

## Descrição
Protótipo inicial de uma aplicação que centraliza anúncios de emprego e permite pesquisar e filtrar ofertas por cargo, localização e área profissional.

**Nota:** as ofertas incluídas nesta primeira versão são fictícias e servem para testar as funcionalidades. A recolha automática de anúncios (scraping) será desenvolvida numa fase posterior, respeitando as regras dos sites consultados.

## Requisitos
- Python 3.10 ou superior
- Não são necessárias bibliotecas externas nesta versão inicial.

## Como executar
1. Instalar o Python 3.
2. Abrir um terminal na pasta do projeto.
3. Executar:
   ```bash
   python main.py
   ```

## Como executar os testes
Na pasta principal, executar:
```bash
python -m unittest discover -s tests -v
```

## Organização
- `main.py`: ponto de entrada e interação com o utilizador.
- `dados.py`: estrutura e carregamento dos dados de exemplo.
- `pesquisa.py`: pesquisa, filtros e apresentação dos resultados.
- `tests/test_pesquisa.py`: testes automatizados da pesquisa.

## Representação dos dados
Cada oferta é representada por um tuplo com os campos:
`(cargo, localização, área, empresa, requisitos, fonte, url)`

As ofertas são guardadas numa lista, que permite percorrer e filtrar os resultados.

## Limitações conhecidas
- Os dados são fictícios.
- Ainda não existe scraping nem gravação permanente em ficheiro.
- A interface atual é textual (terminal), não a interface gráfica apresentada nos slides.
- Os endereços `example.com` são exemplos e não correspondem a anúncios reais.

## Próximos passos
- Implementar recolha de dados de fontes autorizadas.
- Guardar e carregar ofertas através de CSV ou JSON.
- Ligar a lógica à interface gráfica.
- Melhorar validação e tratamento de erros.
