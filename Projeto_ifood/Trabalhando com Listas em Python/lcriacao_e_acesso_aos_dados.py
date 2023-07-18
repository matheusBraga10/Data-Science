# Exemplos de Listas em Python

#Forma mais comum de listas
frutas = ['laranja','maca','uva']
print(frutas)

# Lista vazia
fruta = []
print(fruta)

# Lista onde cada uma das letras é um elemento em separado
letras = list('python')
print(letras)

# Mesmo acima, só que tipo enumerada
numeros = list(range(10))
print(numeros)

# Exemplo de lista com diferentes tipos de dados (strings, inteiros, floats, boleanos)
carro = ['Ferrari','F8', 42000000.00, 2020, 2900, 'São Paulo', True]
print(carro)
print()
#---------------------------------------------------------------------------
# Acessando os dados de uma lista

print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-3])
print()
#---------------------------------------------------------------------------
# Listas Aninhadas
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print()
#----------------------------------------------------------------------------
# Fatiamento em Python
lista = ['p','y','t','h','o','n']

print(lista[2:]) # Início : Fim : Passo
print(lista[:2]) # Start : Stop : Step
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])
print()
#----------------------------------------------------------------------------
# Percorrendo Listas
carros = ['gol','celta','palio']

for cada_item in carros:
    print(cada_item)
print()
#-----------------------------------------------------------------------------
# Enumerando itens de uma lista

for indice, cada_item in enumerate(carros):
    print(f'{indice}: {cada_item}')
print()
#-----------------------------------------------------------------------------
# Compreensão de listas - Filtrando listas
numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) # append cria a nova lista
print(pares)
print()

# Modificando valores versão 1
quadrado = []

for numero in numeros:
    quadrado.append(numero **2)
print(quadrado)
print()

# Filtro versão 2 (melhor)
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)
print()

# Modificando versão 2 (melhor)
quadrado2 = [numero **2 for numero in numeros]
print(quadrado2)
print()


