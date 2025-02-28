#Autor: Zunni Rojas Baldivia
#Conversor de numeros decimales a numeros romanos

#Esta funcion recibe un parámetro el cual es el número decimal que queremos convertir a romano.
def decimal_a_romano(numero_decimal):
    if not (1 <= numero_decimal <= 3999):
        return "\nERROR El número debe estar entre 1 y 3999"

#Lista de tuplas ordenada de mayor a menor para restar correctamente al recorrer
    tuplas_decimal_romanos = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
#Variable con una cadena vacia que almacenara el resultado de nuestro ciclo	
    resultado = ""
    for decimal, romano in tuplas_decimal_romanos:
        while numero_decimal >= decimal:
            resultado += romano
            numero_decimal -= decimal
    
    return resultado

#1937 -> M -> 937 -> CM -> 37 -> X -> 27 -> X -> 17 -> X -> 7 -> V -> 2 -> I -> 1 -> I -> 0

numero_usuario = int(input("Ingresa un numero decimal entre 1 y 3999: "))
print(f"El numero {numero_usuario} en numeros romanos es: {decimal_a_romano(numero_usuario)}")
