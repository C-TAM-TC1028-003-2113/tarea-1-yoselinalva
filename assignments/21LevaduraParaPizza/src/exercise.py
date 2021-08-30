def main():
    # Datos solicitados al usuario
    harina = float(input("Dame la harina en gramos: "))

    # Operaciones
    levadura = (harina * 50)/1000

    # Muestra del resultado
    print("Necesitas estos gramos de levadura:", levadura)

if __name__ == '__main__':
    main()
