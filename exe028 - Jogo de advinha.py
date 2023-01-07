import random
from time import sleep #para colocar um timer
x = random.randint(0,5)
n = int(input('Adivinhe qual número eu escolhi entre 0 e 5: '))
print('Será que você ganhou....')
sleep(3)
if n == x:
    print('PARABÉNS VOCÊ ACERTOU MEU NÚMERO')
else:
    print('É NÃO FOI DESTA VEZ, VOCÊ PERDEU, EU PENSEI NO NÚMERO {}'.format(x))