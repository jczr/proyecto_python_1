operacion = ""

while operacion != "salir":
    operacion = input("Ingrese la operacion: ")

    if operacion == "+":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == "-":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == "*":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese elsegundo numero: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif operacion == "/":
        try:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
        
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"El resultado de la division es: {resultado}")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
    elif operacion == "salir":
        print("Gracias por usar la calculadora, ¡hasta pronto!")
        exit()
    else:
        print("Operacion no valida, reitentalo")

