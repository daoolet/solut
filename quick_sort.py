
def qsort(array: list):

    if len(array) < 2:
        return array
    
    pivot = array[0]

    less = [i for i in array[1:] if i < pivot]
    greater = [i for i in array[1:] if i > pivot]

    return qsort(less) + [pivot] + qsort(greater)