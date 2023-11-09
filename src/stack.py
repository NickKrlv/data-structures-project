class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next_node
            return popped_node.data


stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)  # data3
print(stack.top.next_node.data)  # data2
print(stack.top.next_node.next_node.data)  # data1
print(stack.top.next_node.next_node.next_node)  # None
print(stack.top.next_node.next_node.next_node.data)  # AttributeError: 'NoneType' object has no attribute 'data'
