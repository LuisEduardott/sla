def criarperfil(nome,idade,cidade):
    return f"Perfil criado: Nome: {nome} | Idade: {idade} | Cidade: {cidade}"

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

perfil = criarperfil(nome,idade,cidade)
print(perfil)