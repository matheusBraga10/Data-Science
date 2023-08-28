texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')
else:
    print('Executa no final do laço')
print() #adiciona quebra de linha

#----------------------------------------------------------
for numero in range (0,11,2): # exibindo numeros de 0 a 10, numeros pares
    print(numero, end=' ') # end=' ' imprime na mesma linha (sem quebra) os laços dentro da indentação
print()

#----------------------------------------------------------
opcao = -1

while opcao != 0:
    opcao = int(input('\n[1] Saque\n[2] Extrato\n[0] Sair\n'))
    
    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
    elif opcao != 1 and opcao != 2:
        print('Opção inválida. Tente novamente.')

print('Saindo do programa')

#------------------------------------------------------------
for numero in range(100): # Numeros impares
    if numero % 2 == 0:
        continue
    print(numero, end=' ')