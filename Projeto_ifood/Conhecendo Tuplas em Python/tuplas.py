# Tupla - Irmã da lista
# Tuplas são estruturas imutáveis (diferentes das listas que são mutáveis)

frutas = ('laranja','pera','uva',) #declarar com ',' extra ao final

letras = tuple('python')

numeros = tuple([1,2,3,4])

pais = ('Brasil',)

#-----------------------------------------------------------
print(frutas[0])
print(frutas[2])
print(frutas[-1])

print()
#-----------------------------------------------------------
# Tuplas Aninhadas

matriz = (
    (1,'a',2),
    ('b',3,4,),
    (6,5,'c'),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

print()
#-----------------------------------------------------------
# Fatiamento de Tuplas
tupla = ('p','y','t','h','o','n',) # declarar ',' extra ao final

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])


print()
#-----------------------------------------------------------
# Tentando alterar a tupla

tup = (1,3,)

tup[0] = 2

print(tup)

print()
#-----------------------------------------------------------
# Interações são iguais às listas


print()
#-----------------------------------------------------------
# Métodos da classe tuple
#().count
cores = ('vermelho','azul','verde','azul',)

print(cores.count('vermelho'))
print(cores.count('azul'))
print(cores.count('verde'))
print()

#().index
print(cores.index('verde'))
print()

#().len
print(len(cores))
