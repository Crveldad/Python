import operaciones.ope

def principal():
    sum = operaciones.ope.Sumador()
    print("la suma es",sum.suma(5,18))

    res = operaciones.ope.Restador()
    print("la resta es",res.resta(5,18))

    mul = operaciones.ope.Multiplicador()
    print("la multiplicación es",mul.multiplicacion(5,18))

    div = operaciones.ope.Divisor()
    print("la división es",div.division(5,18))    

if __name__ == '__main__':
    principal()