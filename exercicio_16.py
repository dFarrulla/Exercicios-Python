'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''
'''   Pode usar <import math> ou <from math import trunc>'''
from math import trunc
num = float(input("Digite um valor: "))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num, math.trunc(num)))







