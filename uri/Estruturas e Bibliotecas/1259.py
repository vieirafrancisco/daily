def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def balance(root):
    if root is None:
        return 0
    
    lh = height(root.left)
    rh = height(root.right)

    return (lh - rh)

def right_rotate(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    return new_root

def left_rotate(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    return new_root


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, x):
        if x <= self.value:
            self.insert_left(x)
        elif x > self.value:
            self.insert_right(x)
        
        result = balance(self)
        if result > 1:
            if balance(self.left) < 0:
                left_rotate(self.left)
            right_rotate(self)
        elif result < -1:
            if balance(self.right) > 0:
                right_rotate(self.right)
            left_rotate(self)
    
    def insert_left(self, x):
        if self.left is None:
            self.left = Node(x)
        else:
            self.left.insert(x)
    
    def insert_right(self, x):
        if self.right is None:
            self.right = Node(x)
        else:
            self.right.insert(x)
    
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value)
        if self.right is not None:
            self.right.inorder()
    
    def invert(self):
        if self.left is not None:
            self.left.invert()
        if self.right is not None:
            self.right.invert()
        tmp = self.left
        self.left = self.right
        self.right = tmp


class BinaryTree:
    def __init__(self):
        self.root = None
    
    @property
    def height(self):
        return height(self.root)

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self.root.insert(x)

    def inorder(self):
        if self.root is not None:
            self.root.inorder()
    
    def invert(self):
        if self.root is not None:
            self.root.invert()
    

n = int(input())

a = BinaryTree()
b = BinaryTree()

for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        a.insert(x)
    else:
        b.insert(x)

a.inorder()
b.invert()
b.inorder()
