#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
produto1 = int(input("Digite o preco do primeiro produto: "))
produto2 = int(input("Digite o preco do segundo produto: "))
produto3 = int(input("Digite o preco do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"O produto mais barato é: {produto1}")
elif produto2 < produto1 and produto2 < produto3:
    print(f"O produto mais barato é: {produto2}")
else:
    print(f"O produto mais barato é: {produto3}")