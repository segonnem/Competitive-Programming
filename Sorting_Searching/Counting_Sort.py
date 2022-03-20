def counting_sort(arr):
    output = [0] * len(arr)
    count = [0] * (max(arr) + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

tab = [4, 2, 2, 8, 3, 3, 1]
sorted_tab = counting_sort(tab)
print("Sorted array is:", sorted_tab)
