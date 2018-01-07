class queue:
    """implementing the Queue Abstract data structure"""
    def __init__(self):
        # initializing the queue with list
        self.items = list()

    def isEmpty(self):
        # method for checking whether the queue is empty or not
        return self.items == []

    def enqueue(self, item):
        # method for adding a new item
        self.items.insert(0,item)

    def deque(self):
        # method for deleting the item following the FIFO way of doing things
        return self.items.pop()

    def size(self):
        # method for returning the size of the queue
        return len(self.items)
