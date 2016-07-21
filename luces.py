class Luces(object):

    luz_estado = False
    luz_potencia = 0

    @property
    def get_potencia_luz(self):
        return self.luz_potencia

    def set_potencia_luz(self, potencia):
        self.luz_potencia = potencia




print Luces().get_potencia_luz
print Luces().luz_potencia