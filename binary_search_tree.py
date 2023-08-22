from node import Node


class BinarySearchTree:
    def __init__(self):
        self.__root_node = None

    def insert_value(self, value: int):
        if self.__root_node is None:
            self.__root_node = Node(value)
            return
        current_node = self.__root_node
        while True:
            if value < current_node.get_value():
                new_current_node = current_node.get_left_node()
                if new_current_node is None:
                    current_node.set_left_node(Node(value))
                    return
                current_node = new_current_node
            else:
                new_current_node = current_node.get_right_node()
                if new_current_node is None:
                    current_node.set_right_node(Node(value))
                    return
                current_node = new_current_node


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert_value(1000)
    bst.insert_value(500)
    bst.insert_value(300)
    bst.insert_value(600)
    bst.insert_value(1500)
    bst.insert_value(1200)
    bst.insert_value(1500)
    print(bst)
