# Proyecto: Implementaciones de Algoritmos en Python, JavaScript y .NET

## Descripción
Este proyecto contiene la implementación de varios algoritmos fundamentales en diferentes lenguajes de programación: Python, JavaScript y .NET.
Se incluyen funciones para la manipulación de listas, búsqueda binaria, árboles binarios y algoritmos de ordenamiento.

## Requisitos de Implementación
### 1. Implementaciones en **Python 3**
- `merge_arrays(arr1, arr2)`: Fusiona dos arreglos ordenados en un solo arreglo ordenado.
- ![image](https://github.com/user-attachments/assets/d65a9aa0-51b5-4859-83a3-8ac2f16e55dc)

- `find_median(arr)`: Devuelve la mediana de un conjunto de números enteros.
- ![image](https://github.com/user-attachments/assets/95795574-60fc-40f4-8b90-be0dacacf661)

- `remove_duplicates(arr)`: Devuelve una nueva lista sin elementos duplicados.
- ![image](https://github.com/user-attachments/assets/4df5e89a-85b9-41ef-9984-95bca6f8ca80)

- `binary_search_recursive(arr, target)`: Implementa una búsqueda binaria recursiva en una lista ordenada.
- Algoritmo para mapear una lista de números a resultados de búsqueda binaria, optimizado para grandes volúmenes de datos y procesamiento en paralelo.
- ![image](https://github.com/user-attachments/assets/0e91924f-0041-4ede-8eaf-ab39da520a7f)


### 2. Implementaciones en **JavaScript**
- `isAnagram(str1, str2)`: Verifica si dos cadenas son anagramas.
- ![image](https://github.com/user-attachments/assets/99cab475-eae8-4b4b-a653-f6fc1686d3d3)

- `findCommonElements(listOfLists)`: Encuentra los elementos comunes en todas las sub-listas de una lista dada.
- Implementación del algoritmo de ordenamiento MergeSort.
- ![image](https://github.com/user-attachments/assets/5312ee1a-9e7a-428e-89c0-59bb8649ac91)


### 3. Implementación en **.NET (C#)**
- `BinaryTree`: Implementa un Árbol Binario de Búsqueda (BST) con métodos para:
  - Insertar elementos.
  - Buscar elementos.
  - Imprimir los elementos en orden ascendente.
- Se incluye un análisis de la complejidad computacional de cada operación.
- ![image](https://github.com/user-attachments/assets/562073ed-a3d6-4a75-8a12-c1b573a0c88b)


## Beneficios del uso de Búsqueda Binaria
Dado que la primera lista puede ser muy grande, el uso de la **búsqueda binaria** en lugar de una **búsqueda secuencial** ofrece ventajas significativas:
- **Complejidad:** O(log n) en comparación con O(n) de la búsqueda secuencial.
- **Escalabilidad:** Reducción drástica del número de comparaciones requeridas.
- **Procesamiento en paralelo:** Permite distribuir la carga cuando el conjunto de datos es muy grande.



