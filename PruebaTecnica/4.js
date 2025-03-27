//4. Escribe una función llamada isAnagram que acepte dos cadenas de texto como parámetros y 
// determine si son anagramas (es decir, si tienen exactamente las mismas letras, pero en diferente orden).
function isAnagram(str1, str2) {
    if (str1.length !== str2.length) return false; // Si tienen diferente longitud, no pueden ser anagramas

    // Convertir a minúsculas, ordenar y comparar
    return str1.toLowerCase().split("").sort().join("") === str2.toLowerCase().split("").sort().join("");
}

// Ejemplo de uso
console.log(isAnagram("listen", "silent")); // true
console.log(isAnagram("hello", "world"));   // false
console.log(isAnagram("Dormitory", "Dirtyroom")); // true (sin espacios y mayúsculas no afectan)
