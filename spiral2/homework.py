def spiralize(size, n=1):
    m = 1
    for index in range(2, 501, 2):
        for reps in range(4):
            n += index
            m += n
    return m

