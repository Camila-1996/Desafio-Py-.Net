# 1. Escribe una función llamada merge_arrays que acepte dos 
# arrays ordenados de enteros como parámetros y devuelva un solo 
# array ordenado que contenga todos los elementos de ambos.
def merge_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    # Mezclar los dos arrays ordenadamente
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Agregar los elementos restantes de arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Agregar los elementos restantes de arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge_arrays(arr1, arr2)) 
