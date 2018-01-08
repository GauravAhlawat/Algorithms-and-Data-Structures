class Node:
    def __init__(self, init_val):
        self.data = init_val
        self.next_val = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_val

    def set_data(self, new_val):
        self.data = new_val

    def set_next(self, new_next):
        self.next_val = new_next


class unordered_list:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next = self.head
        self.head = temp

    def size(self):
        counter = 0
        current = self.head

        while current != None:
            counter = counter + 1
            current = current.get_next()

        return counter

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            val = current.get_data()
            if val == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        """we are assuming that the item we are searching for is sure to be in the list"""
        current = self.head()
        previous = None
        found = False

        while not found:
            val = current.get_data()
            if val == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
