#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random

print("Programa para embaralhar palavras")

def embaralhar_palavra(palavra):
    # Converter para letras maiúsculas
    palavra = palavra.upper()
    # Transformar a palavra em uma lista de caracteres
    letras = list(palavra)
    # Embaralhar as letras
    random.shuffle(letras)
    # Juntar as letras embaralhadas de volta em uma string
    palavra_embaralhada = ''.join(letras)
    return palavra_embaralhada

# Entrada do usuário
palavra = input("Digite uma palavra: ")
resultado = embaralhar_palavra(palavra)
print(f"A palavra embaralhada é: {resultado}")
