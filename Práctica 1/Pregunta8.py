# 8. Escribe un programa que pida un numero entero y calcule la suma de 1 hasta el numero ingresado.
n = int(input("Ingrese un número entero positivo: "))
if n < 1:
    print("El número debe ser positivo y mayor o igual a 1.")
else:
    suma = n * (n + 1) / 2  
    print(f"La suma de los números de 1 hasta {n} es {int(suma)}.")