import datetime

def main():
    horaActual = datetime.datetime.now().strftime('%H:%M')
    hora = datetime.datetime.now().time().hour
    minutos = datetime.datetime.now().time().minute

    if hora >= 19:
        print("Es hora de irte")
    elif hora == 18:
        print("te queda ya poco", (60-minutos),"minutos")
    else:
        print("aún te quedan", (19-hora), "horas" )
    print(horaActual)

if __name__ == '__main__':
    main()