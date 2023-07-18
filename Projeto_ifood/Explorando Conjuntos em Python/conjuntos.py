# conjunto é uma coleção de objetos que não se repetem.
# Usamos 'set' para representar conjuntos ou eliminar itens duplicados

print(set([1,2,3,4,2,3,1,4]))
print()

print(set('abacaxi'))
print()

print(set(('palio','gol','celta','palio')))
print()

#Outra forma de declarar conjuntos
linguagens = {'python','java','python'}
print(linguagens)
print()

#-------------------------------------------------------
# Acessando os dados (conjuntos não suportam indexação e nem fatiamento)
# Para ter acesso aos dados, precisamos de converter o conjunto para listas

numeros = {1,2,3,4,2,3,4}
print(numeros[0]) # Dá erro, pois o conjunto não permite
numeros = list(numeros)

# Acessando dados após a conversão
print(numeros[0])
print()
#-------------------------------------------------------
# Iterar conjuntos - for
for numero in numeros:
    print(numero)
print()
#-------------------------------------------------------
# Função enumerate
for indice, numero in enumerate(numeros):
    print(f'{indice}: {numero}')
print()
print()
#-------------------------------------------------------
# {}.union - União
cunjunto_a = {1,2}
cunjunto_b = {2,3,4}

print(conjunto_a.union(conjunto_b)) 
print()
#-------------------------------------------------------
# {}.intersection - Interseção
print(conjunto_a.intersection(conjunto_b))
print()
#-------------------------------------------------------
# {}.difference - Diferença
print(conjunto_a.difference(conjunto_b))
print()
#-------------------------------------------------------
# {}.symmetric_difference - Diferença Simétrica
print(conjunto_a.symmetric_difference(conjunto_b))
print()
#-------------------------------------------------------
# {}.issubset - A Está contido em B 
print(conjunto_a.issubset(conjunto_b))
print()
#-------------------------------------------------------
# {}.issuperset - B contém A 
print(conjunto_a.issuperset(conjunto_b))
print()
#-------------------------------------------------------
# {}.isdisjoint - Conjunto Disjunto
print(conjunto_a.isdisjoint(conjunto_b))
print()
#-------------------------------------------------------
# {}.add
print(conjunto_a.add(conjunto_b))
print()
#-------------------------------------------------------
# {}.clear
print(conjunto_a.clear())
print()
#-------------------------------------------------------
# {}.copy
print(conjunto_a.copy())
print()
#-------------------------------------------------------
# {}.discard
print(conjunto_a.discard(1))
print()
#-------------------------------------------------------
# {}.pop
print(conjunto_a.pop())
print()
#-------------------------------------------------------
# {}.remove
print(conjunto_a.remove(1))
print()
#-------------------------------------------------------
# {}.len
len(conjunto_a)
print()
#-------------------------------------------------------
# {}.in
in(conjunto_a)










