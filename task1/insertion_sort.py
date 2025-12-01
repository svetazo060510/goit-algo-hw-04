def insertion_sort(arr):
    """Сортування вставками."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Переміщуємо елементи, більші за key, на одну позицію вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr