def Rest_Sum(lista, x, listatot):
    if x < len(lista):
        return Rest_Sum(lista, x+1, listatot+lista[x])
    else:
        return listatot

def checkio(data):
    return Rest_Sum(data, 0, 0)
    
    
    
print(checkio([2, 2, 2, 2, 2, 2]))