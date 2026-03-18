#include <iostream>
#include <vector>
#include <deque>
using namespace std;

#define fastio cin.tie(nullptr); ios_base::sync_with_stdio(false)

using pii = pair<int, int>;

int T, M, N, K, X, Y;
int r, c, nr, nc;
int cnt;

vector<vector<int>> v;
vector<vector<bool>> visited;
vector<int> dr = {1, 0, -1, 0};
vector<int> dc = {0, 1, 0, -1};

void bfs(int row, int col) {
    deque<pii> dq;
    dq.push_back({row, col});

    while (!dq.empty()) {
        r = dq.front().first;
        c = dq.front().second;
        dq.pop_front();

        for (int i = 0; i < 4; i++) {
            nr = r + dr[i];
            nc = c + dc[i];

            if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                if (!visited[nr][nc] && v[nr][nc] == 1) {
                    visited[nr][nc] = true;
                    dq.push_back({nr, nc});
                }
            }
        }
    }
}

int main() {
    fastio;

    cin >> T;
    while (T--) {
        cin >> M >> N >> K;
        v.assign(N, vector<int>(M, 0));
        visited.assign(N, vector<bool>(M, false));
        while (K--) {
            cin >> X >> Y;
            v[Y][X] = 1;
        }

        cnt = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (v[i][j] == 1 && !visited[i][j]) {
                    bfs(i, j);
                    cnt++;
                }
            }
        }

        cout << cnt << '\n';
    }

    return 0;
}