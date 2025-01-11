# #Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, 
# # linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
# # eles devem ser modificados para valores dentro da faixa de forma elegante.

# def desenhaMoldura(linha, coluna):
#     linha = int(input("Digite a quantidade de linhas: "))
#     if linha < 1:
#         linha = 1

#     elif linha > 20:
#         linha = 20
#     else:
#         linha = linha
#         print(linha * "-")
#     coluna = int(input("Digite a quantidade de colunas: "))
#     if coluna < 1:
#         coluna = 1

#     elif coluna > 20:
#         coluna = 20
#     else:
#         coluna = coluna
#         print(coluna * "|")


def desenhaMoldura(linha, coluna):
    # Garantir que os valores estejam no intervalo correto
    linha = max(1, min(linha, 20))
    coluna = max(1, min(coluna, 20))
    
    # Desenhar a primeira linha (topo da moldura)
    print("+" + "-" * linha + "+")
    
    # Desenhar as linhas do meio (com bordas verticais)
    for _ in range(linha):
        print("|" + " " * coluna + "|")
    
    # Desenhar a última linha (base da moldura)
    print("+" + "-" * coluna + "+")

# Solicitar os valores ao usuário
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

# Chamar a função com os valores fornecidos
desenhaMoldura(linhas, colunas)



       