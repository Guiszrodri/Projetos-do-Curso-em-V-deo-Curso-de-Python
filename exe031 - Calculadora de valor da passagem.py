v = float(input('Qual a distância de sua viagem: '))
if v<=200:
    m = (v*0.50)
    print('Sua passagem custará R${:.2f}'.format(m))
else:
    n = (v*0.45)
    print('Sua passagem custará R${:.2f}'.format(n))