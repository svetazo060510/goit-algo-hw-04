import timeit
import random
import copy
from typing import Callable, List
from insertion_sort import insertion_sort
from merge_sort import merge_sort 

# Розміри тестових наборів даних
SIZES = {
    "Малий": 100,
    "Середній": 1000,
    "Великий тест": 10000,
}

# Кількість повторів для timeit (для великих масивів = 2: stated on line 63 )
NUM_REPEATS = 5

def generate_data(size: int) -> List[int]:
    """Генерує випадковий набір даних."""
    return [random.randint(0, size * 10) for _ in range(size)]

def measure_time(sort_func: Callable, data: List[int], repeats: int) -> float:
    """Вимірює час виконання сортування за допомогою timeit."""
    
    """Використовуємо функцію-обгортку для timeit, щоб уникнути проблем зі скоупом:
    між змінними: data, copy, sort_func та ізольованим середовищем timeit"""
    def wrapper():
        # Створюємо копію даних, оскільки сортування змінює масив
        temp_data = copy.copy(data) 

        if sort_func == sorted:
            sorted(temp_data)
        elif sort_func == insertion_sort:
            insertion_sort(temp_data)
        elif sort_func == merge_sort:
            merge_sort(temp_data)
            
    # Використовуємо timeit.repeat для отримання кращої середньої оцінки
    times = timeit.repeat(
        stmt=wrapper,
        repeat=repeats, 
        number=1  # Виконуємо 1 раз за вимір
    )
    return min(times) / 1 # Повертаємо мінімальний час для уникнення впливу фонових процесів


def run_tests():
    results = {}
    
    # Алгоритми для порівняння
    algorithms = {
        "Insertion Sort (O(n^2))": insertion_sort,
        "Merge Sort (O(n log n))": merge_sort,
        "Timsort (sorted) (O(n log n))": sorted,
    }
    
    for size_name, size in SIZES.items():
        data = generate_data(size)
        results[size_name] = {}
        print(f"\n--- Тестування набору: {size_name} (N={size}) ---")
        
        # Обмеження повторів для великих, повільних тестів
        current_repeats = NUM_REPEATS if size <= 1000 else 2 
        
        for algo_name, algo_func in algorithms.items():
            
            # Використовуємо менше повторів для повільного O(n^2) алгоритму
            if algo_func == insertion_sort and size > 1000:
                time_taken = float('inf') 
                print(f"[{algo_name}]: Пропущено через надто велику складність (N={size})")
                
            else:
                time_taken = measure_time(algo_func, data, current_repeats)
                results[size_name][algo_name] = time_taken
                print(f"[{algo_name}]: {time_taken:.6f} сек.")
                
    return results

# Виконання тестів
empirical_results = run_tests()