def checkio(a, b, c):
    import math
    Numbers=[a,b,c]
    Numbers.sort()
    if Numbers[0]+Numbers[1]>Numbers[2]:
        Alpha=(180/float(math.pi))*math.acos((Numbers[1]**2+Numbers[2]**2-Numbers[0]**2)/float(2*Numbers[1]*Numbers[2]))
        Alpha=int(round(Alpha/1.)*1)
        Beta=(180/float(math.pi))*math.acos((Numbers[0]**2+Numbers[2]**2-Numbers[1]**2)/float(2*Numbers[0]*Numbers[2]))        
        Beta=int(round(Beta/1.)*1)
        Gamma=(180/float(math.pi))*math.acos((Numbers[0]**2+Numbers[1]**2-Numbers[2]**2)/float(2*Numbers[0]*Numbers[1]))
        Gamma=int(round(Gamma/1.)*1)
        return [Alpha,Beta,Gamma]
    else:
        return [0,0,0]

print checkio(11,20,30)

#a^2 = b^2 + c^2 - 2bc cos(a) 
#b^2 = a^2 + c^2 - 2ac cos(b) 
#c^2 = a^2 + b^2 - 2ab cos(c) 