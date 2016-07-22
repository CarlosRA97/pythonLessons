class Luces(object):

    luz_estado = False
    luz_potencia = 0

    def get_potencia_luz(self):
        return self.luz_potencia

    def set_potencia_luz(self, potencia):
        self.luz_potencia = potencia

    def get_luz_estado(self):
        return self.luz_estado

    def set_luz_estado(self, on_off):
        self.luz_estado = on_off


    def logger(self):
        enter = "\n"
        
        datos = "Estado de luces: " + str(self.luz_estado) + enter
        datos += "Potencia de luz: " + str(self.luz_potencia)
        
        return datos