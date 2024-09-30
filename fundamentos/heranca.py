# Classe base (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        return "O animal faz um som"

# Classe derivada (subclasse) que herda de Animal
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama o construtor da classe base
        self.raca = raca

    def som(self):  # Sobrescreve o método som da classe base
        return "O cachorro late"

# Outra classe derivada
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def som(self):  # Sobrescreve o método som
        return "O gato mia"

# Criando objetos das classes derivadas
cachorro = Cachorro("Rex", "Labrador")
gato = Gato("Mimi", "Branco")

# Usando os métodos
print(f"{cachorro.nome} ({cachorro.raca}) faz: {cachorro.som()}")
print(f"{gato.nome} ({gato.cor}) faz: {gato.som()}")
