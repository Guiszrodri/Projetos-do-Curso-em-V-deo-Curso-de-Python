r1 = float(input('Insira a medida da primeira reta: '))
r2 = float(input('Insira a medida da segunda reta: '))
r3 = float(input('Insira a medida da terceira reta: '))
if r1 < r2+r3 and r2 < r1+r3 and r3< r2+r1:
    print('Você consegue formar um triângulo')
    if r1 == r2 == r3:
        print('Seu triangulo é um EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Seu triangulo é um ISÓSCELES')
    else:
        print('Seu triangulo é um ESCALENO')
else:
    print('Você não consegue formar um triângulo')