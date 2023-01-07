v = float(input('Qual o valor do produto? R$'))
va = v-(v*(10/100))
vp = v+(v*(8/100))
print('Se voce pagar a vista o seu produto sairá por R${:.2f}\nCaso pague parcelo o valor ficará em R${:.2f}'.format(va,vp))

