# 6. Escribe un programa que pida tu edad y muestre si es mayor de edad o no lo es.
edad = int(input("Ingrese su edad: "))
if edad < 1:
    print("La edad debe ser un número positivo mayor o igual a 1.")
elif edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")