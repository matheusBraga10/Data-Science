# [].append
lista = []
lista.append(1)
lista.append('Python')
lista.append([40,30,20])

print(lista)
print()
#--------------------------------------------------
# [].clear
print(lista)

lista.clear()

print(lista)
print()
#--------------------------------------------------
# [].copy
lista = [1,'Python', [40,30,20]]

l_2 = lista.copy()

print(id(l_2), id(lista)) # Cópia de listas

lista[0] = 'alteração'

print(lista, l_2) # A cópia não permite alteração posterior
print()
#--------------------------------------------------
# [].count
cores = ['vermelho','azul','verde','azul']

print(cores.count('vermelho'))
print(cores.count('azul')) # Conta o numero de vezes que os resultados se repetem na lista
print(cores.count('verde'))
print()
#--------------------------------------------------
# [].extend
linguagens = ['python','js','c']

print(linguagens)

linguagens.extend(['java','csharp']) # Adiciona elementos 

print(linguagens) 
print()
#--------------------------------------------------
# [].index
print(linguagens.index('java'))
print(linguagens.index('python'))
print()
#--------------------------------------------------
# [].pop - Retira o ultimo elemento da lista (pilha) ou retira o elemento que você disser
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

print()
#--------------------------------------------------
# [].remove
linguagens = ['python','js','c','java','csharp']
linguagens.remove('c')
print(linguagens)

print()
#--------------------------------------------------
# [].reverse - Transpor a lista
linguagens.reverse()
print(linguagens)

print()
#--------------------------------------------------
# [].sort
linguagens.sort() # Ordem crescente e/ou alfabetica
print(linguagens)

linguagens.sort(reverse=True) # Ordem inversa
print(linguagens)

linguagens.sort(key=lambda x: len(x)) # Ordem por tamanho de palavra
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

print()
#--------------------------------------------------
# len
print(len(linguagens)) # Tamanho da lista
