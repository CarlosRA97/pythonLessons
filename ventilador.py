class Ventilador(object):
    """
        Esta clase controla la velocidad y tiempo de apagado
        de un ventilador
    """


    # Declaramos y inializamos la velocidad del ventilador
    velocidad = 0
    temporizador = 0
    ventilador_on_off = False
    luz_on_off = False


    ## Establecer  = set
    ## Obtener     = get


    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def get_estado_luz(self):
        return self.luz_on_off

    def set_estado_luz(self, on_off):
        self.luz_on_off = on_off

    def get_temporizador(self):
        return self.temporizador

    def set_temporizador(self, segundos):
        self.temporizador = segundos

    def set_ventilador_on_off(self, on_off):
        self.ventilador_on_off = on_off

    # manda todos los datos
    def logger(self):
        enter = "\n"

        datos = "Velocidad: " + str(self.velocidad) + enter
        datos += "Temporizador: " + str(self.temporizador) + enter
        datos += "Estado luz: " + str(self.ventilador_on_off) + enter
        datos += "Estado ventilador: " + str(self.luz_on_off)

        return datos



if "__main__" == __name__:
    ventilador = Mando() # Instanciamos la clase Mando y llamamos al objeto "ventilador"

    # velocidad_actual = ventilador.get_velocidad()
    ventilador.logger()
    #ventilador.set_velocidad(34)
    #print ventilador.logger()
