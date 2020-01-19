"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

from functools import reduce
from operator import mul

class Solution:
    def solve(self, input):
        result = []
        for i, x in enumerate(input):
            list_without_i = input[:i] + input[i:]
            return reduce(mul, list_without_i, 1)


if __name__ == '__main__':
    # sample input
    inputs = [[1, 2, 3, 4, 5], [3, 2, 1]]

    # solution init
    sol = Solution()

    print('Test Run:')
    for input in inputs:
        print('#############')
        print('sample input: ' + str(input))
        output = sol.solve(input)
        print('output: ' + str(output))
        print('#############')