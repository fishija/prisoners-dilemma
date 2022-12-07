def to_binary(i):
    return bin(i)[2:]

def to_binary_length(i, l):
    temp = bin(i)[2:]
    return temp.zfill(l)
