#872. Leaf-Similar Trees
class Solution872(object):
    def leafSimilar(self, root1, root2):
        left = []
        right = []
        self.getLeaves(root1, left)
        self.getLeaves(root2, right)
        return left == right

    def getLeaves(self, root, leaf_arr):
        if not root:
            return
        if not root.left and not root.right:
            leaf_arr.append(root.val)
            return
        self.getLeaves(root.left, leaf_arr)
        self.getLeaves(root.right, leaf_arr)