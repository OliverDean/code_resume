import random

def merge_sort(arr):
    """
    Sorts a list using the merge sort algorithm.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


if __name__ == "__main__":
    random_numbers = [random.randint(1, 999) for _ in range(20)]
    
    print("Unsorted List:")
    print(random_numbers)
    
    sorted_numbers = merge_sort(random_numbers)
    
    print("\nSorted List:")
    print(sorted_numbers)