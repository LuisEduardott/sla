def comprimentar(nome):
    return f"Olá, {nome}! Seja bem-vindo(a)!"
def sua_idade(idade):
    return f"{nome}! Você tem {idade} anos."

nome = input("Digite seu nome: ")
mensagem = comprimentar(nome)
print(mensagem)
idade = int(input(f"{nome}, Qual sua idade:"))
print(sua_idade(idade))