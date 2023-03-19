'''
EXERCÍCIO PROPOSTO

1. Crie uma classe animal com atributos e métodos, posteriormente, crie uma classe que herde seus atributos, 
e possua os seus atributos próprios. 
2. Crie dois objetos da classe filha.
'''

# 1.
class Animal():
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo

class Gato(Animal):
    def __init__(self, nome, sexo, peso):
        super().__init__(nome, sexo)
        self.peso = peso

# 2.
gato1 = Gato('Bob', 'Macho', 5.2)
gato2 = Gato('Kate', 'Fêmea', 3.5)

print(vars(gato1))
print(vars(gato2))