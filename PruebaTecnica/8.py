# 8. Dada una lista de números en orden ascendente y un número objetivo, escribe una función 
# recursiva que encuentre si el número objetivo está en la lista utilizando una búsqueda binaria.
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return False  # El número no está en la lista

    mid = (left + right) // 2  # Calcula el índice medio

    if arr[mid] == target:
        return True  # Se encontró el número
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)  # Buscar en la derecha
    else:
        return binary_search_recursive(arr, target, left, mid - 1)  # Buscar en la izquierda

# Ejemplo de uso
nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search_recursive(nums, 7))  # True
print(binary_search_recursive(nums, 2))  # False
