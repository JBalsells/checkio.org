def checkio(data):
    Roman=''
    temp=int(data)
    mult=int(temp/1000)
    rest=int(temp%1000)
    for i in range(0,mult):
        Roman+='M'
    temp=int(rest)
    mult=int(temp/100)
    rest=int(temp%100)
    
    if mult==9:
        Roman+='CM'
    if mult>=6 and mult<=8:
        Roman+='D'
        for i in range(5,mult):
            Roman+='C'
    if mult==5:
        Roman+='D'
    if mult==4:
        Roman+='CD'
    if mult<=3 and mult>0:
        for i in range(0,mult):
            Roman+='C'
            
    temp=int(rest)
    mult=int(temp/10)
    rest=int(temp%10)

    if mult==9:
        Roman+='XC'
    if mult>=6 and mult<=8:
        Roman+='L'
        for i in range(5,mult):
            Roman+='X'
    if mult==5:
        Roman+='L'
    if mult==4:
        Roman+='XL'
    if mult<=3 and mult>0:
        for i in range(0,mult):
            Roman+='X'

    if rest==9:
        Roman+='IX'
    if rest>=6 and rest<=8:
        Roman+='V'
        for i in range(5,rest):
            Roman+='I'
    if rest==5:
        Roman+='V'
    if rest==4:
        Roman+='IV'
    if rest<=3 and rest>0:
        for i in range(0,rest):
            Roman+='I'
            
    return Roman