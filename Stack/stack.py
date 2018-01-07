class Stack:
    # creating the abstract data structure Stack using List where the top of the stack is the end of the list data type
    def __init__(self):
        #initalizing the class Stack
        self.items = []

    def isEmpty(self):
        # method for checking whether the stack is empty
        return self.items == []

    def push(self, item):
        # method for adding a new item to the stack
        self.items.append(item)

    def pop(self):
        # method for removing the item present at the top of the stack
        return self.items.pop()

    def peek(self):
        # method for checking what the top item at the stack at present
        return self.items[len(self.items) - 1]

    def size(self):
        # method for returning the size of the stack
        return len(self.items)


# reversing a string using the stack class implemented above
def revstring(x):
    s = Stack()
    for i in x:
        s.push(i)
    reversed_string = ''
    while not s.isEmpty():
        popped = s.pop()
        reversed_string = reversed_string + popped
    return (reversed_string)


def main():
    string_in = input("Please enter a string you want a reverse off")
    string_reversed = revstring(string_in)
    print("the reversed string is: %s" % string_reversed)

if __name__ == '__main__':
    main()
