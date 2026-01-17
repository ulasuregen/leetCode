class Solution(object):
    def inorderTraversal(self, root):      
        s = []
        self.rec(root, s)
        return s

    def rec(self, node, stack):
        if node is not None:
            self.rec(node.left, stack)
            stack.append(node.val)
            self.rec(node.right, stack)