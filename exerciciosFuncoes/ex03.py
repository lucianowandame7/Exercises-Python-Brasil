#Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.

def soma(a, b, c ):
    return a + b + c

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite o ultimo número: "))

# Chama a função passando os três argumentos e exibe o resultado
resultado = soma(a, b, c)
print(f"A soma dos números é: {resultado}")