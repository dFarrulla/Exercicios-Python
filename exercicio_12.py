""" Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""
preco = float(input("Qual o valor do produto?: "))
novo = preco -(preco * 5/100)
print('O produto que custava  R${}, na promoção com desconto de 5% vai custar R{}' .format(preco, novo))