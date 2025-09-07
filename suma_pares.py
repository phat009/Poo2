def suma_pares_impares(n):
    suma_par = 0
    suma_imp = 0
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma_par += i
        else:
            suma_imp += i
    
    return suma_par, suma_imp
n = int(input("Ingrese un número entero positivo: "))
pares, impares = suma_pares_impares(n)
print(f"Suma de los pares hasta {n}: {pares}")
print(f"Suma de los impares hasta {n}: {impares}")