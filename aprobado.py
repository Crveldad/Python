# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota.
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

from random import randrange

class ListaNombres:
    pass

class Alumno:
    nombre = ListaNombres
    nota = randrange(10)

    def aprobadoSuspenso(nota):
        if nota >= 5:
            return "aprobado"
        else:
            return "suspenso"

    def mostrarInformacion(nombre, nota):
        print("El alumno", Alumno.nombre,"ha sacado una nota de", Alumno.nota, "y está", Alumno.aprobadoSuspenso(nota))

a1 = Alumno()
a1.mostrarInformacion("Pepe",1)