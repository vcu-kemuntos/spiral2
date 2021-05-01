def spiralize(size, n=1):
    """Your code goes somewhere in here"""
    size=501
    for i in range(3, size+1, 2):
        n+= 4*i*i-6*i+6
    return_value = n
    return return_value
