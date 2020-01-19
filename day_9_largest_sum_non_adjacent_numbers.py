"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def get_largest_sum(nums):
    largest_sum = None
    return largest_sum

# assert get_largest_sum([2, 4, 6, 2, 5]) == 13
# assert get_largest_sum([5, 1, 1, 5]) == 10
get_largest_sum([2, 4, 6, 2, 5])

# largest_sum = None
# last_el_idx = len(nums) - 1
# jump = 2
# start_shifter_is_active = False
# start_shifter = 0
# i = 0
# while i <= last_el_idx:
#     if start_shifter_is_active:
#         i += start_shifter
#     if jump == last_el_idx:
#         print(0)
#         print(last_el_idx)
#         start_shifter_is_active = True
#         start_shifter += 1
#         jump = 2
#         if start_shifter > len(nums) / 2:
#             break
#     print(i)
#     i += jump
#     if i == last_el_idx:
#         print(i)
#         i = 0
#         jump += 1
#     if i > last_el_idx:
#         i = 0
#         jump += 1


# for i in range(0, nums_amount, jump):
#     print(i)
#     if i == nums_amount - 1:
#         i = 0
#         jump += 1
#         print('increase jump')
#         if jump / nums_amount > nums_amount / 2:
#             i = start_shifter
#             start_shifter += 1
