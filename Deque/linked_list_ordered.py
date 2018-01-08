class Node:
    """Other remanining methods to be added"""
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

class ordered_list:
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() < item:
                    current = current.get_next()
                else:
                    stop = True
        return found
