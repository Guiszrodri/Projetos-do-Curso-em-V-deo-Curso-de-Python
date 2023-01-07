s = float(input('Qual o seu salário? R$'))
if s>1250:
    a = (s*0.10)
    b = a+s
    print('Seu aumento será de: R${}'.format(a))
    print('E seu novo salário sera: R${}'.format(b))
else:
    a = (s * 0.15)
    b = a + s
    print('Seu aumento será de: R${}'.format(a))
    print('E seu novo salário sera: R${}'.format(b))