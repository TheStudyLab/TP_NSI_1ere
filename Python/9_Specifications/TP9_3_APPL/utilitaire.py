def maximum(a, b):
    if a > b:
        return a
    if b > a:
        return b
    else:
        return a,b

def main():
    print("Test du maximum :", maximum(10, 5))
    print("Test du maximum :", maximum(6, 6))
    
if __name__ == "__main__":
    main()
    pass # @JiaN0w
