# Sistema de Cadastro de Livros

Trabalho da **Atividade N3** da disciplina **Estrutura de Dados e Organização de Arquivos**.

- **Curso:** Análise e Desenvolvimento de Sistemas (ADS)
- **Aluno(a):** Matheus Teixeira Gomes
- **Professor(a):** Willian Hubiner
- **Linguagem:** Python 3

---

## 1. Descrição

Este programa é um sistema de cadastro de livros feito em Python, que funciona pelo terminal (modo texto). Ele permite cadastrar, alterar, excluir, pesquisar e listar livros. Os dados ficam salvos em um arquivo `JSON`, então continuam guardados depois que o programa é fechado.

Cada livro possui os campos:

| Campo    | Tipo   | Descrição                              |
|----------|--------|----------------------------------------|
| `id`     | número | Código único, gerado automaticamente   |
| `titulo` | texto  | Título do livro                        |
| `autor`  | texto  | Nome do autor                          |
| `ano`    | número | Ano de publicação                      |
| `genero` | texto  | Gênero do livro (ex.: Romance, Ficção) |

---

## 2. Requisitos da atividade

| Requisito                                   | Como foi feito                                                       |
|---------------------------------------------|----------------------------------------------------------------------|
| Incluir, alterar e excluir                  | Funções `incluir()`, `alterar()` e `excluir()`                       |
| Persistência de dados em JSON               | Funções `carregar_dados()` e `salvar_dados()` (arquivo `livros.json`) |
| Pesquisa por campos do tipo texto           | Função `pesquisar()` (título, autor ou gênero)                       |
| Listas ordenadas por 2 campos diferentes    | `listar_por_titulo()` (A-Z) e `listar_por_ano()` (crescente)         |

---

## 3. Como executar

1. Instale o **Python 3** (https://www.python.org/downloads/), se ainda não tiver.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto e execute:

```bash
python cadastro_livros.py
```

Em alguns computadores (Linux/Mac) o comando é `python3`:

```bash
python3 cadastro_livros.py
```

> Não é necessário instalar nenhuma biblioteca extra. O programa usa só `json` e `os`, que já vêm com o Python.

Na primeira execução o arquivo `livros.json` ainda não existe. Ele é criado automaticamente quando o primeiro livro é cadastrado.

---

## 4. Como usar (menu)

```
===== CADASTRO DE LIVROS =====
1 - Incluir livro
2 - Alterar livro
3 - Excluir livro
4 - Pesquisar livro
5 - Listar ordenado por título
6 - Listar ordenado por ano
0 - Sair
```

- **1 - Incluir:** pede título, autor, ano e gênero. O código (`id`) é gerado sozinho.
- **2 - Alterar:** pede o código do livro e mostra os dados atuais. Para manter um campo igual, basta apertar Enter sem digitar nada.
- **3 - Excluir:** pede o código, mostra o livro e pede confirmação (`s` ou `n`).
- **4 - Pesquisar:** o usuário escolhe o campo (título, autor ou gênero) e digita um texto. O programa mostra todos os livros que contêm esse texto, sem diferenciar maiúsculas de minúsculas. Exemplo: pesquisar `casm` encontra "Dom Casmurro".
- **5 - Listar por título:** mostra todos os livros em ordem alfabética (A-Z).
- **6 - Listar por ano:** mostra todos os livros do mais antigo para o mais novo.
- **0 - Sair:** encerra o programa.

---

## 5. Como o código funciona

O código está dividido em funções pequenas, cada uma com uma tarefa:

| Função                                  | O que faz                                                                  |
|-----------------------------------------|----------------------------------------------------------------------------|
| `carregar_dados()`                      | Lê o `livros.json` e devolve a lista de livros                             |
| `salvar_dados(livros)`                  | Grava a lista de livros no `livros.json`                                   |
| `gerar_id(livros)`                      | Calcula o próximo código (maior código existente + 1)                      |
| `buscar_por_id(livros, codigo)`         | Procura um livro pelo código                                               |
| `ler_ano()` / `ler_codigo()`            | Pedem um número ao usuário e repetem se ele digitar algo inválido          |
| `mostrar_livro()` / `mostrar_lista()`   | Mostram um livro ou uma lista de livros na tela                            |
| `incluir()`                             | Cadastra um novo livro                                                     |
| `alterar()`                             | Altera os dados de um livro                                                |
| `excluir()`                             | Remove um livro                                                            |
| `pesquisar()`                           | Busca livros por título, autor ou gênero                                   |
| `listar_por_titulo()`                   | Lista ordenada pelo título                                                 |
| `listar_por_ano()`                      | Lista ordenada pelo ano                                                    |
| `main()`                                | Mostra o menu e chama a função escolhida                                   |

### Estruturas de dados usadas

- **Lista (`list`):** guarda todos os livros cadastrados.
- **Dicionário (`dict`):** cada livro é um dicionário com os campos `id`, `titulo`, `autor`, `ano` e `genero`.

Exemplo de como a lista fica em memória:

```python
[
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "genero": "Romance"},
    {"id": 2, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977, "genero": "Romance"}
]
```

### Persistência em JSON

- Ao **iniciar** o programa, `carregar_dados()` lê o arquivo `livros.json` com `json.load()`.
- Depois de cada **inclusão, alteração ou exclusão**, `salvar_dados()` grava a lista inteira no arquivo com `json.dump()`.

Assim os dados nunca se perdem, mesmo que o programa seja fechado. Exemplo do arquivo `livros.json`:

```json
[
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899,
        "genero": "Romance"
    }
]
```

### Pesquisa

Para cada livro da lista, o programa verifica se o texto digitado está dentro do campo escolhido:

```python
if texto in livro[campo].lower():
    encontrados.append(livro)
```

O `.lower()` deixa tudo em minúsculo, para que "dom" e "Dom" funcionem do mesmo jeito.

### Ordenação

A ordenação usa a função `sorted()` do Python. Ela recebe uma função (`key`) que diz qual campo deve ser usado na comparação:

```python
sorted(livros, key=pegar_titulo)   # ordena por título
sorted(livros, key=pegar_ano)      # ordena por ano
```

O `sorted()` cria uma lista nova ordenada e não altera a lista original.

---

## 6. Estrutura do repositório

```
.
├── cadastro_livros.py   # código do programa
├── livros.json          # dados salvos (criado automaticamente)
└── README.md            # documentação
```

---

## 7. Exemplo de uso

```
===== CADASTRO DE LIVROS =====
Escolha uma opção: 1

--- Incluir livro ---
Título: Dom Casmurro
Autor: Machado de Assis
Ano de publicação: 1899
Gênero: Romance
Livro cadastrado com sucesso!
```

```
Escolha uma opção: 6

--- Livros ordenados por ano (do mais antigo ao mais novo) ---
Código: 1 | Título: Dom Casmurro | Autor: Machado de Assis | Ano: 1899 | Gênero: Romance
Código: 3 | Título: Angústia | Autor: Graciliano Ramos | Ano: 1936 | Gênero: Romance
Código: 2 | Título: A Hora da Estrela | Autor: Clarice Lispector | Ano: 1937 | Gênero: Romance
```

---

## 8. Conclusão

O trabalho reúne os conceitos vistos em sala: listas, dicionários, funções, leitura e escrita de arquivos, pesquisa e ordenação. O objetivo foi manter o código simples e fácil de entender.
