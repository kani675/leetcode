#include <stdio.h>
#include <stdlib.h>

#define MAX_K 1001

int maximumLength(int* nums, int numsSize, int k) {
    int dp[numsSize][MAX_K];
    int maxLen = 1;

    // Initialize all to 1 (every element is a valid subsequence of length 1)
    for (int i = 0; i < numsSize; i++)
        for (int mod = 0; mod < k; mod++)
            dp[i][mod] = 1;

    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < i; j++) {
            int mod = (nums[j] + nums[i]) % k;
            if (dp[j][mod] + 1 > dp[i][mod]) {
                dp[i][mod] = dp[j][mod] + 1;
                if (dp[i][mod] > maxLen)
                    maxLen = dp[i][mod];
            }
        }
    }

    return maxLen;
}
