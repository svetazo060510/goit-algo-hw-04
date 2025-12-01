from typing import List

def merge(list1: List[int], list2: List[int]) -> List[int]:
    """
    Об'єднує два відсортовані списки в один відсортований список.
    Часова складність: O(N), де N - загальна кількість елементів.
    """
    merged = []
    i = 0
    j = 0
    
    # Поки обидва списки мають елементи
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
            
    # Додавання залишку
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків у один відсортований список 
    за допомогою підходу "Розділяй і володарюй".
    
    Часова складність: O(N log k), де N - загальна кількість елементів, 
    а k - кількість списків.
    """
    # Базовий випадок 1: Список порожній
    if not lists:
        return []
    
    # Базовий випадок 2: Залишився лише один список
    if len(lists) == 1:
        return lists[0]
    
    # 1. Розбиття списку списків на дві половини
    mid = len(lists) // 2
    left_half = lists[:mid]
    right_half = lists[mid:]
    
    # 2. Рекурсивне об'єднання лівої половини
    merged_left = merge_k_lists(left_half)
    
    # 3. Рекурсивне об'єднання правої половини
    merged_right = merge_k_lists(right_half)
    
    # 4. Злиття двох отриманих відсортованих списків
    return merge(merged_left, merged_right)

# Тест 1:
lists = [[1, 4, 5], [1, 3, 4], [2, 6], [10, 11]]
merged_list = merge_k_lists(lists)
print("Відсортований список (тест 1):", merged_list)

# Тест 2:
lists_2 = [[-5, 0], [10, 12, 15], [1, 2]]
merged_list_2 = merge_k_lists(lists_2)
print("Відсортований список (тест 2):", merged_list_2)