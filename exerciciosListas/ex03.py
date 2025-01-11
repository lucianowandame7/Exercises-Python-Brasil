#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

print('Programa para ler 4 notas e mostrar as notas e a media')

notas = []

for i in range(4):
    nota = float(input(f'Digite as notas: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print('As notas foram: ', notas)
print(f'A media das notas foi: {media}')