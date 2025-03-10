import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if (self.left == None):
                self.left = BinarySearchTree(value)

            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)

        if target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

        # else:
        #     return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.value == None:
            return None

        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value != None:
            cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass
