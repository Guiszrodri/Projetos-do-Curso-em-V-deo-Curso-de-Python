km = float(input('Qual foi a velocidade do carro: '))
if km>80:
    print('Seu carro foi multado')
else:
    print('')
multa = (km-80)*7
if multa>=7:
    print('E sua multa foi de: R${:.2f}'.format(multa))
else:
    print('PARABÉNS! Você não foi multado')