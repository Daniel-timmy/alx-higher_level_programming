#!/usr/bin/python3
class Node:
    """
        A class that defines a node
    """
    def __init__(self, data, next_node=None):
        """Initialises the variables"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns: returns data"""
        return (self.__data)

    @property.setter
    def data(self, value):
        """sets data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__value = value

    @property
    def next_node(self):
        """Returns the next_node"""
        return (self.__next_node)

    @property.setter
    def next_node(self, value):
        """sets next_node attributes"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    """Singly linked list class"""
    
