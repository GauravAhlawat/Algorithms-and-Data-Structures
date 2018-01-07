# importing the stack data structure
import stack

# function for checking whether the paranthesis are balanced or not using Stack, but only paranthesis, no charachers or integers
def parChecker(input_string):
    s = Stack() #creating a Stack
    balanced = True # variable for checking the balance
    index = 0
    while index < len(input_string) and balanced:
        symbol = input_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True # the paranthesis are balanced
    else:
        return False # the paranthesis are not balanced

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    # return True if they are the same type of paranthesis(opening and closing), which is they both will have the same index
    return opens.index(open) == closers.index(close)
