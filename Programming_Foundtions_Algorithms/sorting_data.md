# Sorting Data

Most modern languages have sorting built in
Bubble sort
Merge sort uses recursion
Quick sort uses recursion

## Bubble Sort

Array of elements
compares first two items and creates new instance where the two items swap places. Largest item bubbles it's way to the top of the array.
Simple
Perfomance `O(n2)` :
For loops inside of for loops usually n2
Not practical and used for teaching only

## Merge Sort

Divide-and-conquer algorithm
Breaks data into individual pieces and merges them
Uses recursion to operate on datasets
Performs well on large sets of data
Performance of O(n log n) time complexity - log linier

## Quicksort

Divide-and-conquer
uses recursion to perfomr sorting
performs better than merge sort, O(n log n)
Operates in place on the data
Can degrade  on run