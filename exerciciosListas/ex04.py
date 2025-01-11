#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

print('Programa para ler um vetor de 10 caracteres e diga quantas consoantes foram lidas')
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print('As consoantes foram: ', end='')
for i in range(10):
    if lista[i] not in 'aeiou':
        print(f'{lista[i]} ', end='')