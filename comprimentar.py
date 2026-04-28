def comprimentar(nome):
    return f"Olá, {nome}! Seja bem-vindo(a)!"

nome = input("Digite seu nome: ")
mensagem = comprimentar(nome)
print(mensagem)
idade = int(input(f"{nome}, Qual sua idade:"))
print(f"{nome}, você tem {idade} anos.")    