def checkio(text):
    text=text.lower()
    y=0
    for i in text:
        if ord(i)>=97 and ord(i)<=122:
            if text.count(i)>y:
                y=text.count(i)
                z=i
            if text.count(i)==y:
                if ord(z)>ord(i):
                    z=i
    return z
    
    
    
print checkio("aAaAaFfFfFfEeEeEe")