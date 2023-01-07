casa = float(input("Qual o valor da casa: R$ "))
salario = float(input("Qual seu salário: R$ "))
anos = float(input("Quanto anos de pagamento: "))
prestacao = casa/(anos*12)
if prestacao >= salario*0.3:
    print("Infelizmente, você não poderá financiar este imóvel")
else:
    print("Seu financiamento ficará em R$ {:.2f} por mês".format(prestacao))