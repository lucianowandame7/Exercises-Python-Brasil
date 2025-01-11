#Faça um Programa que peça a idade e a altura de 5 pessoas, 
# armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

print('Programa para ler a idade e a altura de 5 pessoas')

idades = []
altura = []

for i in range(5):
    idades.append(int(input(f'Digite a idade da pessoa {i+1}: ')))
    altura.append(float(input(f'Digite a altura da pessoa {i+1}: ')))


idades.reverse()
altura.reverse()

print('As idades foram: ', idades)
print('As alturas foram: ', altura)