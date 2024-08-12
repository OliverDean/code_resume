import random

def bubble_sort(lst):
    """
    Sorts a list of elements using the bubble sort algorithm.
    Usage: python bubble_sort.py
    
    Parameters:
    lst (list): The list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

if __name__ == "__main__":
    random_numbers = [random.randint(1, 999) for _ in range(20)]
    
    print("Unsorted List:")
    print(random_numbers)
    
    sorted_numbers = bubble_sort(random_numbers)
    
    print("\nSorted List:")
    print(sorted_numbers)
