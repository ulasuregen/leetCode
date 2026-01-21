############################################################################
# Given the root of a binary tree, return its maximum depth.               #
#                                                                          #
# A binary tree's maximum depth is the number of nodes along the longest   #
# path from the root node down to the farthest leaf node.                  #
############################################################################
import time

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def makeTree(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def compareFunctions(f1, f2, inputs):
    print('\n')

    s_time = time.time()
    f1(*inputs)
    duration1 = time.time() - s_time

    s_time = time.time()
    f2(*inputs)
    duration2 = time.time() - s_time

    fastest, lowest = (f1.__name__, f2.__name__) if duration1 < duration2 else (f2.__name__, f1.__name__)
    duration1, duration2 = (duration1, duration2) if duration1 < duration2 else (duration2, duration1)

    def_n_space = max(len(fastest), len(lowest))

    print(
    f"{fastest:<{def_n_space}} -> {duration1:.10f} sec\n"
    f"{lowest:<{def_n_space}} -> {duration2:.10f} sec\n"
    f"{'Diff':<{def_n_space+2}}: {((duration2 - duration1) / duration2) * 100:.0f}%")

    print('\n')

# This is my first attempt.
# It searches layer by layer until there is no lower layer.
# It works, but it is not fast enough, and its readability is not very good.
def maxDepthFirst(root):
        queue = [root] if root is not None else []
        next_queue = []
        i = 0

        while queue:   
            node = queue.pop()
            next_queue.extend([x for x in [node.left, node.right] if x is not None])

            if not queue:
                i += 1
                queue = next_queue[:]
                next_queue = []

        return i


# This version uses recursion, and its readability is very simple.
# It also runs faster.
# I need to remind myself to check for a recursive solution.
def maxDepthSecond(root):
        if not root:
            return 0
        
        return max(maxDepthSecond(root.left) + 1, maxDepthSecond(root.right)+1)



# Ex1:  
root = makeTree('[3,9,20,null,null,15,7]')
compareFunctions(maxDepthFirst, maxDepthSecond, [root])

# Ex2:
root = makeTree('[0,0,0,0,null,null,0,null,null,null,0]')
compareFunctions(maxDepthFirst, maxDepthSecond, [root])