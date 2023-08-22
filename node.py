from typing import Self

class Node:
    def __init__(self, value):
        self.__value = value
        self.__left_node = None
        self.__right_node = None

    def set_left_node(self, node):
        if not isinstance(node, Node):
            raise AttributeError('Left node has to be a node')
        if self.__left_node is not None:
            raise AttributeError('Left node already set')
        self.__left_node = node

    def set_right_node(self, node):
        if not isinstance(node, Node):
            raise AttributeError('Right node has to be a node')
        if self.__right_node is not None:
            raise AttributeError('Right node already set')
        self.__right_node = node

    def get_left_node(self) -> Self:
        return self.__left_node

    def get_right_node(self) -> Self:
        return self.__right_node

    def get_value(self):
        return self.__value


if __name__ == '__main__':
    root_node = Node(1000)
    root_node.set_left_node(Node(500))
    root_node.set_right_node(Node(1500))
    print(root_node.get_value(), root_node.get_right_node().get_value())