def binaryS_iter(a, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if a[mid] < key:
            low = mid + 1
        elif a[mid] > key:
            high = mid - 1
        elif a[mid] == key:
            return mid        
    return -1

def binaryS_recur(a, low, high, key):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if a[mid] < key:
        low = mid + 1
        return binaryS_recur(a, low, high, key)
    if a[mid] > key:
        high = mid - 1
        return binaryS_recur(a, low, high, key)    
    if a[mid] == key:
        return mid
        
a = [1, 3, 4, 4, 6, 8, 9]
print(binaryS_recur(a, 0, len(a)-1, 9))
            