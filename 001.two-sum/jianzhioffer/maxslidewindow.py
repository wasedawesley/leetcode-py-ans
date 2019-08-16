class Solution:
    def maxInWindows(self, num, size):
        # write code here
        # 存放可能是最大值的下标
        maxqueue = []
        # 存放窗口中最大值
        maxlist = []
        n = len(num)
        # 参数检验
        if n == 0 or size == 0 or size > n:
            return maxlist
        for i in range(n):
            print (i)
            print (maxqueue)
            # 判断队首下标对应的元素是否已经滑出窗口
            if len(maxqueue) > 0 and i - size >= maxqueue[0]:
                maxqueue.pop(0)
            print (maxqueue)
            while len(maxqueue) > 0 and num[i] > num[maxqueue[-1]]:
                maxqueue.pop()
            print (maxqueue)
            maxqueue.append(i)
            print (maxqueue)
            if i >= size - 1:
                maxlist.append(num[maxqueue[0]])
        return maxlist


s = Solution()
s.maxInWindows([2,3,4,2,6,2,5,1], 3)