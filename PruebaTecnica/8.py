# 8. Dada una lista de números en orden ascendente y un número objetivo, escribe una función 
# recursiva que encuentre si el número objetivo está en la lista utilizando una búsqueda binaria.
from concurrent.futures import ThreadPoolExecutor

def binary_search_recursive(arr, target, left=0, right=None):
    """Realiza una búsqueda binaria recursiva para encontrar el número objetivo en una lista ordenada."""
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

def parallel_search(sorted_list, search_list, max_workers=4):
    """Busca en paralelo cada número de search_list dentro de sorted_list utilizando búsqueda binaria."""
    results = {}

    # Usamos ThreadPoolExecutor para realizar búsquedas en paralelo
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_number = {executor.submit(binary_search_recursive, sorted_list, num): num for num in search_list}
        
        for future in future_to_number:
            num = future_to_number[future]
            try:
                results[num] = future.result()
            except Exception as e:
                results[num] = f"Error: {e}"

    return results

# Ejemplo de uso
sorted_numbers = list(range(1_000_000))  # Lista ordenada muy grande
search_numbers = [10, 5000, 999999, 1000001]  # Algunos números a buscar

result = parallel_search(sorted_numbers, search_numbers, max_workers=8)
print(result)

