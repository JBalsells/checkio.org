def checkio(data):
    dt=[]
    for i in range(len(data[0])):
        dt.append([])
        for j in range(len(data)):
            dt[i].append(data[j][i])
    return dt
    
print checkio([[1, 2, 3, 0],[4, 5, 6, 9],[7, 8, 1, 2]])