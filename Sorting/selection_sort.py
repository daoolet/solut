def find_smallest(arr: list) -> int:
    min = arr[0]
    min_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_idx = i

    return min_idx


def selection_sort(arr: list) -> list:
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr