"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def solution(input_list, input_k):
    cache = set()
    for num in input_list:
        complement = input_k - num
        if complement in cache:
            return True
        else:
            cache.add(num)
    return False


if __name__ == '__main__':
    input_list = [10, 15, 3, 7]
    input_k = 17
    expected_output = True

    print('Test Run:')
    print(solution(input_list, input_k))
