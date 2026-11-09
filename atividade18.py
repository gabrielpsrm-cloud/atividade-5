inventario = []

while True:
    item = input("Digite um item ou 'sair': ")

    if item == "sair":
        break
    inventario.append(item)

print("inventario:", inventario)