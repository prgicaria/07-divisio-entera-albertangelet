dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
if divisor == 0:
    print("Error: no es pot dividir entre zero.")
else:
    divisio = dividend / divisor
    quocient = dividend // divisor
    residu = dividend % divisor

    # Mostrar els resultats
    print(f"Divisió: {dividend} / {divisor} = {divisio}")
    print(f"Quocient: {quocient}")
    print(f"Residu: {residu}")