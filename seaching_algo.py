# -----------------------------
# 🌟 LINEAR SEARCH ALGORITHM 🌟
# -----------------------------

def linear_search(arr, target):
    """
    Searches for target in arr using linear search.
    Returns the index if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# -----------------------------
# 🔍 BINARY SEARCH ALGORITHM 🔍
# -----------------------------

def binary_search(arr, target):
    """
    Searches for target in sorted arr using binary search.
    Returns the index if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# -----------------------------
# 🔎 TESTING BOTH SEARCHES 🔎
# -----------------------------

arr = [10, 25, 35, 40, 55, 60, 75]
target = 55

# Linear Search Test
lin_result = linear_search(arr, target)
print(f"Linear Search: {target} found at index {lin_result}" if lin_result != -1 else "Not found with Linear Search")

# Binary Search Test
# Make sure the list is sorted for binary search
sorted_arr = sorted(arr)
bin_result = binary_search(sorted_arr, target)
print(f"Binary Search: {target} found at index {bin_result}" if bin_result != -1 else "Not found with Binary Search")
