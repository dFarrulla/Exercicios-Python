""" Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""
salario = float(input('Qual é -o salário do funcionário?'))
novo = salario + (salario * 15/100)
print("O salário reajustado é de: R${:.2f}" .format(novo))