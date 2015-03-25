def verify_anagrams(fw, sw):
    Resp=False
    Flag=0
    fw=fw.replace(" ","")
    sw=sw.replace(" ","")
    fwArr=[ ord(z) for z in fw.lower() ]
    swArr=[ ord(z) for z in sw.lower() ]
    x=len(fwArr)
    y=len(swArr)
    if x==y:
        for i in range(97,122):
            if fwArr.count(i)==swArr.count(i) and Flag==0:
                Resp=True
            else:
                Resp=False
                Flag=1
    return Resp
    
print verify_anagrams("Kyoto", "Tokyo")
    