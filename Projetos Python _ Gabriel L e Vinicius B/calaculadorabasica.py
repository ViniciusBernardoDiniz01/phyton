numero1 = float(input("Digite o primeiro valor da operação: "))
operacao = input("Digite as operações (+ ; - ; * ; /)")
numero2 = float(input("Digite o segundo numero da operação: "))

if operacao == "/":
    if numero2 == 0:
        print("ERRO: Divisão por zero não é permitida.")
    else:
        resultado = numero1 / numero2
    print("O calculo da divisão é: ", resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print("O resultado da subtração é: ", resultado)
elif operacao == "+":
    resultado = numero1 + numero2
    print("O resultado da soma é: ", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("O resultado da multiplicação é:", resultado)
else:
    print("ERRO: Operação invalida insira: (Use + , - , * , /)")
















