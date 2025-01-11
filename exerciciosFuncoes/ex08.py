#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def quantidade_digitos():
    numeroInformado = int(input("Digite um número: "))
    return len(str(numeroInformado))

# Chama a função sem parâmetros
print(quantidade_digitos())


