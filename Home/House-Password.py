def checkio(data):
    a=False
    b=False
    c=False
    y=False
    x=len(data)
    if (x>=10):
        DAscii=[ ord(z) for z in data ]
        for i in range(0,x-1):
            for j in range(48,57):
                if (DAscii[i]==j):
                    a=True
            for j in range(65,90):
                if (DAscii[i]==j):
                    b=True
            for j in range(97,122):
                if (DAscii[i]==j):
                    c=True
        if (a==True and b==True and c==True):
            y=True
    return y


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"