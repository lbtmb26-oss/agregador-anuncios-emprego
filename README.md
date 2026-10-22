# Agregador de Anúncios de Emprego

## Projeto de Avaliação — Linguagens de Programação 2026/2027

**Grupo:** 22

**Elementos do grupo:**
- Tiago Marcos — 25252
- Luís Belo — 25793

---

## 1. Descrição do projeto

Aplicação em Python que **junta anúncios de emprego de várias fontes** num só sítio.

As ofertas de emprego estão espalhadas por várias plataformas, o que torna a pesquisa lenta e repetitiva
e dificulta a comparação entre ofertas. Com esta aplicação, o utilizador consulta todas as ofertas no mesmo
local e encontra mais depressa as que lhe interessam.

Os anúncios serão recolhidos automaticamente da Web (scraping) e guardados em ficheiro.

---

## 2. Funcionalidades

- Pesquisar ofertas por **cargo**;
- Filtrar ofertas por **localização**;
- Filtrar ofertas por **área profissional**;
- Consultar os **detalhes** de uma oferta (empresa, fonte, descrição);
- Consultar os **requisitos** da vaga e abrir o **anúncio original**.

---

## 3. Interface

A aplicação terá uma **interface gráfica para computador**, feita com **Tkinter**.
Os ecrãs foram desenhados no **Figma**.

### Ecrã de pesquisa

Caixa de pesquisa por cargo, filtros de localização e área, e lista das ofertas recentes.

![Ecrã de pesquisa](docs/ecra_pesquisa.png)

### Detalhe da vaga

Aparece ao carregar em **Ver detalhes**. Mostra a localização, a área, a fonte, a descrição, os requisitos
e um botão para abrir o anúncio original.

![Detalhe da vaga](docs/ecra_detalhe.png)

---

## 4. Estrutura dos dados

Cada oferta é representada por um **tuplo**, porque os dados de uma oferta não mudam depois de recolhidos
e a ordem dos campos é sempre a mesma:

```text
(cargo, localização, área, empresa, requisitos, fonte)
```

Os requisitos também são um tuplo, porque uma vaga pode ter vários.

Todas as ofertas ficam guardadas numa **lista**, que é percorrida com ciclos `for` e filtrada com
condições `if`:

```python
ofertas = [
    ("Programador Python júnior", "Beja", "Informática", "TechSul",
     ("Python", "SQL", "Git"), "Site de empregos A"),
    ...
]
```

Os dados de exemplo estão no ficheiro `dados.py`.

---

## 5. Organização do código

```text
Anuncios-de-emprego/
│
├── main.py
├── dados.py
├── pesquisa.py
├── empregos.py
├── docs/
│   ├── ecra_pesquisa.png
│   └── ecra_detalhe.png
├── README.md
└── requirements.txt
```

| Ficheiro | Responsabilidade |
|---|---|
| `main.py` | Arranque da aplicação e interface gráfica |
| `dados.py` | Ofertas de exemplo (mais tarde, leitura e escrita em CSV/JSON) |
| `pesquisa.py` | Pesquisa por cargo e filtros por localização e área |
| `empregos.py` | Listagem das ofertas e consulta dos detalhes |

---

## 6. Fluxo da aplicação

```text
Fontes de anúncios (sites de emprego)
        ↓
Recolha automática (scraping)
        ↓
Guardar em ficheiro
        ↓
Pesquisa / filtragem
        ↓
Lista de resultados
        ↓
Detalhe da oferta
```

---

## 7. Tecnologias

- **Python 3**
- **Tkinter** — interface gráfica (já incluído no Python)
- **Git / GitHub** — controlo de versões
- **Figma** — desenho dos ecrãs

---

## 8. Instalação e execução

É necessário ter o **Python 3** instalado.

```bash
git clone https://github.com/TitigamerYT/Anuncios-de-emprego.git
cd Anuncios-de-emprego
python main.py
```

Nesta fase não há dependências externas. As bibliotecas usadas no scraping serão adicionadas ao
`requirements.txt`.

---

## 9. Riscos e dificuldades previstas

| Risco | Solução |
|---|---|
| Limites e bloqueios dos sites | Pausas entre pedidos e respeito pelo `robots.txt` |
| Mudanças na estrutura HTML dos sites | Tratamento de exceções (`try/except`) |
| Anúncios com dados em falta | Valor por omissão: "Não indicado" |
| Falhas de internet | Cópia dos dados guardada em ficheiro local |

---

## 10. Planeamento

| Entrega | Data | Conteúdo |
|---|---|---|
| Entrega intermédia 1 | 22 de outubro | Proposta, estrutura dos dados, desenho dos ecrãs e repositório |
| Entrega intermédia 2 | 17 de dezembro | Protótipo com scraping, ficheiros CSV/JSON, validações e testes |
| Entrega final | 13 de janeiro | Aplicação completa, código revisto e documentação |

---

## 11. Estado atual

**Entrega Intermédia 1** — proposta e desenho da solução.

Já existe o esqueleto do código e os dados de exemplo. As funções ainda não estão implementadas.
