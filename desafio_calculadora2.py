#aula 6_7

# operacao = input("Escolha a operação (+, -, *, /): ")
# num1 = float(input("Primeiro numero: "))
# num2 = float(input("Segundo numero: "))

# while operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":

#     if operacao == "+":
#         print(num1 + num2)
#     elif operacao == "-":
#         print(num1 - num2)
#     elif operacao == "*":
#         print(num1 * num2)
#     else:
#         print(num1 / num2)
#     operacao = input("Escolha a operação (+, -, *, /): ")
#     num1 = float(input("Primeiro numero: "))
#     num2 = float(input("Segundo numero: "))

# print("Operação fornecida não e valida")

operacao = input("Escolha a operação (+, -, *, /): ")

while operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":

    num1 = float(input("Primeiro numero: "))
    num2 = float(input("Segundo numero: "))

    if operacao == "+":
        print(num1 + num2)
    elif operacao == "-":
        print(num1 - num2)
    elif operacao == "*":
        print(num1 * num2)
    else:
        print(num1 / num2)
    operacao = input("Escolha a operação (+, -, *, /): ")

print("Operação fornecida não e valida")