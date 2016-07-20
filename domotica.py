from mando import Mando


ventiladorDormitorio = Mando()
ventiladorSalon = Mando()

ventiladorDormitorio.set_velocidad(30)

ventiladorDormitorio.logger()
print ""
print ""
ventiladorSalon.logger()

