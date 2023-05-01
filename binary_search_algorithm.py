# Función para encontrar un elemento determinado de una lista utilizando una búsqueda binaria

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps + 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        elif element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

# En el target se tiene que poner el elemento de la lista que se desea encontrar


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9

binary_search(my_list, target)
