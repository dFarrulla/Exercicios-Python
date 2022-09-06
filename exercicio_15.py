"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""
km = float(input('Quantos km o carro percorreu?: '))
dias = int(input('Quantos o dias vc ficou com o carro?: '))
diaria = dias * 60
rodado = km * 0.15
print('O valor a pagar pelo carro alugado é de :R${:.2f}' .format(diaria + rodado))
