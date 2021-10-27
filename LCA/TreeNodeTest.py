import unittest
from TreeNode import TreeNode

class TestTreeNode(unittest.TestCase):

    def setUp(self):
        global testNode
        testNode = TreeNode(1,None,None);

    def test_right_is_none(self):
        self.assertEqual(None, testNode.right);

    def test_left_is_none(self):
        self.assertEqual(None, testNode.left);

if __name__ == "__main__":
    unittest.main()