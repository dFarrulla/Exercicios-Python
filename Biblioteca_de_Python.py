"""Bibliotecas de Python d
      _Módulos_
      _Biclioteca Math_
      ==> ceil, floor, trunc, pow, sqrt, factorial <==
<import math>
<from math import sqrt, ceil>"""

import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de um {} é igual a {}" .format(num, math.ceil(raiz)))  

from math import sqrt, floor
num = int(input('Digiter um número: '))
raiz = sqrt(num)
print('araiz de {} é igual a {:.2f}' .format(num,floor(raiz)))
