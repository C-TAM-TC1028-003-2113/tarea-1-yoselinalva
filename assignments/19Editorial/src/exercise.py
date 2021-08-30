# coding=utf-8
def main():
    # Datos solicitados al usuario
    import math
    palabras = int(input("Dame el número de palabras: "))
    cuartilla = int(math.ceil(palabras / 475))

    # Operaciones para calcular el precio
    precio = (cuartilla * 60)
    preciofinal = precio - (precio * 0.10)

    # Muestra del costo de la publicación al usuario
    print("El costo de la publicación es:", preciofinal)


if __name__ == '__main__':
    main()
