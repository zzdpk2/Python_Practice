def quick_sort2(data) -> list:
    if data is []:
        return []
    else:
        pivot = data[0]
        less = quick_sort2([l for l in data[1:] if l < pivot])
        more = quick_sort2([m for m in data[1:] if m >= pivot])
        return less + [pivot] + more


if __name__ == '__main__':
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    res = quick_sort2(data)
    print(res)
