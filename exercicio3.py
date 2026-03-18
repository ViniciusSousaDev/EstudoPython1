num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
oper = input("Digite a operação (+, -, *, /): ")

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
else:
    print("Operação inválida")
