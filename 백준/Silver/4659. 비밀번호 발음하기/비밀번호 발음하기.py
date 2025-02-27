import sys

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

while 1:
    pwd = sys.stdin.readline().strip()

    if pwd == "end":
        break

    flag = False

    for p in pwd:
        if p in vowels:
            flag = True

    if len(pwd) >= 2 and flag:
        for i in range(len(pwd) - 1):
            if pwd[i] == pwd[i + 1]:
                if pwd[i] not in "eo":
                    flag = False
                    break
                else:
                    i += 1
        
        if len(pwd) >= 3:
            for i in range(len(pwd) - 2):
                if pwd[i] in vowels and pwd[i + 1] in vowels and pwd[i + 2] in vowels:
                    flag = False
                    break
                elif pwd[i] in consonants and pwd[i + 1] in consonants and pwd[i + 2] in consonants:
                    flag = False
                    break
    
    if flag:
        print(f"<{pwd}> is acceptable.")
    else:
        print(f"<{pwd}> is not acceptable.")