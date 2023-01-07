nome = input('Por gentileza me informe o seu nome: ')
altura = float(input('Olá {}, qual a sua altura: '.format(nome)))
peso = float(input('Olá {},qual o seu peso: '.format(nome)))
imc = peso/(altura*altura)
pesomin = 18.5*(altura*altura)
pesomax = 25*(altura*altura)
print('Seu IMC é: {:.1f}'.format(imc))
if imc<18.5:
    print('\033[31mVocê está abaixo do seu peso ideal, aconcelhamos que procure um médico nutricionista!')
    print('\033[32mSeu peso ideal é entre {:.1f} e {:.1f}'.format(pesomin,pesomax))
elif imc>=18.5 and imc<=25:
    print('\033[32mVocês está no peso ideal!')
    print('\033[32mSeu peso ideal é entre {:.1f} e {:.1f}'.format(pesomin,pesomax))
elif imc>25 and imc<=30:
    print('\033[33mVocê está com sobrepeso!\033[1;31mCUIDADO!')
    print('\033[32mSeu peso ideal é entre {:.1f} e {:.1f}'.format(pesomin, pesomax))
elif imc>30 and imc<=40:
    print('\033[7;31mVocê está com obesidade, aconcelhamos que procure um médico nutricionista!\033[m')
    print('\033[32mSeu peso ideal é entre {:.1f} e {:.1f}'.format(pesomin, pesomax))
else:
    print('\033[7;31mVocê está com obesidade mórbida, aconcelhamos que procure um médico nutricionista com urgência!\033[m')
    print('\033[32mSeu peso ideal é entre {:.1f} e {:.1f}'.format(pesomin, pesomax))