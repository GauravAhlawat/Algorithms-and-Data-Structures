class deque:
    def __init__(self):
        self.items = list()

    def add_front(self, item):
        self.items.append(item)

    def add_back(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_back(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
