#Autor : Javier Orellana
num1 = float(input("Ingrese el primer numeno "))
num2 = float(input("Ingrese el segundo numero "))

print("Opciones:")
print("a) Sumarlos")
print("b) Restarlos")
print("c) Dividirlos")
print("d) Multiplicarlos")
print("e) Elevar")
print("f) Salir")

opcion = input("Ingrese opción:")
opcion = opcion.strip()

if(opcion == "a" or opcion == "A"):
    suma = num1 + num2
    print("La suma es: ", suma)
else:
    if(opcion == "b" or opcion == "B"):
        resta = num1 - num2
        print("La resta es:", resta)
    if(opcion == "c " or opcion == "C"):
        dividir = num1 / num2
        print("El resultado de la divicion es: ",dividir)
    if(opcion == "d" or opcion == "D"):
        multiplicar = num1 * num2
        print("La multiplicacion es" , multiplicar)
    if(opcion == "e" or opcion == "E"):
        elevar = num1 ** num2
        print("Al elevar estos numeros el resultado es :",elevar)
    if (opcion == "f" or opcion =="F"):
        breakpoint()
