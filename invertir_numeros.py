def invertir_digitos(numero):
    numero_str = str(numero)
    
    if numero_str[0] == '-':
        numero_invertido = '-' + numero_str[:0:-1]
    else:
        numero_invertido = numero_str[::-1]
    
    return int(numero_invertido)
numero = int(input("Ingrese un número entero: "))
print("Número invertido:", invertir_digitos(numero))