def binarySearch(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print('mid', arr[mid])

        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1

    return False

array= [1,3,8,10,11,14,17]
x = 10

print('Index of number',x, 'is equal to ', binarySearch(array, x))