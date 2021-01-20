# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("hola")



def suma(num1, num2):
    # print(num1+num2)
    resultado = num1 + num2

    return resultado


almacena_suma = suma(3, 3)

print(suma(10, 10))

print(suma(7, 5))
print(suma(20, 65))
print(suma(345, 2353))

print(almacena_suma)
miLista = ["Boca", "Riber", "Banfield", "Lanus"]
miLista.append("chacarita")
miLista.extend("1")
miLista.pop(1)
print(miLista.index("Boca"))
print(miLista)

diccionario = {}
diccionario["Boca"] = 69
print(diccionario.get("Boca"))




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
