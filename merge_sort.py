def merge_sort(array):
    # Base case: if the array has less than two elements, it is already sorted.
    if len(array) < 2:
        return array
    
    # Step 1: Divide the array into two halves.
    mid = len(array) // 2  # Find the midpoint of the array.
    left_half = array[:mid]  # Assign the first half of the array to left_half.
    right_half = array[mid:]  # Assign the second half of the array to right_half.
    
    # Step 2: Recursively sort each half.
    left_half = merge_sort(left_half)  # Recursively apply merge_sort to the left half.
    right_half = merge_sort(right_half)  # Recursively apply merge_sort to the right half.
    
    # Step 3: Merge the sorted halves.
    sorted_array = []  # Initialize an empty list to store the sorted elements.
    i = j = 0  # Initialize pointers for traversing the two halves.
    
    # Traverse both halves and merge them into sorted_array in sorted order.
    while i < len(left_half) and j < len(right_half):
        # Compare the current elements of both halves and append the smaller one.
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])  # Append element from left_half.
            i += 1  # Move the pointer in left_half forward.
        else:
            sorted_array.append(right_half[j])  # Append element from right_half.
            j += 1  # Move the pointer in right_half forward.

    # After one half is exhausted, append the remaining elements of the other half.
    sorted_array += left_half[i:]  # Append any remaining elements from left_half.
    sorted_array += right_half[j:]  # Append any remaining elements from right_half.
    
    return sorted_array  # Return the merged and sorted array.
