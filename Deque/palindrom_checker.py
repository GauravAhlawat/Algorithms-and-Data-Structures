import deque

def palindrome_checker(exp_string):
    exp_deque = deque()

    for c in exp_string:
        exp_deque.add_back(c)

    equal_c = True

    while exp_deque.size() > 1 and equal_c:
        first = exp_deque.remove_front()
        last = exp_deque.remove_back()
        if first != last:
            equal_c = False

    return equal_c

print(palindrome_checker("radar"))
print(palindrome_checker("hola-hala"))
