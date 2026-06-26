#include <stdlib.h>

void dfs(int** image, int rows, int* cols, int r, int c, int origColor, int newColor){
    if(r < 0 || r >= rows || c < 0 || c >= cols[r]) return;
    if(image[r][c] != origColor) return;

    image[r][c] = newColor;
    dfs(image, rows, cols, r+1, c, origColor, newColor);
    dfs(image, rows, cols, r-1, c, origColor, newColor);
    dfs(image, rows, cols, r, c+1, origColor, newColor);
    dfs(image, rows, cols, r, c-1, origColor, newColor);
}

/**
 * LeetCode-compatible signature: return the modified image and set returnSize/returnColumnSizes.
 */
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {
    if(image == NULL || imageSize == 0 || imageColSize == NULL){
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int origColor = image[sr][sc];
    if(origColor != color){
        dfs(image, imageSize, imageColSize, sr, sc, origColor, color);
    }

    *returnSize = imageSize;
    *returnColumnSizes = (int*)malloc(sizeof(int) * imageSize);
    for(int i = 0; i < imageSize; ++i) (*returnColumnSizes)[i] = imageColSize[i];

    return image;
}
