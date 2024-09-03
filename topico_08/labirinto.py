
import os

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


col_amostradinho = "A"

lin_amostradinho = 3

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





while(True): 

    os.system("cls")

    print(f"\n{menu}\n")

    resposta = input("Selecione uma opção: ")

    if resposta == "0":

        os.system("cls")

        print("Desistindo da travessia! :(")
        print() 
        break


    elif resposta == "1":
        print() 
        posicao_amostradinho = f"\t Posição: {col_amostradinho}{lin_amostradinho}"
        print(posicao_amostradinho)
        input("")

   
    elif resposta == "2":
        print() 
        print(caminhar_para())
        input("")

    
    elif resposta == "3":
        print() 
        girar_esquerda()
        nova_direcao = f"\t Nova direção: {dir_amostradinho}"
        print(nova_direcao)
        input("")

    
    elif resposta == "4":
        print() 
        girar_direita()
        nova_direcao = f"\t Nova direção: {dir_amostradinho}"
        print(nova_direcao)
        input("")

    
    elif resposta == "5":
        print() 
        direcao_amostradinho = f"\t Direção: {dir_amostradinho}"
        print(direcao_amostradinho)
        input("")

    
    else:
        print() 
        print("\nOpção inválida")
        input("") 