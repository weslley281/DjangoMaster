# Classe base
class Animal:
    def som(self):
        raise NotImplementedError("Subclass deve implementar este método")

# Classes derivadas implementam o método som
class Cachorro(Animal):
    def som(self):
        return "O cachorro late"

class Gato(Animal):
    def som(self):
        return "O gato mia"

class Vaca(Animal):
    def som(self):
        return "A vaca muge"

# Função que usa polimorfismo
def fazer_som(animal):
    print(animal.som())

# Criando instâncias das classes derivadas
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

# Usando o polimorfismo
fazer_som(cachorro)  # Saída: O cachorro late
fazer_som(gato)      # Saída: O gato mia
fazer_som(vaca)      # Saída: A vaca muge
