class Array:
    """
    @summary: Class-based dict allowing tuple subscripting and sparse data.
    """
    def __init__(self, p, m, n):
        """
        @summary: Create an M-element list of N-element row lists and
                  P-element pages
        @param p: Pages number of the array
        @param m: Rows number of the array
        @param n: Cols number of the array
        @type p: int
        @type m: int
        @type n: int
        """
        self._data = {}
        self._pages = p
        self._rows = m
        self._cols = n

    def __getitem__(self, key):
        """
        @summary: Returns the appropriate element for a three-element
                  subscript tuple.
        @param key: The key by which value will be located in the array.
        @type key: int
        @return: array element value if it is located | 0 if element
                 is not found
        @type: int
        @raise: KeyError if subscript is forbidden
        """
        page, row, col = self._validate_key(key)
        try:
            return self._data[page, row, col]
        except KeyError:
            return 0

    def __setitem__(self, key, value):
        """
        @summary: Sets the appropriate element for a two-element
                  subscript tuple.
        @param key: The key of the array where the value will be stored
        @param value: The value of the key to be stored
        """
        page, row, col = self._validate_key(key)
        self._data[page, row, col] = value

    def _validate_key(self, key):
        """
        @summary: Validates a key against the array's shape, returning
                  good tuples. Raise KeyError on problems.
        @raise KeyError: In case the key is invalid
        @return: The key if it is valid one
        @rtype: int
        @raise: KeyError if subscript is forbidden
        """
        page, row, col = key
        if (0 <= page < self._pages
            and 0 <= row < self._rows
                and 0 <= col < self._cols):
            return key
        raise KeyError("Subscript out of range")