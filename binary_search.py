def bi_setch_recursive(arr: list, low: int, high: int, target: int) -> int:

    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]

        elif arr[mid] > target:
            return bi_setch_recursive(arr, low, mid - 1,target)

        else:
            return bi_setch_recursive(arr, mid + 1, high, target)
    else:
        return -1