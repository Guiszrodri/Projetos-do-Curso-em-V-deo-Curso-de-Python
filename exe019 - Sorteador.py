import random
a1=input('Qual nome do aluno 1: ')
a2=input('Qual nome do aluno 2: ')
a3=input('Qual nome do aluno 3: ')
a4=input('Qual nome do aluno 4: ')
lista = [a1,a2,a3,a4]
e=random.choice(lista)
print('O aluno escolhido foi: {}'.format(e))