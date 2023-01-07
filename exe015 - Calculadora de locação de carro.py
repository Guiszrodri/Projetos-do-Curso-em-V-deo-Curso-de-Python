k = float(input('Quantos KM você andou com o carro? '))
d = int(input('Quantos dias você ficou com o carro? '))
t = (k*0.15) + (d*60)
print('O total a pagar pelo aluguel do carro é de: \nR${:.2f}'.format(t))