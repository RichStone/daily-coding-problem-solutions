"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""


class XorLinkedList:
    def __init__(self):
        self.both = None

    class Node:
        def __init__(self, data):
            self.data = data

    def add(self, element):
        if not self.both:
            pass


    def get(self, index):
        pass


ll = XorLinkedList()
el1 = 1
el2 = 2

ll.add(el1)

print()

"""
Unsolved
"""