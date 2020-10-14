def quick_sort(data, start, end) -> None:
    # the terminating condition
    if start > end:
        return
    # init values
    left = start
    right = len(data) - 1
    pivot = data[start]
    # start sorting
    while left < right:
        # if the right value is smaller than the left value, these two elements need to be switched
        if left < right and data[right] >= pivot:
            right -= 1
        # temporarily cover the left value from the right value
        data[left] = data[right]

        # if the left value is larger than the right value, these two elements need to be switched
        if left < right and data[left] <= pivot:
            left += 1
        # temporarily cover the right value from the left value
        data[right] = data[left]

    # put the pivot to the exact position
    data[right] = pivot
    # recursively sort all the elements
    quick_sort(data, start, left - 1)
    quick_sort(data, right + 1, end)


if __name__ == '__main__':
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(data, 0, len(data) - 1)
    print(data)
