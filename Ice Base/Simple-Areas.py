def simple_areas(P1,*P2):
    import math
    if len(P2)==0:
        Area=math.pi*(P1/float(2))**2
        Area=round(Area/0.01)*0.01
    if len(P2)==1:
        Area=P1*P2[0]
        #Area=round(Area/0.01)*0.01
    if len(P2)==2:
        #Heron
        SemiPmt=(P1+P2[0]+P2[1])/float(2)
        Area=math.sqrt(SemiPmt*(SemiPmt-P1)*(SemiPmt-P2[0])*(SemiPmt-P2[1]))
    return Area
    
    
print simple_areas(1,1,1)