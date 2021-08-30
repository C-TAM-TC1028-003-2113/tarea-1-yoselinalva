# coding=utf-8
def main():
    # Datos solicitados al usuario
    nuevo = int(input("Dame la cantidad de juegos nuevos: "))
    usado = int(input("Dame la cantidad de juegos usados: "))

    # Fórmula para sacar el costo a cobrar al usario
    total = (nuevo * 1000) + (usado * 350)

    # Muestra del resultado final al usuario
    print("El total de la compra es:", total)

if __name__ == '__main__':
    main()
