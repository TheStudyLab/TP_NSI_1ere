def ones_complement(binary_str):
    """Compute the one's complement of a binary string."""
    complement_str = ""
    for bit in binary_str:
        if bit == '0':
            complement_str += '1'
        else:
            complement_str += '0'
            
    return complement_str

def twos_complement(binary_str):
    """Compute the two's complement of a binary string."""
    # Step 1: Get the one's complement
    ones = ones_complement(binary_str)
    
    # Step 2: Add 1 to the one's complement from right to left
    ones_list = list(ones)
    carry = 1
    
    for i in range(len(ones_list) - 1, -1, -1):
        if ones_list[i] == '1' and carry == 1:
            ones_list[i] = '0'
            carry = 1
        elif ones_list[i] == '0' and carry == 1:
            ones_list[i] = '1'
            carry = 0
            break
        else:
            break
            
    return "".join(ones_list)
