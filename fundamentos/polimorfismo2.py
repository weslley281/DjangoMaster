class Forma():

    def area(self):
        pass


class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    

quadrado = Quadrado(lado=5)
print(quadrado.area())

quadrado = Quadrado(lado=80)
print(quadrado.area())