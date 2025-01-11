# print('Programa para informar a data ao usuario no formato dd de MM de AAAA')
# dia = int(input('Digite o dia: '))
# mes  = int(input('Digite o mes: '))
# ano = int(input('Digite o ano: '))

# if mes == 1 :
#     print(f'{dia} de janeiro de {ano}')
# elif mes == 2 :
#     print(f'{dia} de Fevereiro de {ano}')
# elif mes == 3 : 
#     print(f'{dia} de Março de {ano}')
# elif mes == 4 :
#    print(f'{dia} de Abril de {ano}')
# elif mes == 5 :
#     print(f'{dia} de Maio de {ano}')
# elif mes == 6 :
#     print(f'{dia} de Junho de {ano}')
# elif mes == 7 : 
#     print(f'{dia} de Julho de {ano}')
# elif mes == 8 :
#     print(f'{dia} de Agosto de {ano}')
# elif mes == 9 :
#     print(f'{dia} de Setembro de {ano}')
# elif mes == 10 :
#     print(f'{dia} de Outubro de {ano}')
# elif mes == 11 :
#     print(f'{dia} de Novembro de {ano}')
# elif mes == 12 :
#     print(f'{dia} de Dezembro de {ano}')

# else :
#     print('Digite um mes valido')

from datetime import datetime

def data_por_extenso(data_string):
    try:
        # Converter a string para um objeto datetime
        data = datetime.strptime(data_string, "%d/%m/%Y")
        # Obter o dia, mês por extenso e ano
        dia = data.day
        mes_por_extenso = data.strftime("%B").lower()
        ano = data.year
        # Retornar a data formatada
        return f"{dia} de {mes_por_extenso} de {ano}"
    except ValueError:
        # Retornar None se a data for inválida
        return None

# Exemplos de uso
print(data_por_extenso("15/12/2005"))  # Saída: "7 de janeiro de 2025"
print(data_por_extenso("31/02/2025"))  # Saída: None
