#include <stdlib.h>
#include <string.h>
#include <limits.h>

int minRound, maxRound;
char visited[29][29][29]; // memo[len][a][b]

void dfs(int round, int* players, int len, int first, int second) {
    int a = -1, b = -1;
    for (int i = 0; i < len; i++) {
        if (players[i] == first) a = i;
        if (players[i] == second) b = i;
    }
    if (a == -1 || b == -1) return; // if one of them was eliminated (invalid path)

    if (a > b) {
        int tmp = a;
        a = b;
        b = tmp;
    }

    if (a + b + 2 == len + 1) {
        if (round < minRound) minRound = round;
        if (round > maxRound) maxRound = round;
        return;
    }

    if (visited[len][a][b]) return;
    visited[len][a][b] = 1;

    int i = 0, j = len - 1;
    int half = len / 2;
    int mid = (len % 2 == 1) ? players[half] : -1;

    // bitmask simulation for all undecided matches
    int maxMask = 1 << half;

    for (int mask = 0; mask < maxMask; ++mask) {
        int next[28];
        int p = 0;
        int skip = 0;

        while (i < j) {
            int left = players[i];
            int right = players[j];

            if (left == first || left == second) {
                next[p++] = left;
            } else if (right == first || right == second) {
                next[p++] = right;
            } else {
                int win = (mask >> (i)) & 1 ? left : right;
                next[p++] = win;
            }

            i++; j--;
        }

        if (mid != -1) {
            next[p++] = mid;
        }

        // sort by original player numbers for the next round
        for (int m = 0; m < p - 1; ++m) {
            for (int n = m + 1; n < p; ++n) {
                if (next[m] > next[n]) {
                    int tmp = next[m];
                    next[m] = next[n];
                    next[n] = tmp;
                }
            }
        }

        dfs(round + 1, next, p, first, second);
        i = 0;
        j = len - 1;
    }
}

int* earliestAndLatest(int n, int firstPlayer, int secondPlayer, int* returnSize) {
    int players[28];
    for (int i = 0; i < n; i++) players[i] = i + 1;

    memset(visited, 0, sizeof(visited));
    minRound = INT_MAX;
    maxRound = 0;

    dfs(1, players, n, firstPlayer, secondPlayer);

    int* res = (int*)malloc(2 * sizeof(int));
    res[0] = minRound;
    res[1] = maxRound;
    *returnSize = 2;
    return res;
}
