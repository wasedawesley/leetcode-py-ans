class Solution(object):
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """

    def dfs(left, path, res, n):
      if len(path) == 2 * n:
        if left == 0:
          res.append("".join(path))
        return

      if left < n:
        path.append("(")
        dfs(left + 1, path, res, n)
        path.pop()
      if left > 0:
        path.append(")")
        dfs(left - 1, path, res, n)
        path.pop()

    res = []
    dfs(0, [], res, n)
    return res

  def my(self, n):
    result = []
    def trace(S = "", left = 0, right = 0):
      # print (S, left, right)
      if len(S) == 2* n:
        result.append(S)
      if left < n:
        trace(S + '(', left +1, right )
        print('use', S , left, right)
      if right<left:
        trace(S + ')', left , right +1 )
        print('use', S , left, right)
    trace()
    return result




class Solution1:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #每次增加括号时需要判断之前字符串中左右括号的个数
        #判断增加‘(’或‘)’依据为，若之前字符串中左括号个数小于n，则应增加左括号，若之前字符串中右括号个数小于左括号，则应增加右括号
        result = []
        #函数嵌套
        def trackback(S = "", left = 0, right = 0):
            if len(S) == 2 * n:     #若当前字符串的长度等于2n则字符串存入列表中
                result.append(S)
            if left < n:
                trackback(S + '(', left + 1, right)
            if right < left:
                trackback(S + ')', left, right + 1)
            
        trackback()
        return result


# s = Solution1()
# print(s.generateParenthesis(3))

        
s = Solution()
print(s.my(3))
