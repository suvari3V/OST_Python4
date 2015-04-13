class sstr(str):
    """
    Implements the lshitf ("<<") and rshift (">>") methods as a cyclic
    shifting of the characters in the string.
    """
    def __init__(self, string, *args, **kwargs):
        if not isinstance(string, str):
            raise ValueError("Class argument must be string")
        if not string:
            raise ValueError("Class argument cannot be empty string")
        super(sstr, self).__init__(*args, **kwargs)
        self.string = string

    def __lshift__(self, shift_val):
        if not isinstance(shift_val, int):
            raise ValueError("Shift value must be integer")
        if shift_val < 0:
            raise ValueError("Shift value cannot be negative")
        shifted_str = self.string[shift_val:] + self.string[:shift_val]
        return sstr(shifted_str)

    def __rshift__(self, shift_val):
        if not isinstance(shift_val, int):
            raise ValueError("Shift value must be integer")
        if shift_val < 0:
            raise ValueError("Shift value cannot be negative")
        shifted_str = self.string[-shift_val:] + self.string[:-shift_val]
        return sstr(shifted_str)

    def __str__(self):
        return self.string