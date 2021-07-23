def binary_search(list, target):
    first = 0
    last = len(list) - 1

    # El while loop es la instrucción que hace que crezca la complejidad del algoritmo
    # porque cada que se cambia el valor de first y last se hace que se siga ejecutando
    # el ciclo hasta que se cumpla la condición o se alcance la instrucción con el primer return
    # el algoritmo tiene un crecimiento O(log n) porque a medida que el problema se acerca 
    # al peor de los casos, la lista se va reduciendo cada vez más.
    while first <= last: 
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last =  midpoint - 1

    return None


def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)
result = binary_search(numbers, 6)
verify(result)