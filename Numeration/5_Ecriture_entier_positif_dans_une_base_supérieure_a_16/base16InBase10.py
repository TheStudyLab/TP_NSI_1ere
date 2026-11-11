def hexadecimal_to_decimal(hex_str):
    """Convert a hexadecimal string (base 16) to a decimal integer (base 10)."""
    hex_chars = "0123456789ABCDEF"
    decimal_val = 0
    power = 0
    
    # Iterate from right to left
    for i in range(len(hex_str) - 1, -1, -1):
        char = hex_str[i].upper()
        # Find the numeric value of the hex character manually
        val = 0
        for idx, c in enumerate(hex_chars):
            if c == char:
                val = idx
                break
                
        decimal_val += val * (16 ** power)
        power += 1
        
    return decimal_val
