import pytest

from LCA import LCA


class TestLCA(object):

    @pytest.fixture
    def testing_tree(self):
        node = LCA.TreeNode(3)                                      # _3_
        node.left = LCA.TreeNode(5);                              # /      \
        node.right = LCA.TreeNode(1);                           # _5_       1
        node.left.left = LCA.TreeNode(6);                      # /     \    /  \
        node.left.right = LCA.TreeNode(2);                      # 6       2   0    8
        node.left.right.left = LCA.TreeNode(7);                # /  \
        node.left.right.right = LCA.TreeNode(4);             # 7     4
        node.right.left = LCA.TreeNode(0);
        node.right.right = LCA.TreeNode(8);

        return node

    def test_tree_empty(self):
        assert LCA.lowestCommonAncestor(LCA(), None, None, None) is None

    def test_single_node(self):
        node = LCA.TreeNode(3)
        node.left = None
        node.right = None

        assert LCA.lowestCommonAncestor(LCA(), node, node, node.left).val == 3

    def test_LCA_on_same_level(self, testing_tree):
        assert LCA.lowestCommonAncestor(LCA(), testing_tree, testing_tree.left, testing_tree.right).val == 3

    def test_LCA_one_node_behind(self, testing_tree):
        assert LCA.lowestCommonAncestor(LCA(), testing_tree, testing_tree.left, testing_tree.left.right.right).val == 5

    def test_LCA_beside_each_other(self, testing_tree):
        node = LCA.TreeNode(1);
        node.left = LCA.TreeNode(2);

        assert LCA.lowestCommonAncestor(LCA(), node, node, node.left).val == 1

    def test_diff_subtree_and_diff_level(self, testing_tree):
        assert LCA.lowestCommonAncestor(LCA(), testing_tree, testing_tree.left, testing_tree.right.right).val == 3

    if __name__ == '__main__':
        pytest.main()
