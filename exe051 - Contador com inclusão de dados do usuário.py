primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decima = primeiro + (10-1) * razao
for c in range(primeiro, decima + razao, razao):
    print('{}'.format(c), end=' ')
print('ACABOU')