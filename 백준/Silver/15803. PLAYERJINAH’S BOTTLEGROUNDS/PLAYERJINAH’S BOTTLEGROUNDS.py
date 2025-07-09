import sys

INF = int(1e9)

def get_slope(p1, p2):
    if p2[0] - p1[0] == 0:
        return INF
    
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return slope

if __name__ == "__main__":
    team = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
    
    m = get_slope(team[0], team[1])
    n = get_slope(team[1], team[2])
    
    if m == n:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")