from time import sleep
from defs import assento, cadastro, filme, comida, total, limpaTela
from variables import TEXT_BEMVINDO, TEXT_MENU

# CADASTRO
print(TEXT_BEMVINDO)
cadastro()
perg = int(input('Seus dados conferem? [1]Sim [2]Não '))

if perg == 2:
    print("Digite seus dados novamente")
    cadastro()

# OPCÕES
limpaTela()
print(TEXT_MENU)
sleep(1)
opc = int(input('Digite sua opção: '))

if opc == 1:
    filme()
    assento()
    print("""\033[34m[1]\033[m ENCERRAR E PAGAR
\033[34m[2]\033[m VER COMIDAS""")
    escolha_pos = int(input('Sua escolha: '))
    if escolha_pos == 1:
        print("Tenha um ótimo filme!")
    if escolha_pos == 2:
        comida()
        total()

if opc == 2:
    comida()
    print("""\033[34m[1]\033[m ENCERRAR E PAGAR
\033[34m[2]\033[m COMPRAR INGRESSOS""")
    escolha_pos = int(input('Sua escolha: '))
    if escolha_pos == 1:
        print("Tenha um bom lanche!")
    if escolha_pos == 2:
        filme()
        assento()