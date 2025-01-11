#Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

mediaAlunos = []

for i in range(10):
    notas = []
    for j in range(4):
        notas.append(float(input(f'Digite a nota {j+1}: ')))
    media = sum(notas) / len(notas)
    mediaAlunos.append(media)

alunosAprovados = 0

for i in range(10):
    if mediaAlunos[i] >= 7.0:
        alunosAprovados += 1

print(f'{alunosAprovados} alunos tiveram media maior ou igual a 7.0')