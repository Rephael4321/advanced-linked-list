from typing import Iterable

class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self, nodes:list[str]=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next
    
    def __iter__(self) -> Iterable:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)    

    def addFirst(self, node: Node) -> None:
        node.next = self.head
        self.head = node
    
    def addLast(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def addAfter(self, target_node_data: str, new_node: Node) -> None:
        if self.head is None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception(f"Node with data {target_node_data} not found")

    def addBefore(self, target_node_data: str, new_node: Node) -> None:
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.addFirst(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        
        raise Exception(f"Node with data {target_node_data} not found")

    def removeNode(self, target_node_data: str) -> None:
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                del(node)
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def reverse(self):
        prev_node = None
        node = self.head
        while node is not None:
            if node.next is None:
                self.head = node
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node


if __name__ == "__main__":
    llist = LinkedList("a b c d e f g".split())
    llist.addFirst(Node("1"))
    llist.addLast(Node("2"))
    llist.addAfter("c", Node("X"))
    llist.addBefore("g", Node("Y"))
    llist.removeNode("a")
    print(llist)
    llist.reverse()
    print(llist)
