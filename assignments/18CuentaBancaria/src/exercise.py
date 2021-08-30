# coding=utf-8
def main():
    # Datos solicitados al usuario
    anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheque = int(input("Dame el número de cheques: "))

    # Suma de las cantidades
    total1 = (anterior + ingresos - egresos) - (cheque*13)

    # Operaciones para sacar el total
    total2 = total1 - (total1 * 0.075)

    # Muestra del resultado final al usuario
    print("El saldo final de la cuenta es: ", total2)

if __name__ == '__main__':
    main()
