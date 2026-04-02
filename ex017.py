#exercicio para calcular a hipotenusa obtendo o cateto oposto e o cateto adjacente no input
from math import hypot,ceil
cateto_1 = float(input('Froneça o valor do cateto oposto: '))
cateto_2 = float(input('Agora o valor do cateto adjacente: '))
hipotenusa = hypot(cateto_1, cateto_2)
print(f'Considerando o cateto oposto como {cateto_1} e o cateto adjacente como {cateto_2}\nO valor da hipotenusa é {ceil(hipotenusa)}')

