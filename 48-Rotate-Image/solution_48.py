"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Output: [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

Input: matrix = [
    [5,  1, 9,11],
    [2,  4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Input: matrix = [[1]]
Output: [[1]]

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

Constraints:
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

# for each row => for each col => m[n-1] swap m[0]
# rotate ring by ring (hard to figure out the location)
# same as https://leetcode.com/problems/rotate-image/discuss/19002/4ms-few-lines-C%2B%2B-code-Rotate-Image-90-degree-for-O(1)-space
# Tome: O(M), Space O(1)
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 1:
            return matrix

        leng = len(matrix)
        for i in range(leng - 1):
            for j in range(i, leng - 1 - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[leng - 1 - j][i]
                matrix[leng - 1 - j][i] = matrix[leng - 1 - i][leng - 1 - j]
                matrix[leng - 1 - i][leng - 1 - j] = matrix[j][leng - 1 - i]
                matrix[j][leng - 1 - i] = temp


class TransposeSolution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 1:
            return matrix

        n = len(matrix)

        # reflect vertically
        for i in range(n // 2):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - i][j]
                matrix[n - 1 - i][j] = temp

        # transpose:
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # inverse-transpose
        # for i in range(n - 1):
        #     for j in range(n - 1 - i):
        #         matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
