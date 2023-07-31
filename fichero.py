# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.

def main():
    
    f = open('archivo.txt', 'a')

    f.write("ahsjbsdakj\n")
    f.write("jhdashvdassdas\n")
    f.write("jhdashvdassdas\n")
    f.write("jsdeff\n")
    f.write("etewrererty\n")

    f.close()

    print("Hemos escrito en el fichero")

if __name__ == '__main__':
    main()