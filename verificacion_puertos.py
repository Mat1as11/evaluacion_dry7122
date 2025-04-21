print("***************************")
print("**Verificacion De Puertos**")
print("***************************")

try:
# Solicitar Numero de Puerto
    puerto = int(input("Ingrese El Numero de Puerto: "))

    # Vereficar el Rango del Puerto
    if puerto >= 0 and puerto <= 1023:
        print(f"El puerto {puerto} es un Puerto Bien Conocido (0 / 1023)")
    elif puerto >= 1024 and {puerto} <= 49151 :
        print(f"El puerto {puerto} es un Puerto Registrado (1024 / 49151)")
    elif puerto >= 49152 and {puerto} <= 65535:
        print(f"El Puerto {puerto} es un Puerto Dinamico / Privada (49152 / 65535)")
    else:
        print("¡ERROR! El Numero Ingresado Se Encuentra Fuera Del Rango (0 / 65535)")
except ValueError:
    print("¡ERROR! Debe Ingresar un Numero Valido")

print("\nFin Del Proceso")