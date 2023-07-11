class Jar:

    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity > 0:
            raise ValueError ("Wrong input")
        self.capacity = capacity
        self.cookies = []

    def __str__(self):
        return "🍪" * len(self.cookies)

    def deposit(self, n):
        if len(self.cookies) + n >self.capacity:
            raise ValueError ("Wrong input")
        self.cookies.extend([None]*n)


    def withdraw(self, n):
        if len(self.cookies) < n:
            raise ValueError ("Wrong input")
        del self.cookies[-n:]

    @property
    def capacity(self):
        return self.capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Wrong input")
        if len(self._cookies) > value:
            raise ValueError ("Wrong input")
        self._capacity = value


    @property
    def size(self):
        return len(self.cookies)