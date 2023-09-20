# funções sem parâmetros
# são blocos de código que podem se repetir no decorrer do projeto e para isto é mais facil apenas chamar a função desejada e executar a tarefa sem a necessidade de criar o código novamente
def minhafunc():
     total = 2 + 2
     tt = 5 * 5
# OBS: quando uma função precisa retornar algum valor quando for chamada é necessário o return
     return total, tt

print(minhafunc())


#  funções com parâmetros
# funções com parâmetros precisam conter argumentos quando as mesmas são chamadas, e um return para retonar o valor esperado.
def func2 (a, b):
     return a + b
# exemplo de argumento
print(func2(4, 8))

def func3 (text1, text2):
     return text1 + text2

print(func3("aqui ","esta"))