"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

-- "that contains at most k distinct characters" should than 'abcb' not be the longest string with still most distinct chars?
"""

import unittest


def get_longest_distinct_chars_substr(k, s):
    pass


assert get_longest_distinct_chars_substr(2, 'abcba') == 'bcb'