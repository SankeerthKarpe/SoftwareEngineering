class LCA:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, node1, node2):
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the self node is one of node1 or node2
            current = current_node == node1 or current_node == node2

            # If it is self node
            if left and right or left and current or right and current :
                self.ans = current_node

            return current or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans 