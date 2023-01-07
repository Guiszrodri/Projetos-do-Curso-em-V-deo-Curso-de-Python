num = int(input("Digite um número inteiro: "))
print('''Digite uma das opções abaixo para conversão
[1] para binário
[2] para octal
[3] para hexadecimal''')
opção = int(input("Sua opção: "))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Digite umas das opções solicitadas anteriormente')
