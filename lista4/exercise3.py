from collections.abc import Sequence

class SortedList(Sequence):
    def __init__(self, unsorted_list, key):
        [].