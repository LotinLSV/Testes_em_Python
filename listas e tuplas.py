# exemplos de lista

# métodos para adicionar/editar itens da lista

# uma lista pode ser mudada seus parametros tanto removidos, quanto adicionados ou modificados

lista_Compras = ["Arroz", "Macarrão", "Batata", "Abacaxi"]

# posso trocar o valor de uma lista utilizando de um indice que começa do valor 0 e dando um novo valor para o mesmo
lista_Compras[2] = "Carne muida"

lista_Compras[3] = 7 * 2

print(lista_Compras[2])
print(lista_Compras)


# append serve para adicionar um elemento a lista OBS: este elemento vai estar na ultima posição

lista_Compras.append("Pimenta")
print(lista_Compras)

# Método insert(): O método insert() permite adicionar um elemento em uma posição específica da lista, especificando o índice desejado.

minha_lista = [1, 2, 3]
minha_lista.insert(2, 4)  # Insere o número 4 no índice 1
print(minha_lista)  # Output: [1, 4, 2, 3]



# métodos para remover um item da lista

# o remove serve para remover a primeira ocorrencia de uma valor na lista

lista_Exe = [10, 20, 30, 40, 50, 60, 50]

lista_Exe.remove(50)
print(lista_Exe)

# o pop serve para recortar o valor, podendo salvar em outra varíavel ou até mesmo em outra lista
recebe_lis_exe = lista_Exe.pop(1)
print(lista_Exe)
print(recebe_lis_exe)


# com o del eu posso remover um item com base no índice da lista
del lista_Exe[3]
print(lista_Exe)


# exemplo de tupla

# Tuplas não diferentemente das listas não podem ter seus valores alterados depois de criada 

tupla_compras = ("Feijão", "Abóbora", "Repolho", "Brócolis")

tupla_compras[1] = "Pepino"

print(tupla_compras[1])



