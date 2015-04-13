class MyTree:
    def __init__(self, key, data):
        """
        @summary: Create a new tree node
        @param key: The master key of the node.
        @param data: The data to be stored as an additional attribute to
                     each node.
        @type key: string
        @type data: list
        """
        self.key = key
        self.left = self.right = None
        self.data = data

    def insert(self, key):
        """
        @summary: Insert a key into a tree
        @param key: string
        @raise ValueError: If key already exist in the tree
        """
        if key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = MyTree(key, self.data[self.data.index(key)+1:])
        elif key > self.key:
            if self.right:
                self.right.insert(key)
            else:
                self.right = MyTree(key, self.data[self.data.index(key)+1:])
        else:
            raise ValueError("Attempt to insert a duplicate value")

    def find(self, key):
        """
        @summary: Locate a key in a tree and return the data associated with
                  the node.
        @param key: Key to find in the tree
        @type key: string
        @raise KeyError: If the key is not present in the tree
        """
        tree_data = list(self.walk())
        for node in tree_data:
            if node[0] == key:
                return node[-1]
        raise KeyError("Key is not present in the tree")

    def walk(self):
        """
        @summary: Generate the keys from the tree in sorted order.
        """
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key, self.data
        if self.right:
            for n in self.right.walk():
                yield n