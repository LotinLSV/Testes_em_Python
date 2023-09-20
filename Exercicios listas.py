

# Declarar função
def maiorls(lista):

# duas variaveis uma menor e outra maior vão receber o mesmo valor
    maiorvl = lista[0]
    menorvl = lista[0]
# busco pelos valores e salvo o maior  e menor nas variáveis
    for valor in lista:
        if valor > maiorvl:
         maiorvl = valor;
        if valor < menorvl:
         menorvl = valor
# retorno os valores maior e menor
    return maiorvl, menorvl
# crio a lista
cr_list = [10, 20, 30, 40, 70, 25]

# atribuo os valores de menor e maior dentro dos repectivos valores maior/menor que saem da função
maior, menor = maiorls(cr_list)

#  utilizo , para concatenar entre string e interiro
print("o maior valor é: " , maior)
print("o menor valor é: " , menor)





