class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BinarySearchTree(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BinarySearchTree(value)
                    break
                else:
                    current = current.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        while True:
            if target == current.value:
                return True
            elif target < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            else:
                if current.right:
                    current = current.right
                else:
                    return False

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb, add):
        if self.right:
            self.right.for_each(cb, add)
        if self.left:
            self.left.for_each(cb, add)
        if self.value == 'm':
            return
        if cb(self.value):
            add(self.value)
