import random
from typing import List, Any


class Array:

    @staticmethod
    def get_item(arr: List[Any], index: int) -> Any:
        if 0 <= index < len(arr):
            return arr[index]
        raise IndexError("Index out of bounds")
    
    @staticmethod
    def bubble_sort(arr: List[Any]) -> None:
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

    @staticmethod
    def selection_sort(arr: List[Any]) -> None:
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]


def arr_create(size: int) -> List[int]:
    return [random.randint(11, 100) for _ in range(size)]


if __name__ == "__main__":
    arr = Array()
    
    arr_list = arr_create(10)
    print("Original Array:", arr_list)
    arr.bubble_sort(arr_list)
    print("Sorted Array:", arr_list)
    print("\n")
    
    arr_list = arr_create(10)
    print("Original Array:", arr_list)
    arr.selection_sort(arr_list)
    print("Sorted Array:", arr_list)