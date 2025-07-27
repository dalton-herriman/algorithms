import random
import time
import matplotlib.pyplot as plt

def quick_sort(array):
    # Base case: lists with 0 or 1 elements are already sorted
    if len(array) <= 1:
        return array

    # Step 1: Choose a pivot (here we use the middle element)
    pivot = array[len(array) // 2]

    # Step 2: Partition the array
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    # Step 3: Recursively sort left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)


# Test different sizes to visualize time complexity
sizes = [100, 500, 1000, 2000, 5000, 10000]
times = []

for size in sizes:
    arr = [random.uniform(-1000, 1000) for _ in range(size)]
    start = time.time()
    quick_sort(arr)
    times.append(time.time() - start)

# Plot results
plt.plot(sizes, times, marker='o')
plt.title("Quick Sort Time Complexity")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()