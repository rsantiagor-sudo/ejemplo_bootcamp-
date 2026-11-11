""" ESTRUCTURA REPITITIVA (CICLO) WHILE """

# EJEMPLO UNO
# 1. Imprimir o ejecutar 10 veces la palabra "Python"

# Primero creo una variable que me va a almacenar
# el numero de veces la palabra python, en este
# caso comenzando desde la pocision 1 
#print()
#x = 1

# Despues de tener deinida la variable, se
# procede a realizar la estructura while, preguntado
# a partir de la poision 1

#while x <= 10:
    #print(f"{x}. PYTHON")

# Si la variable cumple la condicion de la estructura
# y esta es "TRUE", entonces ejecuta la primera parte
# luego realiza un aumento en la variable para seguir
# preguntado con el siguiente numero; para esto se 
# crea un contador que me aumente al siguiente numero.

    #x = x + 1
#print()

# --------------------------------------------------------------------------------------------------

# EJEMPLO DOS
# 2. MUESTRE LOS NUMEROS DEL 1-10

#print()

#x = 1
#while x <= 10:
    #print(f"Numero {x}")
    #x = x+1
#print()
# ----------------------------------------------------------------------------------------------

# EJEMPLO DOS-UNO
# 2.1

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          0  1  2  3  4  5  6  7  8  9

#indice = 0

#while indice < len(numeros):

    #numero = numeros[indice]

    #print(f"{numero}")

    #indice += 1
#print()
# -------------------------------------------------------------------------------------------

# EJEMPLO TRES
# 3. Ejecutar la numeracion descendentemente 10-1

print("-"*47)
print("CUENTA REGRESIVA")
print()

num = 10


while num >= 1:
    
    print(f" Numero {num}")

    num = num -1







