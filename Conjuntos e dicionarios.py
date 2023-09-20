# funcionamento do conjunto

# o conjunto é uma coleção de elementos únicos e não ordenados

exe_Conju = {10, 20, 30, 40, 50}

# não necesáriamente o add vai adicionar o elemento na última posição do conjunto já que o mesmo é desordenado
exe_Conju.add(60)

# para se remover um elemento não chamamos o seu índice e sim o seu valor
exe_Conju.remove(10)

# os elementos de um conjunto podem ser strings ou números

exe_Conju.add("Palavra")

# if "Palavra" in exe_Conju:
#     print("sim temos este elemento no conjunto")
#     print(exe_Conju)
# else:
#     print("não tem este elemento no conjunto")

# for numero in exe_Conju:
#     print(numero)



# dicíonários
#  um dicionário é um array, que possui chave e valor

meu_dici = {"nome": "Lucas", "idade": "28", "cidade": "Campo Belo"}

# para puxar uma informação de um array ou dicionário eu posso atribuir o valor a uma variável ou puxar pelo "indice da chave"
# ex por variável
nomeuser = meu_dici["nome"]
print(nomeuser)

# ex indice da chave
print(meu_dici["cidade"])

# para adicionar um novo elemento preciso criar a palavra chave depois dar a ela um valor

meu_dici["profissão"] = "Desenvolvedor"

print(meu_dici["profissão"])

# para remover um elemento preciso usar o del e a palavra chave

del meu_dici["idade"]

if "idade" in meu_dici:
    print("este dicionário possui a informação idade que é " + meu_dici["idade"])
else:
    print("este dicionário não possui a informação idade")


