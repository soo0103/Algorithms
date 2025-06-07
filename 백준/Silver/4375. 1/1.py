while 1:
    try:
        n = int(input())
        
        target = 1
        length = 1
        
        while target % n != 0:
            target = target * 10 + 1
            length += 1
        
        print(length)
        
    except:
        break