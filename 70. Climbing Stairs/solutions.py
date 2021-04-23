class Solution:
    def climbStairs(self, n: int) -> int:
        fibonacci_arr = [1, 2]
        if n <= 2:
            return n
        for _ in range(3, n + 1):
            fibonacci_arr.append(fibonacci_arr[-1] + fibonacci_arr[-2])
        return fibonacci_arr[-1]


if __name__ == '__main__':
    assert (Solution().climbStairs(1) == 1)
    assert (Solution().climbStairs(2) == 2)
    assert (Solution().climbStairs(3) == 3)
    assert (Solution().climbStairs(4) == 5)
    print('all test cases pass')
