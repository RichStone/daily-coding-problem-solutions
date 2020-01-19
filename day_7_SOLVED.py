"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def is_decodable(num):
    return int(num) >= 1 and int(num) <= 26


def decode(message):
    # start with one since there is always an all single numbers count solution
    decodable_ways_count = 1
    double_tokens = [str(message)[i:i+2] for i in range(0, len(message), 1) if i < len(message) - 1]
    decodable_tokens = [token for token in double_tokens if is_decodable(token)]
    print(decodable_tokens)
    decodable_ways_count += len(decodable_tokens)
    print(decodable_ways_count)
    return decodable_ways_count



decode('123411')
print(is_decodable('122'))

"""
SOLVED 🎉🎉🎉
READ SOLUTION 
"""