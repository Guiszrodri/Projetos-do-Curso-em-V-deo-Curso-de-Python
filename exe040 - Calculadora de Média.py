n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
m = (n1+n2)/2
print('Sua média é: {}'.format(m))
if m<5:
        print('\033[31mREPROVADO')
elif m >=5 and m<=6.9:
    print("\033[33mRECUPERAÇÃO")
else:
    print('\033[32mAPROVADO')