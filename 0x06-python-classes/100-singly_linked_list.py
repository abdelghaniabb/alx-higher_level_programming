#!/usr/bin/python3
""" Node class"""


class Node:
    """ this class defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """
            Initializes a new Node
            Args:
                data: the data of the Node
                next_node: the next Node
            Return:
                None
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
            Getter method to retrieve the Node's data
            Returns:
                Node's data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
            Setter method to set the Node's data
            Args:
                value : Node's data
            Raises:
                TypeError: data must be an integer
            Returns:
                None
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
            Getter method to retrieve the next Node
            Returns:
                the next Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
            Setter method to set the next Node
            Raises:
                TypeError: next_node must be a Node object
            Returns:
                    None
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" SinglyLinkedList"""


class SinglyLinkedList:
    """This class defines a sigly linked list"""

    def __init__(self):
        """
            Initializes a new inglyLinkedList
            Args:
                None
            Return:
                None
        """
        self.head = None

    def sorted_insert(self, value):
        """
            Inserts a new Node into the correct sorted position in the list.
            Args:
                value (int): The value to be inserted.
            Returns:
                None
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curs = self.head
            while curs.next_node is not None and curs.next_node.data < value:
                curs = curs.next_node
            new_node.next_node = curs.next_node
            curs.next_node = new_node

    def __str__(self):
        """
            Returns a string representation of the linked list.
            Returns:
                str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
