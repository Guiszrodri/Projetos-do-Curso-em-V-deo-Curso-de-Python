from datetime import date #biblioteca para pegar o ano atual
a = int(input('Insira um ano e descubra se ele é ou não bissexto, ou, coloque 0 para o ano atual: '))
if a == 0:
    a = date.today().year #para pegar o ano atual se colocar 0
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é bissexto'.format(a))
else:
    print('O ano de {} não é bissexto'.format(a))
