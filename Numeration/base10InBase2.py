# print(bin(int(input("Enter a number : "))))

# ---

def binaire(n: int):
    binary = []
    value = ""
    while n != 0:
        if n % 2 == 1: 
            binary.append(1)
        elif n % 2 == 0:
            binary.append(0)
        n //= 2
    for i in range(len(binary)-1, -1, -1):
        value += str(binary[i])
    return "0b" + value
            
print(binaire(int(input("Enter a new number : "))))
