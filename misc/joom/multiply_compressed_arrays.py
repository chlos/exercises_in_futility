
# a
# b

# s = a[0]*b[0] + ... + a[1000]*b[1000]


# compression:
# V: [0, 0, 1, 6, 6, 6]
# RLE: [[2, 0], [1, 1], [3, 6]]

# [2,4]
# *
# [2,3]

def multArrays(a, b):
    result = 0

    virt_i = 0
    ai, bi = 0, 0
    packed_ai, packed_bi = 0, 0
    while ai < len(a) and bi < len(b):
        packed_a = a[ai]
        packed_b = b[bi]
        val_a = packed_a[1]
        val_b = packed_b[1]
        count_a = packed_a[0]
        count_b = packed_b[0]
        
        result += val_a * val_b
        
        if packed_ai < count_a - 1:
            packed_ai += 1
        else:
            ai += 1
            packed_ai = 0
        if packed_bi < count_b - 1:
            packed_bi += 1
        else:
            bi += 1
            packed_bi = 0
    
    return result





