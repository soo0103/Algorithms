import sys

k = list(map(int, str(sys.stdin.readline().strip())))

if len(k) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    d = k[1] - k[0]
    flag = True

    for i in range(2, len(k)):
        if k[i] - k[i - 1] == d:
            continue
        else:
            flag = False

    if flag:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    else:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")