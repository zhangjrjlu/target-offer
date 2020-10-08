class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1

        f = [ 1 for _ in range(n+1) ]
        #print(f)
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]

        return f[n] % 1000000007
