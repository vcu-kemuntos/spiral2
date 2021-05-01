def spiralize(size, n=1):
    """Your code goes somewhere in here"""

    num = n

    for index in range(2, size, 2):
        for reps in range(4):
            num += index
            n += num

    return n




