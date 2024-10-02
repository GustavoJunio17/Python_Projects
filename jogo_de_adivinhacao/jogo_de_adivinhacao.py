import os
import random

def menu():
    print("Jogo de Adivinhacao")
    print("1 - Começar")
    print("0 - Sair")
    
def jogo():
    os.system('cls')
    limite = int(input("Digite um limite: "))
    numero = random.randint(0, limite)
    adivinhar = int(input(f"Adivinhe o número que estou pensando entre 0 e {limite}: "))
    if(adivinhar == numero):
        print("Parabéns você acertou")
    if(adivinhar != numero):
        print(f"Você errou, o número era {numero}")
    

while True:
    menu()
    op = int(input("Digite uma opção: "))
    if op == 1:
        while True:
            jogo()
            continuar = str(input("Deseja jogar novamente (s/n): ?"))
            if continuar == 's':
                os.system('cls')
                continue
            if continuar == 'n':
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Opção incorreta digite novamente")
                continuar = str(input("Deseja jogar novamente (s/n): ?"))
        continue
    if op == 0:
        break
    else:
        print("Opção incorreta digite novamente")
        op = int(input("Digite uma opção: "))
        os.system('cls')