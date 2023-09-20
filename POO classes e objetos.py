# Classes são como uma caixa de presentes, onde tem espaços definidos que são chamados de atributos
# ex de classe
class Carro:
    # aqui definimos que a classe carro possui dois atributos dentro de si, que no caso são as marcas, e as cores
    def __init__(self, marca, cor):
        # aqui temos atributos desta classe.
        self.marca = marca
        self.cor = cor

    # aqui podemos ver os métodos que a classe possui e podemos reparar algo intrigante, que mesmo o objeto sendo declarado fora da classe e posterior a ela, nós ainda conseguimos realizar a chamada do mesmo dentro da classe.
    def modelo1(self):
        print(f"O carro da {carro1.marca} possui a cor {carro1.cor}")
    def modelo2(self):
        print(f"O carro da {carro2.marca} possui a cor {carro2.cor}")

# aqui temos a definição de dois objetos, que vão para a mesma classe.
# a classe 'Carro'
carro1 = Carro("Toyota", "Vermelho")
carro2 = Carro("Renew", "Azul")

# aqui foi somente um ponto de escolha para analisar o comportamento da classe e objeto.
selectcarro = input("Entre com o carro desejado")
if selectcarro == "a":
     carro1.modelo1()
else:
     carro2.modelo2() 