import random

def binary_search(arr, x):
    """
    Implements binary search to find the position of x in a sorted list arr.
    Returns the index of x if present, else returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1

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

    random_numbers = [random.randint(1, 100) for _ in range(20)]
    
    print("Unsorted List:")
    print(random_numbers)

    sorted_numbers = merge_sort(random_numbers)
    
    print("\nSorted List:")
    print(sorted_numbers)
    
    search_element = random.choice(sorted_numbers)
    
    print(f"\nSearching for: {search_element}")
    
    index = binary_search(sorted_numbers, search_element)
    
    if index != -1:
        print(f"Element {search_element} found at index {index}.")
    else:
        print(f"Element {search_element} not found in the list.")
