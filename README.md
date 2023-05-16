# Binary Search

Este programa implementa la función `binary_search` para encontrar un elemento específico en una lista utilizando el algoritmo de búsqueda binaria.

## Descripción

La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en una lista ordenada. Comienza dividiendo la lista en dos mitades y compara el elemento objetivo con el valor del elemento en el medio de la lista. Si el elemento objetivo es igual al valor del elemento en el medio, se devuelve la posición del elemento. Si el elemento objetivo es menor que el valor del elemento en el medio, se busca en la mitad inferior de la lista. Si el elemento objetivo es mayor que el valor del elemento en el medio, se busca en la mitad superior de la lista. El proceso se repite hasta que se encuentra el elemento objetivo o se determina que no está presente en la lista.

El programa define la función `binary_search` que toma una lista ordenada y un elemento objetivo como parámetros. Realiza la búsqueda binaria en la lista y devuelve la posición del elemento si se encuentra, o -1 si no está presente en la lista.

## Uso

1. Define una lista ordenada en la variable `my_list`. Asegúrate de que los elementos de la lista estén en orden ascendente.
2. Establece el elemento objetivo que deseas encontrar en la variable `target`.
3. Llama a la función `binary_search` pasando la lista y el elemento objetivo como argumentos.
4. La función devolverá la posición del elemento si se encuentra, o -1 si no está presente.
5. Se mostrará el progreso de la búsqueda, indicando los pasos y la lista actual en cada iteración.

**Nota:** Asegúrate de que la lista esté ordenada correctamente para obtener resultados precisos con la búsqueda binaria.

## Ejemplo

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9

result = binary_search(my_list, target)

if result != -1:
    print("El elemento", target, "se encuentra en la posición", result)
else:
    print("El elemento", target, "no está presente en la lista")
```

## Resultado

```
Step 0 : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Step 1 : [6, 7, 8, 9]
Step 2 : [8, 9]
Step 3 : [9]
El elemento 9 se encuentra en la posición 8
```

En este ejemplo, la función `binary_search` encuentra el elemento 9 en la lista y devuelve su posición como 8.

Ten en cuenta que la búsqueda binaria es efectiva en listas ordenadas y puede reducir significativamente el tiempo de búsqueda en comparación con otros algoritmos de búsqueda lineal.
