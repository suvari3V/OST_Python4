class MyDict(dict):
    def __init__(self, default_value):
        self.__dv = default_value
        super().__init__()

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except:
            return self.__dv