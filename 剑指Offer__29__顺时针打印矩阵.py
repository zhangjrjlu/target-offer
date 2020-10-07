class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # ans = []
        # while matrix:
        #     ans.extend(matrix[0])
        #     matrix = list(zip(* matrix[1:]))[::-1]
        # return ans
        if not matrix or not matrix[0]:
            return list()

        row, column = len(matrix), len(matrix[0])
        if_visit = [ [False] * column for i in range(1, row+1) ]
        #print(if_visit)
        total_num = row * column
        #print(total_num)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        i, j = 0, 0
        order = []
        for a in range(total_num):
            order.append(matrix[i][j])
            if_visit[i][j] = True
            next_i = i + directions[directionIndex][0]
            next_j = j + directions[directionIndex][1]
            if not (0 <= next_i < row and 0 <= next_j < column and not if_visit[next_i][next_j]):
                directionIndex = (directionIndex + 1) % 4
            i = i + directions[directionIndex][0]
            j = j + directions[directionIndex][1]
        
        return order
