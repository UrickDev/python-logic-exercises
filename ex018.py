#Programa para trazer o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
#Define nome do programa
programa = " Seno - Cosseno - Tangente "
#Imprime nome do programa
print(f'{programa:=^45}')
#Recebe o valor do ângulo em graus
angulo_graus = float(input('Digite o valor de um ângulo qualquer sem °: '))
#Transforma valor no ângulo de graus para radiano
angulo_radian = radians(angulo_graus)
#Calcula seno
seno = sin(angulo_radian)
#Calcula cosseno
cosseno = cos(angulo_radian)
#Calcula tangente
tangente = tan(angulo_radian)
#Printa os valores de seno, cosseno e tangente
print(f'Os valores respectivos de Seno, Cosseno e tangente são aproximadamente, {seno:2f}, {cosseno:2f}, {tangente:2f}.')