lista = [3, 7, 9, 12, 15, 23]
lista2 = []
contador = 0


while contador < 6:
    numero = int(input("Escreva um numero: "))
    lista2.append(numero)
    contador+=1
    print(lista2)

for numero in lista2:
    if numero in lista:
        print("Esse são os numeros que voce acertou: ",numero)





