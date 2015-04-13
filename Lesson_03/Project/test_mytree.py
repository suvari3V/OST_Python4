from mytree import MyTree
import unittest


class TestMyTree(unittest.TestCase):
    def test_insert(self):
        try:
            tree_data = "BJQKFAC"
            my_tree = MyTree("D", tree_data)
            for i, c in enumerate(tree_data):
                my_tree.insert(c)
        except ValueError as e:
            self.fail("Unable to insert tree data: {}".format(e))

    def test_missing_key(self):
        tree_data = "BJQKFAC"
        my_tree = MyTree("D", tree_data)
        for i, c in enumerate(tree_data):
                my_tree.insert(c)
        self.assertRaises(KeyError, my_tree.find, "P")

    def test_existing_key(self):
        try:
            tree_data = "BJQKFAC"
            my_tree = MyTree("D", tree_data)
            for i, c in enumerate(tree_data):
                    my_tree.insert(c)
            my_tree.find("J")
        except Exception as e:
            self.fail("Unable to find existing key: {}".format(e))

    def test_walk(self):
        try:
            tree_data = "BJQKFAC"
            my_tree = MyTree("D", tree_data)
            for i, c in enumerate(tree_data):
                    my_tree.insert(c)
            my_tree.walk()
        except Exception as e:
            self.fail("Unable to walk through the tree: {}".format(e))

if __name__ == '__main__':
    unittest.main()