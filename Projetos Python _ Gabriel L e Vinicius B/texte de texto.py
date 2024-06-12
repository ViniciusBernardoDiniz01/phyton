with open('arquivo.txt', 'a') as file:
    file.write('\n acrescentando mais uma  linha')
with open ('arquivo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

