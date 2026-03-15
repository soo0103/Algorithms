#include <iostream>
#include <map>
#include <cctype>
using namespace std;

#define fastio cin.tie(nullptr), ios_base::sync_with_stdio(false)

int N, M;
string s1, s2;
map<int, string> mp1;
map<string, int> mp2;

int main() {
    fastio;

    cin >> N >> M;

    for (int i = 1; i <= N; i++) {
        cin >> s1;
        mp1[i] = s1;
        mp2[s1] = i;
    }

    while (M--) {
        cin >> s2;
        if (isdigit(s2[0])) cout << mp1[stoi(s2)] << '\n';
        else cout << mp2[s2] << '\n';
    }

    return 0;
}