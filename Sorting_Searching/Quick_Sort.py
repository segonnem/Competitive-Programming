def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi-1)
            _quick_sort(items, pi+1, high)

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print("Sorted array:", arr)
