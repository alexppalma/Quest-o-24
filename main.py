#[Questão 24] Faça um Programa que leia 2 números
#e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal. 

n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))
pergunta = (input("Qual o operação deseja realizar ?  + soma, - subtração, * multiplicação, divisão: "))


if pergunta == "+":
  operacao = n1+n2
  print("Resultado:", operacao)
elif pergunta == "-":
  operacao = n1-n2
  print("Resultado:", operacao)
elif pergunta == "*":
  operacao = n1*n2
  print("Resultado:", operacao)
elif pergunta == "/":
  operacao = n1/n2
  print("Resultado:", operacao)
else:
  print("Operação inválida")
  print("Resultado:", operacao)

resultado = operacao

#Par ou impar
print("------------------------------")
if resultado % 2 == 0:
  print("É um número Par")
else:
  print("É um número Impar")
print("------------------------------")
  
#Positivo ou negativo
if resultado > 0:
  print("É um número Positivo")
else:
  print("É um número Negativo")
  
#Inteiro ou decimal 
print("------------------------------")
if resultado // 1 == resultado:
  print("É um número Inteiro")
else:
  print("É um número Decimal")