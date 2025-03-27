#  7. Escribe una función llamada remove_duplicates que acepte una lista como parámetro 
# y devuelva una nueva lista sin elementos duplicados.
def remove_duplicates(lst):
    return list(set(lst))

# Ejemplo de uso
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  
print(remove_duplicates(["a", "b", "a", "c", "d", "c"])) 
