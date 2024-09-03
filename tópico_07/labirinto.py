# importar módulo O.S. para limpeza da tela
import os

# Menu de opções
menu = """
[0] - Desistir da travessia
[1] - Posição atual do Amostradinho
[2] - Caminhar
[3] - Girar para esquerda
[4] - Girar para a direita
"""

# laço de repetição infinito
while(True):

    # faz a limpeza da tela
    os.system("cls")

    # imprime o menu de opções
    print(f"\n{menu}\n")

    # captura a resposta do usuário
    resposta = input("Selecione uma opção: ")

    # testa a resposta do usuário
    if resposta == "0":

        # faz a limpeza da tela
        os.system("cls")
        # imprime mensagem de desistência
        print("Desistindo da travessia! :(")
        print() # print vazio para pular uma linha
        # interrompe o loop infinito
        break

    elif resposta == "1":
        print() # print vazio para pular uma linha
        print("Crie a função e faça aqui a invocação para receber a posição atual doAmostradinho!")
        input("") # Input vazio para fazer leitura da mensagem impressa

    elif resposta == "2":
        print() # print vazio para pular uma linha
        print("Crie a função e faça aqui a invocação para Amostradinho caminhar para a nova posição.")
        input("") # Input vazio para fazer leitura da mensagem impressa

    elif resposta == "3":
        print() # print vazio para pular uma linha
        print("Crie a função e faça aqui a invocação para Amostradinho girar para a esquerda.")
        input("") # Input vazio para fazer leitura da mensagem impressa

    elif resposta == "4":            
        print() # print vazio para pular uma linha
        print("Crie a função e faça aqui a invocação para Amostradinho girar para a direita.")
        input("") # Input vazio para fazer leitura da men