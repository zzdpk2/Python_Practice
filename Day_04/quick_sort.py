def quick_sort(data, start, end) -> None:
    if start >= end:
        return
    pivot = data[start]
    left = start
    right = end
    while left < right:
        while left < right and data[right] >= pivot:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= pivot:
            left += 1
        data[right] = data[left]

    data[right] = pivot

    quick_sort(data, start, left - 1)
    quick_sort(data, left + 1, end)


if __name__ == '__main__':
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(data, 0, len(data) - 1)
    print(data)
