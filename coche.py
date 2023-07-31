# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

# Color

# Ruedas

# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

# Velocidad

# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo():
    color = ""
    ruedas = 4
    puertas = 3

class Coche(Vehiculo):
    velocidad = 170
    cilindrada = 144

c = Coche()
print(c.cilindrada)
print(c.velocidad)