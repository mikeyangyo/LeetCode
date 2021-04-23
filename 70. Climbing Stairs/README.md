# 70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1**
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2**
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
``` 

**Constraints:**
- `1 <= n <= 45`

**Solution Idea**
If you want to climb to `n` stair, you need to climb to `n-1` stair or `n-2` stair.
So, distinct ways to `n` stair is sum of distinct ways to `n-1` stair and distinct ways to `n-2` stair.
The formula is like $F(n)=F(n-1)+F(n-2)$ *(Fibonacci sequence)*.
Therefore, **distinct ways to `n` stair is $(n+2)_{th}$ value in Fibonacci sequence**.