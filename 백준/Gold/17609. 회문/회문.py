import sys

def is_palindrome(s):
    if s == s[::-1]:
        print(0)
        return

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            remove_left = s[:left] + s[left+1:]
            if remove_left == remove_left[::-1]:
                print(1)
                return
            
            remove_right = s[:right] + s[right+1:]
            if remove_right == remove_right[::-1]:
                print(1)
                return

            print(2)
            return

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        sentence = sys.stdin.readline().strip()
        
        is_palindrome(sentence)