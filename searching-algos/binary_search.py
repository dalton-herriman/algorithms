import random
import math

# Generate a sorted array of unique values for more reliable testing
random_sorted_array = sorted(random.sample(range(1, 10001), 1000))
# Pick a target that is guaranteed to be in the array
random_target = random.choice(random_sorted_array)

def binary_search(target, start, end, depth=0):
    print(f"{'  '*depth}Searching in range [{start}, {end}]")
    if start > end:
        print(f"{'  '*depth}Target {target} not found in current range.")
        return "Not found"
    
    middle = math.floor((start + end) / 2)
    print(f"{'  '*depth}Middle index: {middle}, Value: {random_sorted_array[middle]}")

    if random_sorted_array[middle] == target:
        print(f"{'  '*depth}Target {target} found at index {middle}")
        return (f"Found at index {middle}")
    
    if random_sorted_array[middle] > target:
        print(f"{'  '*depth}Target {target} is less than {random_sorted_array[middle]}. Searching left half.")
        return binary_search(target, start, middle-1, depth+1)
    
    if random_sorted_array[middle] < target:
        print(f"{'  '*depth}Target {target} is greater than {random_sorted_array[middle]}. Searching right half.")
        return binary_search(target, middle+1, end, depth+1)

def main():
    start, end = 0, len(random_sorted_array) - 1
    print(f"Array size: {len(random_sorted_array)}")
    print(f"Target to find: {random_target}")
    result = binary_search(random_target, start, end)
    print(result)
    print(f"Binary search time complexity: O(log n)")

main()