import random

def heapify(arr, n, i):
    """
    A function to heapify a subtree rooted with node i which is an index in arr[].
    n is the size of the heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heap_sort(arr):
    """
    The main function to sort an array of given size using heap sort algorithm.
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
    
    return arr

if __name__ == "__main__":
    random_numbers = [random.randint(1, 999) for _ in range(20)]
    
    print("Unsorted List:")
    print(random_numbers)
    
    sorted_numbers = heap_sort(random_numbers)
    
    print("\nSorted List:")
    print(sorted_numbers)
