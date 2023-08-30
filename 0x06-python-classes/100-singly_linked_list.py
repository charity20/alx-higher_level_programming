#!/usr/bin/python3
"""Define  a class of a singly linked lists"""

class Node:
    def __init__(self, data, next_node=None):
        """Constructor method to initialize a Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for retrieving the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for setting the data in the node.

        Args:
            value (int): The new data value for the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for retrieving the next node in the linked list.

        Returns:
            Node or None: The next node in the linked list or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for setting the next node in the linked list.

        Args:
            value (Node or None): The new next node for the current node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Constructor method to initialize a SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The data value for the new Node.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Custom string representation of the SinglyLinkedList instance.

        Returns:
            str: A string representation of the linked list.
        """
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

