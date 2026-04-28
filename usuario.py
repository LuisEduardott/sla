def exibir_info_usuario(info):
    print("Informações do usuário:")
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

info_usuario = {}

usuario = input("Digite o nome do usuário ou 'sair' para encerrar: ")

while usuario != "sair":
    chave = input("Nome do campo (ex: profissao)): ")
    valor = input("Valor do campo: ")
    info_usuario[chave] = valor
    usuario = input("Digite o nome do usuário (ou 'sair' para encerrar): ")


exibir_info_usuario(info_usuario)
print("Programa encerrado.")  