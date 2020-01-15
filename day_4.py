"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

arr = [3, 4, -1, 1]

lowest = -1
first_positive_int_unset = True
for x in arr:
    if first_positive_int_unset and x > lowest:
        lowest = x
        first_positive_int_found = False
    else:
        if lowest > x:
            lowest = x

print(lowest)

"""
Unsolved
"""