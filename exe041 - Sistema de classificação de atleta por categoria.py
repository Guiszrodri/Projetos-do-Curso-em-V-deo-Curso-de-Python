from datetime import date
atual = date.today().year
ano = int(input("Qual o ano de nascimento do atleta: "))
idade = atual-ano
print('Sua idade é: {}'.format(idade))
if idade<=9:
    print('Sua categoria é: MIRIM')
elif idade<=14:
    print('Sua categoria é: INFANTIL')
elif idade<=19:
    print('Sua categoria é: JUNIOR')
elif idade<=25:
    print('Sua categoria é: PROFFISSIONAL')
else:
    print('Sua categoria é: MASTER')