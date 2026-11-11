def decimal_to_binary(n):
    """Convert a positive integer from base 10 to base 2."""
    if n == 0:
        return "0"
    
    binary_str = ""
    while n > 0:
        remainder = n % 2
        # Prepend the remainder to build the binary string from right to left
        binary_str = str(remainder) + binary_str
        n = n // 2
        
    return binary_str
