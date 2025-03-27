#2. Escribe una función llamada find_median que acepte un array de enteros como parámetro y devuelva la mediana del conjunto.
def find_median(arr):
    arr.sort()  # Ordenar el array
    n = len(arr)
    mid = n // 2

    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid]) / 2

print(find_median([3, 1, 4, 2, 5]))  
print(find_median([7, 8, 3, 5]))  