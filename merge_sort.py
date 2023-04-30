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
