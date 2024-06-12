numero = int(input("escreva o valor"))
maior = -1 

while numero != 0:
    if numero > maior:
        maior = numero 
    numero = int(input("informe outro valor: "))

print("o maior valor e :", maior)
