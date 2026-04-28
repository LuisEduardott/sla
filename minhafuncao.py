def formatar_real_replace(valor):
    texto = f"R${valor:.2f}" # Padrao EUA 1,234.56
    texto = texto.replace(".","X")
    texto = texto.replace(",",",")
    texto = texto.replace("X",".")
    return texto

# Exemplo de uso
preco = float(input("Digite o preço: ")) 
print(formatar_real_replace(preco)) # R$1.234,56