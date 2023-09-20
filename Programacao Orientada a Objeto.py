# class usuario:
#     def __init__ (self):
#         self.nome = "Lucas"
#         self.idade = 28
#         self.sexo = "M"


# User = usuario()
# print("Olá meu nome é " +  User.nome + " minha idade é de " + User.idade + " e meu sexo é do tipo " + User.sexo)

class usuario:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def nomeUser(self):
        print(f"Meu nome é {self.nome}")
    def idadeUser(self):
        print(f"Minha idade é {self.idade}")

dadosUser = usuario("Lucas", 28, "M")

dadosUser.nomeUser()