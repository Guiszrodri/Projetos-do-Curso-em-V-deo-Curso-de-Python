valor = float(input('Qual o valor do produto: R$ '))
print('''Qual a condição de pagamento
\033[4m[1]Dinheiro
[2]À vista no cartão
[3]2x no cartão
[4]Mais de 3x no cartão\033[m''')
opção = int(input('Selecione uma opção: '))
if opção == 1:
    av = valor-(valor*0.10)
    print('\033[4;32mO valor do produto terá um desconto de 10%\033[m, ficando com seu valor final de R${:.2f}'.format(av))
elif opção == 2:
    ac = valor-(valor*0.05)
    print('\033[4;32mO valor terá um desconto de 5%\033[m, ficando com seu valor final de R${:.2f}'.format(ac))
elif opção == 3:
    xx = valor/2
    print('Parcelando em 2x no cartão seu produto sairá por R$ {:.2f} e sua parcela será de R${:.2f} por mês'.format(valor,xx))
elif opção == 4:
    numerodex = int(input('Quantas vezes irá parcelar: '))
    xxx = valor+(valor*0.20)
    parcela = xxx/numerodex
    print('Você irá parcelar sua compra em {} vezes, o valor final será de R${:.2f} e as parcelas de R${:.2f} por mês\033[1;31m COM JUROS'.format(numerodex,xxx,parcela))
else:
    print('Selecione uma forma de pagamento')