class Ventilador(object):
    """
        Esta clase controla la velocidad y tiempo de apagado
        de un ventilador
    """


    # Declaramos y inializamos las variables del ventilador
    velocidad = 0
    temporizador = 0
    estado_ventilador = False
    estado_luz = False


    ## Establecer  = set
    ## Obtener     = get


    def get_velocidad(self):
        return self.velocidad

    def get_temporizador(self):
        return self.temporizador

    def get_estado_ventilador(self):
        return self.estado_ventilador

    def get_estado_luz(self):
        return self.estado_luz

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_temporizador(self, segundos):
        self.temporizador = segundos

    def set_estado_ventilador(self, on_off):
        self.estado_ventilador = on_off

    def set_estado_luz(self, on_off):
        self.estado_luz = on_off

    # manda todos los datos
    def logger(self):
        enter = "\n"

        datos = "Velocidad: " + str(self.velocidad) + enter
        datos += "Temporizador: " + str(self.temporizador) + enter
        datos += "Estado luz: " + str(self.estado_ventilador) + enter
        datos += "Estado ventilador: " + str(self.estado_luz)

        return datos



if "__main__" == __name__:
    ventilador = Mando() # Instanciamos la clase Mando y llamamos al objeto "ventilador"

    # velocidad_actual = ventilador.get_velocidad()
    ventilador.logger()
    #ventilador.set_velocidad(34)
    #print ventilador.logger()
