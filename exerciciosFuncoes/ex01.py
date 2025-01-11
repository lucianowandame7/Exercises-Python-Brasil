#Faça um programa para imprimir, 
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.


def imprimir(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="   ")  # Imprime o número i com 3 espaços de separação
        print()  # Para pular para a próxima linha

# Entrada de dados
numeroDigitado = int(input("Digite um número: "))
imprimir(numeroDigitado)

