def spiralize(size, n=1):
    """ Your code goes somewhere in here"""
    n+= sum(4*i*i-6*(i-1)for i in range (3,size+1,2))
    return_value = n
    return return_value
