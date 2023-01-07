from datetime import date
atual = date.today().year
nascimento = int(input('Insira seu ano de nascimento: '))
idade = atual-nascimento
if idade == 18:
    print("Você tem {} e \033[1;32mjá está na hora de se alistar\033[m".format(idade))
elif idade < 18:
    a = 18-idade
    print("Você tem {} e ainda vai se alistar, \033[1;33mfalta {} ano(s)\033[m".format(idade,a))
    b = nascimento+18
    print('\033[1;32mSeu ano de alistamento será {}\033[m'.format(b))
else:
    a = idade-18
    print("Você tem {} e já se alistou à {} ano(s)\033[m".format(idade,a))
    b = nascimento + 18
    print('\033[1;32mSeu ano de alistamento foi {}\033[m'.format(b))