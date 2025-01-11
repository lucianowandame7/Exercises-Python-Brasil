#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
# O programa deverá então exibir o valor a ser pago na tela. 
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
#  Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento():
    while True:
        # Solicita o valor da prestação e os dias de atraso
        valorPrestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))
        
        if valorPrestacao == 0:  # Condição de parada
            print("Programa encerrado.")
            break

        diasAtraso = int(input("Digite o número de dias em atraso: "))

        # Se não houver atraso, o valor permanece o mesmo
        if diasAtraso == 0:
            print(f"O valor a ser pago é: R$ {valorPrestacao:.2f}")
        elif diasAtraso > 0:
            # Calcula multa de 3% e juros de 0,1% por dia de atraso
            multa = valorPrestacao * 0.03
            juros = valorPrestacao * 0.001 * diasAtraso
            valorFinal = valorPrestacao + multa + juros
            print(f"O valor a ser pago é: R$ {valorFinal:.2f}")

# Chama a função
valorPagamento()

