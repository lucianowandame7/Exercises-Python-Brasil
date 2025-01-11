#Faça um programa para imprimir
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):  # Imprime os números de 1 até i
            print(j, end="   ")  # Imprime o número j com 3 espaços de separação
        print()  # Para pular para a próxima linha

# Entrada de dados
numeroDigitado = int(input("Digite um número: "))
imprimir(numeroDigitado)
