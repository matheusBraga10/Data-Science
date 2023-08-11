def titulo():
    print('=--='*30)
    print('\tERRO!\n\tTENTE NOVAMENTE!')
    print('=--='*30)

def main():   
    numero_pedidos = int(input())
    if numero_pedidos <= 0:
            titulo()
    for i in range(1, numero_pedidos + 1):
        prato = input()
        calorias = int(input())
        if calorias <= 0:
            titulo()
        eh_veg = input()
        if eh_veg == 's':
            eh_veg = 'Vegano'
        else:
            eh_veg = 'Não é Vegano'

        vegano = {'numero_pedidos': i, 'prato': prato, 'eh_veg':eh_veg, 'calorias': calorias}
        print(f"Pedido {vegano['numero_pedidos']}: {vegano['prato']} ({vegano['eh_veg']}) - {vegano['calorias']} calorias")


main()