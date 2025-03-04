import sys

def isAvailable():
    vowels = 0
    consonants = 0

    for i in range(len(s)):
        if s[i] in {'a', 'e', 'i', 'o', 'u'}:
            vowels += 1
        else:
            consonants += 1
        
    if vowels >= 1 and consonants >= 2:
        return True
    else:
        return False

def backtracking():
    if len(s) == L:
        if isAvailable():
            print(*s, sep = '')
            return

    for i in range(C):
        if not visited[i]:
            if not s or s[-1] < S[i]:
                visited[i] = True
                s.append(S[i])
                backtracking()
                s.pop()
                visited[i] = False

if __name__ == "__main__":
    L, C = map(int, sys.stdin.readline().split())
    S = list(sys.stdin.readline().split())

    S.sort()
    visited = [False] * C
    s = []

    backtracking()