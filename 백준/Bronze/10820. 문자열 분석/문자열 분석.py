while 1:
    try:
        seq = list(input())

        lower = 0
        upper = 0
        num = 0
        space = 0
        
        for i in range(len(seq)):
            code = ord(seq[i])

            if 97 <= code <= 122:
                lower += 1
            elif 65 <= code <= 90:
                upper += 1
            elif code == 32:
                space += 1
            else:
                num += 1

        print(lower, upper, num, space)

    except:
        break