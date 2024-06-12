lista = [23, 9, 75, 46, 3, 54, 32, 6, 89, 66, 44]
soma = 0
maior = -1

for i in lista:
    soma += i
    if i > maior:
        maior = i
for i in lista:
    if i % 2 == 0:
        print("Os numeros pares são: ",i)

    
print("A soma é:",soma)
print("O maior numero é: ",maior)

