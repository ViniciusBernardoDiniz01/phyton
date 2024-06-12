senha = str(input("Qual a sua senha: "))
ConfirmacaoDeSenha = str(input("Confirme sua senha: "))

while senha != ConfirmacaoDeSenha:
    print("Senha incorreta")
    ConfirmacaoDeSenha = str(input("Confirmação de senha incorretos. Coloque a senha igual a anterior: "))
    
    

print("Senha correta.")