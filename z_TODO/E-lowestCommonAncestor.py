class TreeNode:
    # Binary Tree Node
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    # Method to insert node into tree
    def insert(self, value):

        if self.value is None:
            self.value = value
            return

        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    # Method to find a node in a tree
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True

###############################################################
    # Function to find lowest common ancestor
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.value > cur.value and q.value > cur.value:
                cur = cur.right
            elif p.value < cur.value and q.value < cur.value:
                cur = cur.left
            else:
                return cur
###############################################################

    # Method to display tree in inorder traversal
    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.value, end='  ')
        if self.right:
            self.right.inOrderTraversal()

    # Method to display tree in preorder traversal
    def preOrderTraversal(self):
        print(self.value, end='  ')
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()

    # Method to display tree in postorder traversal
    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.value, end='  ')

    # Method to display tree visually
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# Insert Nodes into Tree
tree = TreeNode()
tree.insert(6)
tree.insert(2)
tree.insert(8)
tree.insert(0)
tree.insert(4)
tree.insert(7)
tree.insert(9)
tree.insert(3)
tree.insert(5)

# Display tree visually
print("\nTree")
tree.display()
print()

##########################################

p = TreeNode(2)
q = TreeNode(8) 

result = tree.lowestCommonAncestor(tree, p, q)
print("The LCA of nodes", p.value, "and", q.value, "is: ", result.value)
##########################################