"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def is_decodable(num):
    if num >= 1 and num <= 26:
        return True


def decode(message):
    single_tokens = [i for i in str(message)]
    print(single_tokens)
    double_tokens = [str(message)[i:i+2] for i in range(0, len(message), 1) if i < len(message) - 1]
    print(double_tokens)

decode('123')