def merge_sort(array):
    if len(array) < 2:
        return array
    
    # Divide the array into two halves
    mid = len(array) // 2
    left_half = array[:mid] 
    right_half = array[mid:] 
    
    # Recursively sort each half
    left_half = merge_sort(left_half) 
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    sorted_array = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1
    sorted_array += left_half[i:]
    sorted_array += right_half[j:]
    
    return sorted_array



# Test the algorithm on a random list of 1000 integers betwen 1 and 10000
import random
import time

# Generate a list of 1000 random integers between 1 and 10000
my_list = [random.randint(1, 10000) for i in range(1000)]

# Measure the time it takes to sort the list using merge sort
start_time = time.time()
sorted_list = merge_sort(my_list)
end_time = time.time()

# Print the sorted list and the time it took to sort it
print(sorted_list)
print()
print()
print("Time taken:", end_time - start_time, "seconds")