class LCA(object):
    class TreeNode(object):
        def __init__(self, x):
            self.val = x

            self.left = None
            self.right = None

    def lowestCommonAncestor(self, root, p, q):

        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if not left:
            return right

        if not right:
            return left;
