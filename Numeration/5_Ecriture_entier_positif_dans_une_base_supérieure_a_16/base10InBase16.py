def decimal_to_hexadecimal(n):
    """Convert a positive integer from base 10 to base 16."""
    if n == 0:
        return "0"
        
    hex_chars = "0123456789ABCDEF"
    hex_str = ""
    
    while n > 0:
        remainder = n % 16
        hex_str = hex_chars[remainder] + hex_str
        n = n // 16
        
    return hex_str
