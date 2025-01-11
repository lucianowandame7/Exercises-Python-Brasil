#Faça um programa, com uma função que necessite de um argumento.
#  A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verifica_numero(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Chama a função e exibe o resultado
resultado = verifica_numero(numero)
print(f"O resultado é: {resultado}")

