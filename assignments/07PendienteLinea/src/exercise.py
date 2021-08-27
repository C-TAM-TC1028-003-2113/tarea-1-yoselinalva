def main():
    # Datos iniciales
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    # Calculo de la pendiente
    m = (y2 - y1) / (x2 - x1)
    # Muestro del resultado final al usuario
    print("Pendiente:", m)


if __name__ == '__main__':
    main()
