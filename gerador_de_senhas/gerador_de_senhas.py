import os
import random

def menu():
    print("Gerador de Senhas")
    print("1 - Gerar")
    print("0 - Sair")
    
def gerador_de_senhas():
    tamanho = int(input("Digite a quantidade de caracteres de sua senha: "))
    simbolos = str(input("Se desejar simbolos digite os simbolos: "))
    letras = str(input("Deseja letras s/n?: "))
    print(f"Senha gerada: {gerar_senha(tamanho, simbolos, letras)}")

def gerar_senha(tamanho, simbolos, letras):
    senha = []
    senha_final = ""
    
    for n in range(tamanho):
        seed = random.randint(0, 3)
        if seed == 3:
            senha.append(str(aleatoriedade_simbolo(simbolos)))
            continue
        senha.append(str(random.randint(0, 9)))
        continue
    
    
    for caractere in senha:
        senha_final += caractere
        continue
    return senha_final

def aleatoriedade_simbolo(simbolos):
    return simbolos[random.randint(0, len(simbolos)-1)]

while True:
    menu()
    op = int(input("Digite uma opção: "))
    
    if op == 1:
        gerador_de_senhas()
        continue
    
    if op == 0:
        break
    
    else:
        op = int(input("Opção incorreta, digite novamente: "))