def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if "lado" in prompt and value > 0:
                return value
            elif "lado" in prompt:
                print("Por favor, introduce un número positivo.")
            else:
                return value
        except ValueError:
            print("Por favor, introduce un número válido.")


def main():
    funcionando = True
    while funcionando:
        ladoA = get_valid_number("Escribe el primer lado del triángulo: ")
        ladoB = get_valid_number("Escribe el segundo lado del triángulo: ")
        ladoC = get_valid_number("Escribe el tercer lado del triángulo: ")

        if ladoA == ladoB == ladoC:
            print("El triángulo es equilátero.")
        elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

        while True:
            respuesta = input("¿Quieres comprobar otro triángulo? (s/n): ").lower()
            if respuesta == "s":
                break
            elif respuesta == "n":
                funcionando = False
                break
            else:
                print("Por favor, introduce 's' para sí o 'n' para no.")


if __name__ == "__main__":
    main()
