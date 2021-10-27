import unittest
from LCA import LCA
from TreeNode import TreeNode

class TestLCA(unittest.TestCase):

    #
    # Here is an example tree we can use for our testing.
    #     1
    #    / \
    #   2   5
    #  /   / \
    # 3   4   6
    #

    def setUp(self):
        global lca
        global root
        global two
        global three
        global four
        global five
        global six
        lca = LCA();
        three = TreeNode(3,None,None);
        four = TreeNode(4,None,None);
        six = TreeNode(6,None,None);
        two = TreeNode(2,three,None);
        five = TreeNode(5,four,six);
        root = TreeNode(1,two,five);

    def test_no_node(self):
        self.assertEqual(None, lca.lowestCommonAncestor(five,three,six));

    def test_parent_and_child(self):
        self.assertEqual(five, lca.lowestCommonAncestor(root,five,six));

    def test_same_parent(self):
        self.assertEqual(five, lca.lowestCommonAncestor(root,four,six));

    def test_invalid_node(self):
        invalid = TreeNode(-1,None,None);
        self.assertEqual(None, lca.lowestCommonAncestor(root,invalid,six));

    def test_same_depth(self):
         self.assertEqual(root, lca.lowestCommonAncestor(root,three,six));

    def test_root_and_another(self):
        self.assertEqual(root, lca.lowestCommonAncestor(root,root,six));

if __name__ == "__main__":
    unittest.main()