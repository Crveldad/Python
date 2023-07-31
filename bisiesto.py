# Cómo determinar si un año es un año bisiesto

# Para determinar si un año es bisiesto, siga estos pasos:

#   1  Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
#   2  Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
#   3  Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
#   4  El año es un año bisiesto (tiene 366 días).
#   5  El año no es un año bisiesto (tiene 365 días).


# def bisiesto(ano):
#     if ano % 4 == 0:
#         if ano % 100 == 0:
#             if ano % 400 == 0:
#                 print("El año",ano,"es bisiesto")
#             else: 
#                 print("El año",ano,"es no bisiesto")
#         else: 
#             print("El año",ano,"es no bisiesto")
#     else: 
#         print("El año",ano,"es no bisiesto")

def bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("es")
    else:
        print("no es")

bisiesto(2000)
bisiesto(1997)
bisiesto(1936)