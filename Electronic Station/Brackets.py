def checkio(exp):
    x=len(exp)
    y=[]
    z=False
    for i in exp:
        if i in set(["(","[","{"]):
            y.append(i)
        if i==")":
            if len(y)<=0 or y[-1]!="(":
                return False
            y.pop()
        if i=="]":
            if len(y)<=0 or y[-1]!="[":
                return False
            y.pop()
        if i =="}":
            if len(y)<=0 or y[-1]!="{":
                return False
            y.pop()
    if len(y)>0:
        return False
    return True