#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""

        list1 = self[:]
        list1.sort()
        print(list1)
