class Solution(object):
  def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    dp = [0 for _ in range(0, len(s))]
    left = 0
    ans = 0
    for i in range(0, len(s)):
      if s[i] == "(":
        left += 1
      elif left > 0:
        left -= 1
        dp[i] = dp[i - 1] + 2
        j = i - dp[i]
        if j >= 0:
          dp[i] += dp[j]
        ans = max(ans, dp[i])
    return ans


  def longestValidParentheses_(self, s):
    dp, res = [0] * len(s), 0  # 初始化dp、定义最优结果变量
    for i in range(len(s)):
        
        if s[i] == ')':  # 只考虑以')'结尾的子串
            if i > 0 and s[i - 1] == '(':  # 第一中情况，直接加 2
                
                dp[i] = dp[i - 2] + 2
            if i > 0 and s[i - 1] == ')':  # 第二种情况，
                if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] - 1 > 0:  # 当前合法子串，前面还有子串，的情况
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:  # 当前合法子串，前面--没有--子串，的情况
                        dp[i] = dp[i - 1] + 2
            res = max(res, dp[i])  # 更新最长的合法子串
    return res
  def longestValidParentheses_stack(self, s):
        stack, res = [-1], 0
        for i, e in enumerate(s):
            print('(', stack)
            if e == '(':
                stack.append(i)
                
            elif e == ')':  # 出栈
                stack.pop()
                if not stack:  # 如果栈为空，当前 位置索引 进栈，做为一个新的子串的开始（主要用作求合法子串的长度）
                    stack.append(i)
                    # print(')', stack)
                else:
                    res = max(res, i - stack[-1])  # 更新合法子串的长度
        return res


s = ')()())'
solu = Solution()
print(solu.longestValidParentheses_stack(s))