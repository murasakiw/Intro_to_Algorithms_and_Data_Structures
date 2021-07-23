def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print('Number found: ', result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 10)
verify(result)

result = recursive_binary_search(numbers, 2)
verify(result)