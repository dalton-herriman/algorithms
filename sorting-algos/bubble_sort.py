import random
import time
import matplotlib.pyplot as plt

# Bubble sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array

# Test different sizes to visualize time complexity
sizes = [100, 500, 1000, 2000]
times = []

for size in sizes:
    arr = [random.uniform(-1000, 1000) for _ in range(size)]
    start = time.time()
    bubble_sort(arr)
    times.append(time.time() - start)

# Plot results
plt.plot(sizes, times, marker='o')
plt.title("Bubble Sort Time Complexity")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()
