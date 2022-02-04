# Algorithm Coding Test Practice

Will post my solutions to different coding test algorithm problems here. 
The test case contains a handful of simple example cases. The committed code is validated using more extensive examples.


## Arrays
[two_number_sum.py](https://github.com/poomstas/algorithms/blob/main/two_number_sum.py)
See if two numbers from a given array sum up to the target sum value.

[spiral_traverse.py](https://github.com/poomstas/algorithms/blob/main/spiral_traverse.py)
Traverse a 2D array in spiral, collecting all the values along the way.

[move_element_to_end.py](https://github.com/poomstas/algorithms/blob/main/move_element_to_end.py)
Move all 2's to the end of the array (for instance).

[smallest_difference.py](https://github.com/poomstas/algorithms/blob/main/smallest_difference.py)
Given two arrays, find the two values that has the smallest difference. 

[sorted_square_array.py](https://github.com/poomstas/algorithms/blob/main/sorted_square_array.py)
Take a non-empty array of integers sorted in ascending order and return a new array of the same length with the squares of the original integers also sorted in ascending order. May contain negative values. Uses while loop.

[sorted_square_array_alt.py](https://github.com/poomstas/algorithms/blob/main/sorted_square_array_alt.py) Alternative solution that uses a for loop. Cleaner. 

[validate_subsequence.py](https://github.com/poomstas/algorithms/blob/main/validate_subsequence.py) Taking two 1D arrays and seeing if one is a subsequence of the other.

[leetcode_two_sum.py](https://github.com/poomstas/algorithms/blob/main/leetcode_two_sums.py)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

[tournament_winner.py](https://github.com/poomstas/algorithms/blob/main/tournament_winner.py)
Determine the winner of the tournament after reviewing all match results.

[kadanes_algorithm.py](https://github.com/poomstas/algorithms/blob/main/kadanes_algorithm.py)
Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all of the integers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers (numbers next to each other in the input array).

## Sort
[bubble_sort.py](https://github.com/poomstas/algorithms/blob/main/bubble_sort.py)
Standard implementation of a bubble sort.


## Trees
[find_closest_value_in_BST.py](https://github.com/poomstas/algorithms/blob/main/find_closest_value_in_BST.py)
Find the value closest to the input value in a BST.

[node_depths.py](https://github.com/poomstas/algorithms/blob/main/node_depths.py)
Calculate the sum of all node depths in a binary tree.

[node_depths_alt.py](https://github.com/poomstas/algorithms/blob/main/node_depths_alt.py)
Alternative solution to node depth calculation in a binary tree.

[binary_tree_diameter.py](https://github.com/poomstas/algorithms/blob/main/binary_tree_diameter.py)
Determine the diameter of a binary tree.

[BST_traversal.py](https://github.com/poomstas/algorithms/blob/main/BST_traversal.py)
Implement three different tree traversal algorithms: in-order, pre-order, and post-order.

[validate_BST.py](https://github.com/poomstas/algorithms/blob/main/validate_BST.py)
Validate the values in a BST to ensure they are within expected ranges.

[min_height_BST.py](https://github.com/poomstas/algorithms/blob/main/min_height_BST.py)
Calculate the minimum height of a BST after inputting a sorted list of values.

[find_kth_largest_value_in_bst.py](https://github.com/poomstas/algorithms/blob/main/find_kth_largest_value_in_bst.py)
Find the kth largest value in a BST. O(h+k) time | O(h) space.

[find_kth_largest_value_in_bst_alt.py](https://github.com/poomstas/algorithms/blob/main/find_kth_largest_value_in_bst_alt.py)
Find the kth largest value in a BST. O(N) time | O(N) space.

[invert_binary_tree_recur.py](https://github.com/poomstas/algorithms/blob/main/invert_binary_tree_recur.py)
Invert a binary tree (recursive solution).

[invert_binary_tree_iter.py](https://github.com/poomstas/algorithms/blob/main/invert_binary_tree_iter.py)
Invert a binary tree (iterative solution).


## Searching
[binary_search.py](https://github.com/poomstas/algorithms/blob/main/binary_search.py)
Do a binary search on a sorted array.

[depth_first_search.py](https://github.com/poomstas/algorithms/blob/main/depth_first_search.py)
Depth-first Search on an acyclic tree-like structure.

[search_in_sorted_matrix.py](https://github.com/poomstas/algorithms/blob/main/search_in_sorted_matrix.py)
Find the coordinates of a target value in a sorted 2D matrix.

## Strings
[leetcode_roman_to_integer.py](https://github.com/poomstas/algorithms/blob/main/leetcode_roman_to_integer.py)
Convert Roman numeral string to integer.

[leetcode_palindrome_number.py](https://github.com/poomstas/algorithms/blob/main/leetcode_palindrome_number.py)
Given an integer x, return true if x is palindrome integer.


## Linked Lists
[remove_duplicates_from_linked_list.py](https://github.com/poomstas/algorithms/blob/main/remove_duplicates_from_linked_list.py)
Singly linked list, with integer nodes arranged in sorted order. Remove all duplicates.

[sum_of_linked_lists.py](https://github.com/poomstas/algorithms/blob/main/sum_of_linked_lists.py)
You're given two linked lists with potentially unequal length. Each linked list represents a non-negative integer, where each node in the linked list is a digit of that integer (first nodein each linked list always represents the least significant digit of the integer). Write a function that returns the head of a new linked list that represents the sum of the integers represented by the two input linked lists.

[remove_kth_node_from_end.py](https://github.com/poomstas/algorithms/blob/main/remove_kth_node_from_end.py)
Singly Linked List and an integer k. Remove kth node from end. 

[reverse_linked_list.py](https://github.com/poomstas/algorithms/blob/main/reverse_linked_list.py)
Reverse the order of singly linked list.



# To Practice Next:
- Practice explaining the binary_tree_diameter.py question using an example case. Walk through the solution and explain why the algorithm works.