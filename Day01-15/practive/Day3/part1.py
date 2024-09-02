class Room:
    __slots__ = ('_name', '_owner', '_width', '_length', '_high')

    def __init__(self, name, owner, width, length, high):
        self._name = name
        self._owner = owner
        self._width = width
        self._length = length
        self._high = high

    @property
    def cal_area(self):
     return self.width * self.length

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value