// Escribe una función llamada findCommonElements que acepte una lista de 
// listas como parámetro y devuelva una lista con los elementos comunes a todas las sub-listas.
function findCommonElements(lists) {
    if (lists.length === 0) return [];

    return lists.reduce((acc, curr) => acc.filter(el => curr.includes(el)));
}

// Ejemplo de uso
const lists = [
    [1, 2, 3, 4, 5],
    [2, 3, 5, 7, 9],
    [2, 3, 5, 10, 12]
];

console.log(findCommonElements(lists)); 
