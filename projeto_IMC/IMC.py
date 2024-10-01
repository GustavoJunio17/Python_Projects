import os

def menu():
    print("Calculadora IMC")
    print("1 - Calcular")
    print("0 - Sair")

def classificacao(n):
    if (n <= 18.5):
        print("Abaixo do peso")
        
    if (n >= 18.6 and n <= 24.9):
        print("Normal")
        
    if (n >= 25 and n <= 29.9):
        print("Sobrepeso")
    
    if (n >= 30 and n <= 34.9):
        print("Obesidade grau I")
    
    if (n >= 35 and n <= 39.9):
        print("Obesidade grau II")
        
    if (n > 40):
        print("Obesidade grau III")
        

def calcularIMC():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    resultado = peso / (altura*altura)
    print(f"O resultado é: {resultado:.2f}")
    classificacao(resultado)
    print("1 - Voltar ao menu")
    op = int(input("Digite uma opção: "))
    os.system("cls")
    
while True:
    menu()
    op = int(input("Selecione uma opção: "))
    
    if(op == 1):
        os.system("cls")
        calcularIMC()
        
    elif(op == 0):
        print("Encerrando o programa") 
        break