# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    
    def __init__(self, color, motor, precio) -> None:
        self.color = color
        self.motor = motor
        self.precio = precio

    def __str__(self) -> str:
        return "Es de color azul " + self.color + "\nEs de motor " + self.motor + "\nY cuesta " + self.precio + " €"
    
c1 = Vehiculo("azul marino", "diésel", "3500")
print(c1)

# crear el bin
# f = open('coche.bin', 'wb')
# pickle.dump(c1,f)
# f.close()

l = open('coche.bin','rb')
pickle.load(l)
l.close()


