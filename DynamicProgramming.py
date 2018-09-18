# Leetcode 198. House Robber
# f(k) = max(f(k-1), f(k-2)+nums(k))
class Solution198(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0
        now = 0
        for i in nums:
            last, now = now, max(now, last + i)
        return now


# Leetcode 338. Counting Bits
# f(k) = k%2 + f(k/2)
class Solution338(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # solution 1: slow
        if num <= 1:
            return list(range(num + 1))
        ones = [0, 1]
        n = 1
        i = 2
        while i <= num:
            if i == 2**n:
                n += 1
            ones.append(ones[i-2**(n-1)] + 1)
            i += 1
        return ones
        # solution 2:fast
        ones = [0]
        for i in range(1, num+1):
            ones.append(i%2 + ones[i/2])
        return ones


# Leetcode 413. Arithmetic Slices
class Solution413(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum = 0
        curr = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                curr += 1
                sum += curr
            else:
                curr = 0
        return sum

# Leetcode 647. Palindromic Substrings
class Solution647(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # solution 1: DP, > 6%
        p = []
        for i in range(len(s)):
            row = []
            for j in range(len(s)):
                row.append(0)
            p.append(row)
            
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                p[i][j] = 1 if s[i] == s[j] and (i+1 > j-1 or p[i+1][j-1] == 1) else 0
        result = 0
        for i in p:
            result += sum(i)
        return result
        
        # solution 2, > 49%
        ans = 0
        for i in range(2*len(s)-1):
            left = int(i / 2)
            right = left + i%2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
        return ans

# Leetcode 650. 2 Keys Keyboard
class Solution650(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        d = 2
        while n > 1:
            while n % d == 0:
                res += d
                n /= d
            d += 1
        return res

# Leetcode 486. Predict the Winner
class Solution486(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        dp = [[0]*N for i in range(N)]
        for i in range(N-1, -1, -1):
            for j in range(i, N):
                score_right = 0 if i == N-1 else dp[i+1][j]
                score_left = 0 if j == 0 else dp[i][j-1]
                dp[i][j] = max(nums[i] - score_right, nums[j] - score_left)
        return dp[0][N-1] >= 0

# Leecode 



# Nowcoder: https://www.nowcoder.com/question/next?pid=6910869&qid=126953&tid=17260778
def min_sum(N, nums):
    dp = [[0]*N for i in range(N)]
    for i in range(2, N):
        dp[i][i-1] = dp[i-1][i-2] + abs(nums[i-1] - nums[i-2])
    
    for i in range(2, N):
        for j in range(i):
            if i - 1 == j:
                min_temp = 1 << 30
                for k in range(i-1):
                    temp = dp[i-1][k] + abs(nums[k] - nums[i])
                    if temp < min_temp:
                        min_temp = temp
                dp[i][j] = min(min_temp, dp[i][j])
            else:
                dp[i][j] = dp[i-1][j] + abs(nums[i] - nums[i-1])
    return min(dp[N-1][:N-1])
    
if __name__ == '__main__':
    N = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    if N <= 2:
        print(0)
    else:
        print(min_sum(N, nums))


