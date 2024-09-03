# importar módulo O.S. para limpeza da tela 
import os

# Menu de opções 
menu = """
    [0] - Desistir da travessia
    [1] - Posição atual do Amostradinho
    [2] - Caminhar
    [3] - Girar para esquerda
    [4] - Girar para a direita
    [5] - Direção do Amostradinho
"""

colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
linhas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
direcoes = ["Norte", "Leste", "Sul", "Oeste"]

# posição de coluna do Amostradinho
col_amostradinho = "A"
# posição de linha do Amostradinho
lin_amostradinho = 3
# direção de caminhada do Amostradinho
dir_amostradinho = "Leste"



def girar_direita():
    global dir_amostradinho

    if dir_amostradinho == "Leste":        
        dir_amostradinho = "Sul"
        
    elif dir_amostradinho == "Oeste":
        dir_amostradinho = "Norte"

    elif dir_amostradinho == "Norte":        
        dir_amostradinho = "Leste"

    else: 
        dir_amostradinho = "Oeste"



def girar_esquerda():
    global dir_amostradinho

    if dir_amostradinho == "Leste":        
        dir_amostradinho = "Norte"
        
    elif dir_amostradinho == "Oeste":
        dir_amostradinho = "Sul"

    elif dir_amostradinho == "Norte":        
        dir_amostradinho = "Oeste"

    else: 
        dir_amostradinho = "Leste"



def processar_caminho(coluna, linha) -> tuple:

    col_indice = colunas.index(coluna)
    lin_indice = linhas.index(linha)

    if dir_amostradinho == "Leste":        
        coluna = colunas[col_indice + 1]

    if dir_amostradinho == "Oeste":
        coluna = colunas[col_indice - 1]        

    if dir_amostradinho == "Norte":        
        linha = linhas[lin_indice - 1]

    if dir_amostradinho == "Sul":
        linha = linhas[lin_indice + 1]

    return coluna, linha



def caminhar_para()->str:
    global col_amostradinho
    global lin_amostradinho
    nova_posicao = processar_caminho(col_amostradinho, lin_amostradinho)
    mensagem = f"Caminhar de {col_amostradinho}{lin_amostradinho} para {nova_posicao[0]}{nova_posicao[1]}"
    col_amostradinho = nova_posicao[0]
    lin_amostradinho = nova_posicao[1]
    return mensagem




# laço de repetição infinito
while(True): 
    # faz a limpeza da tela
    os.system("cls")

    # imprime o menu de opções
    print(f"\n{menu}\n")

    # captura a resposta do usuário
    resposta = input("Selecione uma opção: ")

    # testa a resposta do usuário
    # se resposta for igual a zero
    if resposta == "0":
        # faz a limpeza da tela
        os.system("cls")
        # imprime mensagem de desistência
        print("Desistindo da travessia! :(")
        print() # print vazio para pular uma linha
        # interrompe o loop infinito
        break

    # se resposta for igual a 1 
    elif resposta == "1":
        print() # print vazio para pular uma linha
        posicao_amostradinho = f"\t Posição: {col_amostradinho}{lin_amostradinho}"
        print(posicao_amostradinho)
        input("") # Input vazio para fazer leitura da mensagem impressa

    # se resposta for igual a 2
    elif resposta == "2":
        print() # print vazio para pular uma linha
        print(caminhar_para())
        input("") # Input vazio para fazer leitura da mensagem impressa

    # se resposta for igual a 3
    elif resposta == "3":
        print() # print vazio para pular uma linha
        girar_esquerda()
        nova_direcao = f"\t Nova direção: {dir_amostradinho}"
        print(nova_direcao)
        input("") # Input vazio para fazer leitura da mensagem impressa

    # se resposta for igual a 4
    elif resposta == "4":
        print() # print vazio para pular uma linha
        girar_direita()
        nova_direcao = f"\t Nova direção: {dir_amostradinho}"
        print(nova_direcao)
        input("") # Input vazio para fazer leitura da mensagem impressa

    # se resposta for igual a 5
    elif resposta == "5":
        print() # print vazio para pular uma linha
        direcao_amostradinho = f"\t Direção: {dir_amostradinho}"
        print(direcao_amostradinho)
        input("") # Input vazio para fazer leitura da mensagem impressa

    # para nenhuma das opções disponíveis
    else:
        print() # print vazio para pular uma linha
        print("\nOpção inválida")
        input("") # Input vazio para fazer leitura da mensagem impressa