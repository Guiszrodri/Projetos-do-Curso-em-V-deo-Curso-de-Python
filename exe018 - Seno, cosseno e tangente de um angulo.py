import math
a = float(input('Qual o ângiulo escolhido: '))
s = math.sin(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'. format(a, s))
c = math.cos(math.radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'. format(a, c))
t = math.tan(math.radians(a))
print('O ângulo de {} tem a TANGENTE de {:.2f}'. format(a, t))
