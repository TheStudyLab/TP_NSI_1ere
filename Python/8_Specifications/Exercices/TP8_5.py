def ou_exclusif(a, b):
    if len(a) == len(b):
        result = []
        for i in range(len(a)):
            if a[i] == b[i]:
                result.append(0)
            else:
                result.append(1)
        return(result)
    else:
        return("The lists don't have the same length.")
    
print(ou_exclusif([1, 0, 1, 0], [1, 1, 1, 1]))
