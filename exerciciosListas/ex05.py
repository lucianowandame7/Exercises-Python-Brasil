#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

print('Programa para ler 20 numeros inteiros e armazene-os num vetor')

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
par = []
impar = []

for i in range(20):
    if vetor[i] % 2 == 0:
        par.append(vetor[i])
    else:
        impar.append(vetor[i])
print(vetor)
print(par)
print(impar)