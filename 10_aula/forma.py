class Forma:
    def __init__(self,nome):
      self.nome = nome

    def calcula_Area(self):
        raise NotImplementedError("O método deve ser implementado subclasse")

    def calcular_Perimetro(self):
        raise NotImplementedError("O método deve ser implementado em subclasse")

    def __str__(self):
        return f"Nome : {self.nome}"