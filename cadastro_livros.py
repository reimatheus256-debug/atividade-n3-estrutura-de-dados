# Atividade N3 - Estrutura de Dados e Organização de Arquivos
# Sistema de cadastro de livros (incluir, alterar, excluir, pesquisar e listar)
# Os dados ficam salvos em um arquivo JSON.

import json
import os

# Nome do arquivo onde os dados serão guardados
ARQUIVO = "livros.json"


# ---------------------------------------------------------------
# PERSISTÊNCIA (JSON)
# ---------------------------------------------------------------

def carregar_dados():
    """Lê o arquivo JSON e devolve a lista de livros.
    Se o arquivo ainda não existe, devolve uma lista vazia."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_dados(livros):
    """Grava a lista de livros no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)


# ---------------------------------------------------------------
# FUNÇÕES AUXILIARES
# ---------------------------------------------------------------

def gerar_id(livros):
    """Gera um código novo: o maior código existente + 1."""
    maior = 0
    for livro in livros:
        if livro["id"] > maior:
            maior = livro["id"]
    return maior + 1


def buscar_por_id(livros, codigo):
    """Procura um livro pelo código. Devolve o livro ou None."""
    for livro in livros:
        if livro["id"] == codigo:
            return livro
    return None


def ler_ano():
    """Pede o ano até o usuário digitar um número válido."""
    while True:
        ano = input("Ano de publicação: ")
        if ano.isdigit():
            return int(ano)
        print("Ano inválido! Digite apenas números.")


def ler_codigo():
    """Pede um código até o usuário digitar um número válido."""
    while True:
        codigo = input("Digite o código do livro: ")
        if codigo.isdigit():
            return int(codigo)
        print("Código inválido! Digite apenas números.")


def mostrar_livro(livro):
    """Mostra os dados de um livro na tela."""
    print(f"Código: {livro['id']} | Título: {livro['titulo']} | "
          f"Autor: {livro['autor']} | Ano: {livro['ano']} | "
          f"Gênero: {livro['genero']}")


def mostrar_lista(livros):
    """Mostra todos os livros de uma lista."""
    if len(livros) == 0:
        print("Nenhum livro encontrado.")
    else:
        for livro in livros:
            mostrar_livro(livro)


# ---------------------------------------------------------------
# 1) INCLUIR
# ---------------------------------------------------------------

def incluir(livros):
    print("\n--- Incluir livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = ler_ano()
    genero = input("Gênero: ")

    # Cada livro é um dicionário
    livro = {
        "id": gerar_id(livros),
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "genero": genero
    }

    livros.append(livro)
    salvar_dados(livros)
    print("Livro cadastrado com sucesso!")


# ---------------------------------------------------------------
# 2) ALTERAR
# ---------------------------------------------------------------

def alterar(livros):
    print("\n--- Alterar livro ---")
    codigo = ler_codigo()
    livro = buscar_por_id(livros, codigo)

    if livro is None:
        print("Livro não encontrado.")
        return

    print("Dados atuais:")
    mostrar_livro(livro)
    print("(Deixe em branco e aperte Enter para manter o valor atual)")

    titulo = input("Novo título: ")
    if titulo != "":
        livro["titulo"] = titulo

    autor = input("Novo autor: ")
    if autor != "":
        livro["autor"] = autor

    ano = input("Novo ano: ")
    if ano != "":
        if ano.isdigit():
            livro["ano"] = int(ano)
        else:
            print("Ano inválido, o ano não foi alterado.")

    genero = input("Novo gênero: ")
    if genero != "":
        livro["genero"] = genero

    salvar_dados(livros)
    print("Livro alterado com sucesso!")


# ---------------------------------------------------------------
# 3) EXCLUIR
# ---------------------------------------------------------------

def excluir(livros):
    print("\n--- Excluir livro ---")
    codigo = ler_codigo()
    livro = buscar_por_id(livros, codigo)

    if livro is None:
        print("Livro não encontrado.")
        return

    mostrar_livro(livro)
    resposta = input("Tem certeza que deseja excluir? (s/n): ")

    if resposta.lower() == "s":
        livros.remove(livro)
        salvar_dados(livros)
        print("Livro excluído com sucesso!")
    else:
        print("Exclusão cancelada.")


# ---------------------------------------------------------------
# 4) PESQUISAR POR CAMPO DE TEXTO
# ---------------------------------------------------------------

def pesquisar(livros):
    print("\n--- Pesquisar livro ---")
    print("1 - Pesquisar por título")
    print("2 - Pesquisar por autor")
    print("3 - Pesquisar por gênero")
    opcao = input("Escolha o campo: ")

    if opcao == "1":
        campo = "titulo"
    elif opcao == "2":
        campo = "autor"
    elif opcao == "3":
        campo = "genero"
    else:
        print("Opção inválida.")
        return

    texto = input("Digite o texto a pesquisar: ").lower()

    encontrados = []
    for livro in livros:
        # Verifica se o texto digitado está dentro do campo
        # (tudo em minúsculo para não diferenciar maiúsculas de minúsculas)
        if texto in livro[campo].lower():
            encontrados.append(livro)

    print(f"\n{len(encontrados)} livro(s) encontrado(s):")
    mostrar_lista(encontrados)


# ---------------------------------------------------------------
# 5) LISTAS ORDENADAS (por 2 campos diferentes)
# ---------------------------------------------------------------

def pegar_titulo(livro):
    """Devolve o título em minúsculo (usado para ordenar por título)."""
    return livro["titulo"].lower()


def pegar_ano(livro):
    """Devolve o ano (usado para ordenar por ano)."""
    return livro["ano"]


def listar_por_titulo(livros):
    print("\n--- Livros ordenados por título (A-Z) ---")
    lista_ordenada = sorted(livros, key=pegar_titulo)
    mostrar_lista(lista_ordenada)


def listar_por_ano(livros):
    print("\n--- Livros ordenados por ano (do mais antigo ao mais novo) ---")
    lista_ordenada = sorted(livros, key=pegar_ano)
    mostrar_lista(lista_ordenada)


# ---------------------------------------------------------------
# MENU PRINCIPAL
# ---------------------------------------------------------------

def mostrar_menu():
    print("\n===== CADASTRO DE LIVROS =====")
    print("1 - Incluir livro")
    print("2 - Alterar livro")
    print("3 - Excluir livro")
    print("4 - Pesquisar livro")
    print("5 - Listar ordenado por título")
    print("6 - Listar ordenado por ano")
    print("0 - Sair")


def main():
    # Ao iniciar, carrega os dados que já estavam salvos no JSON
    livros = carregar_dados()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir(livros)
        elif opcao == "2":
            alterar(livros)
        elif opcao == "3":
            excluir(livros)
        elif opcao == "4":
            pesquisar(livros)
        elif opcao == "5":
            listar_por_titulo(livros)
        elif opcao == "6":
            listar_por_ano(livros)
        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Inicia o programa
main()
