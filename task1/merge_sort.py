def merge_sort(arr):
    """Сортування злиттям (рекурсивне розбиття)."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    """Об'єднання двох відсортованих списків."""
    merged = []
    i = j = 0
    
    # Порівняння та злиття елементів
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    # Додавання залишку
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged