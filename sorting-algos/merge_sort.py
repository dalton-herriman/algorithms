import random
import time
import matplotlib.pyplot as plt

# Merge Sort
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any leftovers
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test different sizes to visualize time complexity
sizes = [100, 500, 1000, 2000, 5000, 10000]
times = []

for size in sizes:
    arr = [random.uniform(-1000, 1000) for _ in range(size)]
    start = time.time()
    merge_sort(arr)
    times.append(time.time() - start)

# Plot results
plt.plot(sizes, times, marker='o')
plt.title("Merge Sort Time Complexity")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()
