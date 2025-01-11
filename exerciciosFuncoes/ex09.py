#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
#[::-1] inverte a string
def reverso(numero):
    return int(str(numero)[::-1])

resultado = reverso(127)
print(resultado)