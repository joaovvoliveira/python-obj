import dataclasses
import datetime

#5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse 
#usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

#qtd_salario = 1
#salario_min = 1293.2
#salario = float(input("Digite seu salario: "))
#t=2
#if salario > salario_min:
#    qtd_salario = salario//salario_min
#    resto = float(salario%salario_min)
#    print(f"O sujeito recebe {qtd_salario} salario minimos, e o resto é de {resto}\n")
#else:
#    print(f"Digite um salario maior q o salario minimo de R${salario_min}")


#6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

#valor = float(input("Digite um valor em Reais: "))
#valor = valor + valor*0.05
#print(valor)

#7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.

#valor1 = bool(input("Digite um valor: "))
#valor2 = bool(input("Digite um valor: "))
#print(valor1)
#print(valor2)

#8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

#valor1 = int(input("Digite um valor: "))
#valor2 = int(input("Digite um valor: "))
#valor3 = int(input("Digite um valor: "))
#
#NUMEROS = [valor1,valor2,valor3]
#numeros = sorted(NUMEROS, reverse=True)
#print(numeros)

#9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição de acordo com a tabela abaixo:
# Fórmula do IMC = peso / (altura) ²
#Abaixo de 18,5   | Abaixo do peso          
#Entre 18,6 e 24,9 | Peso ideal (parabéns)  
#Entre 25,0 e 29,9 | Levemente acima do peso
#Entre 30,0 e 34,9 | Obesidade grau I 
#Entre 35,0 e 39,9 | Obesidade grau II (severa)
#Maior ou igual a 40 | Obesidade grau III (mórbida)

#altura = float(input("Digite sua altura: "))
#peso = int(input("Digite seu peso: "))
#IMC = peso / (altura**2)
#if round(IMC,2) <= 18.5:
#    print("Abaixo do peso")
#elif round(IMC,2) <= 24.4:
#    print("Peso Ideal")
#elif round(IMC,2) <= 29.9:
#    print("Levemente acima do peso")
#elif round(IMC,2) <= 34.9:
#    print("Acima do peso")
#else:
#    print("Obesidade")
#print(round(IMC,2))

#11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 
#se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.

#nota1 = int(input("Digite a 1º nota: "))
#nota2 = int(input("Digite a 2º nota: "))
#nota3 = int(input("Digite a 3º nota: "))
#nota4 = int(input("Digite a 4º nota: "))
#media = 0
#notas = [nota1,nota2,nota3,nota4]
#n = 0
#for var in notas:
#    media = media + notas[n]
#    n = n+1
#    print(media)
#media = media / len(notas)
#print(media)
#if(media >= 7):
#    print("Aprovado")
#else:
#    print("Reprovado")

#12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento 
#pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.
#
# Tabela de Código de Condições de Pagamento
# 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
#
# 2 - À Vista no cartão de crédito, recebe 10% de desconto
#
# 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
#
# 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%

#CODIGOS = [2902,8562,1647,1976,5060]
#PRODUTOS = ["Televisão","Cômoda","Sofá","Computador","Celular"]
#VALOR = [1200,150,400,800,700]
#DESCONTO = [0.15,0.1,0.0,0.1]
#valor_produto = float(input("Digite o código do produto: "))
#forma_pgto = str("Digite a forma de pagamento: ")
#print(CODIGOS.index(valor_produto))
#print(f"O total a ser pago para o produto {PRODUTOS.index[valor_produto]}, código {CODIGOS.index[valor_produto]} de preço {VALOR.index(valor_produto)} é de: {VALOR.index(valor_produto)} + ({VALOR.index(valor_produto)} * {DESCONTO.index(forma_pgto)})")
#
#valor_prd = float(input("Digite o valor:"))
#FORMA_PAGAMENTO = ["PIX","CRÉDITO","PARCELADO2X","PARCELADO>3X"]
#tipo_pgto = str(input("Tipo de pagamento: "))
#forma = FORMA_PAGAMENTO.index(tipo_pgto.upper())
#if forma == 0:
#    valor_prd = valor_prd - (valor_prd*0.15)
#elif forma == 1:
#    valor_prd = valor_prd - (valor_prd*0.1)
#elif forma == 2:
#    valor_prd = valor_prd
#else:
#    valor_prd = valor_prd + (valor_prd*0.1)
#print(f"Valor a pagar: {valor_prd}")

#15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em 
#consideração o ano com 365 dias e o mês com 30 dias.

nasc = int(input("Digite o ano: "))
hoje = datetime.datetime(2024, 5, 6)
print(f"{hoje - nasc}")

#import math
#
#age=28
#name = 'João Victor'
#
#preco = 10
#print(f"R$", preco)
#preco = float(preco)
#
#print(preco)
#
#print(type(float(preco)))
#
#nome = input("Nome: ")
#idade= input("Idade: ")
#print(nome, end= idade)
#print(name)
#
#name = "Victor"
#
#if (age == 28):
#        age=27
#else:
#        age == 28;    
#
#print(f'Meu nome é {name} e tenho {age}')
#
#print(1.4 +2)
#
#STATES = ['SP','RJ','MG','PE']
#
#print(STATES)
#
#print(STATES[2])
#



