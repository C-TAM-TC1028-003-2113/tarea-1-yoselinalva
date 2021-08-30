# coding=utf-8
def main():
    # Datos solicitados al usuario
    mensaje = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))

    # Fórmula para sacar el coso
    costo = float(mensaje + megas + minutos) * 0.80

# Muestra del resultado final al usuario
print("El costo mensual es:", costo)

if __name__ == '__main__':
    main()