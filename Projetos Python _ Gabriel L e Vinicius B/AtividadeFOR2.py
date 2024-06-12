maior = float("-inf")
soma = 0

for i in range (10):
    numero = int(input("Informe o numero: "))
    soma += numero
    
    if numero > maior:
        maior = numero
media = soma / 10 

print(maior)
print(soma)
print(media)



  

