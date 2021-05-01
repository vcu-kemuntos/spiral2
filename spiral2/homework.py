def spiralize(size, n=1):
    """Your code goes somewhere in here"""
    m = [[0] * n for i in range(n)]
    x1, y1 = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += x1[i % 4]
            y += y1[i % 4]
            m[x][y] = c
            c += 1
    return m


