// 6. Escribe una implementación para el algoritmo de ordenamiento mergesort.
function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr; // Caso base: si el array tiene 0 o 1 elementos, ya está ordenado
    }

    const mid = Math.floor(arr.length / 2); // Encontramos el punto medio
    const left = mergeSort(arr.slice(0, mid)); // Ordenamos la mitad izquierda
    const right = mergeSort(arr.slice(mid)); // Ordenamos la mitad derecha

    return merge(left, right); // Fusionamos ambas mitades ordenadas
}

function merge(left, right) {
    let sortedArray = [];
    let i = 0, j = 0;

    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) {
            sortedArray.push(left[i]);
            i++;
        } else {
            sortedArray.push(right[j]);
            j++;
        }
    }

    // Agregamos los elementos restantes de ambas mitades (si los hay)
    return sortedArray.concat(left.slice(i)).concat(right.slice(j));
}

console.log(mergeSort([38, 27, 43, 3, 9, 82, 10])); 
console.log(mergeSort([5, 1, 4, 2, 8])); 
console.log(mergeSort([])); 
console.log(mergeSort([7])); 
