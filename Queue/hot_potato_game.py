import queue

def hot_potato_game(names, num_of_rot):
    # function for playing the hot_potato_game with num_of_rot number of rotations
    name_queue = queue()
    for name in names:
        name_queue.enqueue(name)

    while name_queue > 1:
        for i in range(num_of_rot):
            name_queue.enqueue(name_queue.deque())

        name_queue.deque()

    return name_queue.deque()

print(hot_potato_game(['a','b','c'], 4))
