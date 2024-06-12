numero = int(input("informa o valor"))

def positivo(numero):
    if numero > 0:
        print("positivo")
    
    elif numero < 0:
        print("negativo")

    else :
        print("e 0")

positivo(numero)