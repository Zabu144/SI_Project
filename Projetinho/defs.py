from random import randint
from time import sleep
from variables import FILMES_LIST, FILMES_DICT, TEXT_FILME_1, TEXT_FILME_2, TEXT_FILME_3, TEXT_FILME_4, TEXT_FILME_5, TEXT_FILME_6, TEXT_MENU_COMIDAS, TEXT_PIPOCA, TEXT_REFRI, TEXT_DOCES
import os


def cadastro(nome='', email='', senha=''):  # CADASTRO
    nome = str(input('\033[4;34mDigite o seu nome:\033[m '))
    email = str(input('\033[4;34mDigite o seu email:\033[m '))
    senha = str(input('\033[4;34mDigite a sua senha:\033[m '))
    
    print(f"""Sua informações são:
    nome = {nome}
    email = {email}
    senha = {senha}""")

    
def filme():  # ESCOLHA DOS FILMES
    escolha_filme2 = 0

    while escolha_filme2 != 1:
        # LISTA DE FILMES
        limpaTela()
        print("-==-== \033[1;31;40mESCOLHA SEU FILME\033[m ==-==-")
        for c in range(0, 6):
            print(f'{[c+1]} {FILMES_DICT["Filmes"][c]}')
        escolha_filme = int(input("Escolha: "))

        
        # INFORMAÇÕES DE CADA FILME
        if escolha_filme == 1:   # FILME 1
            print(TEXT_FILME_1)

        if escolha_filme == 2:   # FILME 2
            print(TEXT_FILME_2)

        if escolha_filme == 3:   # FILME 3
            print(TEXT_FILME_3)

        if escolha_filme == 4:   # FILME 4
            print(TEXT_FILME_4)

        if escolha_filme == 5:   # FILME 5
            print(TEXT_FILME_5)

        if escolha_filme == 6:   # FILME 6
            print(TEXT_FILME_6)

        # POS INFOMAÇÃO DO FILME
        sleep(1)
        print("-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-")
        escolha_filme2 = int(input("\033[34m[1]\033[m ESCOLHER ASSENTO    \033[34m[2]\033[m ESCOLHER OUTRO FILME "))

        if escolha_filme2 == 1:
            break
            
        
def assento():  # ESCOLHA DE ASSENTOS
    global total_ingresso
    matriz = [
        ['▱', '▱', '▱', '▱', '▱', '▱', '▱', '▱'],
        ['▱', '▱', '▱', '▱', '▱', '▱', '▱', '▱'],
        ['▱', '▱', '▱', '▱', '▱', '▱', '▱', '▱'],
        ['▱', '▱', '▱', '▱', '▱', '▱', '▱', '▱'],
        ['▱', '▱', '▱', '▱', '▱', '▱', '▱', '▱'],
        ['▱', '▱', '▱', '▱', '▱', '▱', '▱', '▱'],
        ['▱', '▱', '▱', '▱', '▱', '▱', '▱', '▱'],
        ['▱', '▱', '▱', '▱', '▱', '▱', '▱', '▱'],
    ]
    print()
    print("""▱ - Cadeira vazia
▰ - Cadeira Ocupada
\033[32m▰\033[m - Cadeira escolhida""") # LEGENDA DOS ASSENTOS
    print('Valor de cada ingresso: \033[32mR$\033[m20,00')
    print()
    
    num = randint(0, 50)
    for total_cadeira in range(num):   # RANDOMIZADOR DE CADEIRAS
        matriz[randint(0, 7)][randint(0, 7)] = '▰'

    qt_ingresso = int(input('Quantos ingressos você deseja comprar? ')) 
    print()
    
    print('  1 2 3 4 5 6 7 8')
    for index, c in enumerate(matriz):
        print(f'{index+1} ', end='')
        for l in c:
            print(l, end=' ')
        print()
    print("▭▭▭▭  TELA ▭▭▭▭")
    
    for c in range(qt_ingresso):    # ESCOLHA DOS ASSENTOS
        while True:
            local_linha = int(input('Digite a linha: '))
            local_coluna = int(input('Digite a coluna: '))

            if matriz[local_linha - 1][local_coluna - 1] == '▰':
                print("O local escolhido já está ocupado!")
            elif matriz[local_linha - 1][local_coluna - 1] == '▱':
                break

        matriz[local_linha - 1][local_coluna - 1] = '\033[32m▰\033[m'
        for linha in matriz:
            for cadeira in linha:
                print(cadeira, end=' ')
            print()
        total_ingresso = qt_ingresso * 20   # VAlOR TOTAL DOS INGRESSOS
    print(f'Valor total dos ingressos \033[32mR$\033[m{total_ingresso},00')
       
  
def comida():   # FUNÇÃO DAS COMIDAS
    global total_comida 
    dados = []
    
    print("-==-== \033[1;31;40mCOMIDA\033[m ==-==-")
    while True:
        print(TEXT_MENU_COMIDAS)     # ESCOLHA DE COMIDA
        sleep(1)
        escolha_comida = int(input('Sua escolha: '))  # ESCOLHA
        
        if escolha_comida == 1: # CASO ELE ESCOLHA PIPOCA
            print(TEXT_PIPOCA)
            print()
            dados.append(int(input('Sua escolha (DIGITE O PREÇO DO PRODUTO): ')))
            print()
            cont = int(input("\033[34m[1]\033[m Escolher outro item \033[34m[2]\033[m Encerrar pedido "))
            print()
            if cont == 2:
                print("Pedido de comida encerrado")
                print(f"Seus pedidos foram: {dados}")
                total_comida = sum(dados)
                print(f"Total a pagar \033[32mR$\033[m{total_comida},00")
                break
        
        if escolha_comida == 2: # CASO ELE ESCOLHA REFRI
            print(TEXT_REFRI)
            print()
            dados.append(int(input('Sua escolha (DIGITE O PREÇO DO PRODUTO): ')))
            print()
            cont = int(input("\033[34m[1]\033[m Escolher outro item \033[34m[2]\033[m Encerrar pedido "))
            if cont == 2:
                print("Pedido de comida encerrado")
                print(f"Seus pedidos foram: {dados}")
                total_comida = sum(dados)
                print(f"Total a pagar \033[32mR$\033[m{total_comida},00")
                break
            
        if escolha_comida == 3: # CASO ELE ESCOLHA DOCES
            print(TEXT_DOCES)
            print()
            dados.append(int(input('Sua escolha (DIGITE O PREÇO DO PRODUTO): ')))
            print()
            cont = int(input("\033[34m[1]\033[m Escolher outro item \033[34m[2]\033[m Encerrar pedido "))
            if cont == 2:
                print("Pedido de comida encerrado")
                print(f"Seus pedidos foram: {dados}")
                total_comida = sum(dados)
                print(f"Total a pagar pela comida\033[32mR$\033[m{total_comida},00")
                break


def total():  # FUNÇÃO TOTAL A PAGAR
    print(f"Total a ser pago: \033[32mR$\033[m{total_comida + total_ingresso},00")
 
   
def limpaTela():
    os.system("cls")

    