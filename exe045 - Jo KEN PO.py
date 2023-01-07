from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Selecione uma das opções abaixo e tente ganhar de máquina no JO KEN PO!
[0] Pedra
[1] Papel
[2] Tesoura''')
opção = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*10)
print('O computador escolheu {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[opção]))
print('-='*10)
if computador == 0 and opção == 1:
    print('\033[32mVocê VENCEU')
elif computador == 1 and opção == 2:
    print('\033[32mVocê VENCEU')
elif computador == 2 and opção == 0:
    print('\033[32mVocê VENCEU')
elif computador == 1 and opção == 0:
    print('\033[31mComputador VENCEU')
elif computador == 2 and opção == 1:
    print('\033[31mComputador VENCEU')
elif computador == 0 and opção == 2:
    print('\033[31mComputador VENCEU')
else:
    print('\033[33mDeu empate, jogue de novo')
