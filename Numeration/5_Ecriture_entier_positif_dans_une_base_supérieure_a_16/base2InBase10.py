def binary_to_decimal(binary_str):
    """Convert a binary string (base 2) to a decimal integer (base 10)."""
    decimal_val = 0
    power = 0
    
    # Iterate from right to left without using reversed()
    for i in range(len(binary_str) - 1, -1, -1):
        bit = int(binary_str[i])
        decimal_val += bit * (2 ** power)
        power += 1
        
    return decimal_val
