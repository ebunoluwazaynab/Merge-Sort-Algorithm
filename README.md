# Merge Sort Algorithm

This is a Python implementation of the merge sort algorithm. Merge sort is a divide-and-conquer sorting algorithm that recursively breaks down an array into two halves, sorts each half independently, and then merges the sorted halves back together to produce a final sorted array.

## Algorithm

The merge sort algorithm can be described in the following steps:
1. If the input array has fewer than two elements, return it as is (it is already sorted).
2. Divide the input array into two halves at the midpoint.
3. Recursively sort each half using merge sort.
   - For the left half, call the merge sort function with the subarray from index 0 to the midpoint (exclusive).
   - For the right half, call the merge sort function with the subarray from the midpoint to the end of the array (inclusive).
   - The recursion will continue until the subarrays have only one or zero elements, at which point they are considered sorted.
4. Merge the two sorted halves back together into a single sorted array.
   - Create an empty array to hold the merged result.
   - Compare the first element of each sorted half and append the smaller one to the result array.
   - Move the index pointer for the subarray from which the smaller element was taken by one position.
   - Continue comparing and appending elements until one of the subarrays has been completely merged into the result array.
   - Append any remaining elements from the other subarray to the result array.
5. Return the merged result array.

By dividing the array into smaller subarrays and recursively sorting them, merge sort achieves a time complexity of O(n log n), making it one of the most efficient sorting algorithms for large arrays.

## Usage

To use this implementation of the merge sort algorithm in your Python project, you can simply import the `merge_sort` function from the `merge_sort.py` file and call it with an input array.

```python
from merge_sort import merge_sort

input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = merge_sort(input_array)

print(sorted_array) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

## Contributions

Contributions are welcome! If you have any suggestions, improvements or issues with this implementation, feel free to submit a pull request or open an issue.

## License

This implementation is licensed under the MIT License. See the `LICENSE` file for details.
