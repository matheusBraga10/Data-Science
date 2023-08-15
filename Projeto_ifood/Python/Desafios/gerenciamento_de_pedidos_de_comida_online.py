def main():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        pedido = input().split(' ')
        nome = pedido[0]
        valor = float(pedido[0])
        total += valor

    cupom = (input())
    desconto = (100 - float(cupom[:2]))/100
    print(desconto)
    valor_final = total * desconto
    print(f'Valor total: {valor_final:.2f}')


main()