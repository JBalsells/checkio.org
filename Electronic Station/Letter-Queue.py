def letter_queue(commands):
    x=[]
    Str=""
    l=0
    for i in commands:
        if i[1]=='U':
            x.append(i[5])
        if i[1]=='O':
            if len(x)>0:
                del x[0]
    for i in x:
        Str+=i
    return Str




print letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])