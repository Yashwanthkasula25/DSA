# ------------------------
# 🔁 BUBBLE SORT ALGORITHM
# ------------------------

def bubble_sort(arr):
    """
    Repeatedly swaps adjacent elements if they are in wrong order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):  # Last i elements are already in place
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# ---------------------------
# 🔀 SELECTION SORT ALGORITHM
# ---------------------------

def selection_sort(arr):
    """
    Selects the minimum element and places it at correct position.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# ----------------------------
# 📌 INSERTION SORT ALGORITHM
# ----------------------------

def insertion_sort(arr):
    """
    Builds the final sorted array one item at a time.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# -----------------------
# ⚡ MERGE SORT ALGORITHM
# -----------------------

def merge_sort(arr):
    """
    Divide and conquer approach. Divides list and merges sorted parts.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive sort
        merge_sort(left)
        merge_sort(right)

        # Merge sorted halves
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# --------------------
# 🔎 TESTING SORTS 🔎
# --------------------

original = [64, 25, 12, 22, 11]

# Bubble Sort Test
arr1 = original.copy()
bubble_sort(arr1)
print("Bubble Sort:", arr1)

# Selection Sort Test
arr2 = original.copy()
selection_sort(arr2)
print("Selection Sort:", arr2)

# Insertion Sort Test
arr3 = original.copy()
insertion_sort(arr3)
print("Insertion Sort:", arr3)

# Merge Sort Test
arr4 = original.copy()
merge_sort(arr4)
print("Merge Sort:", arr4)
