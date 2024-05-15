def main():
    print("Angel González 1180724")
    metros = float(input("Ingresa la cantidad en metros: "))
    millas = metros / 1609.34
    kilometros = metros / 1000
    pies = metros * 3.28084
    pulgadas = metros * 39.3701
    print(metros, "metros equivalen a:")
    print(millas, "millas")
    print(kilometros, "kilómetros")
    print(pies, "pies")
    print(pulgadas, "pulgadas")
if __name__ == "__main__":
    main()