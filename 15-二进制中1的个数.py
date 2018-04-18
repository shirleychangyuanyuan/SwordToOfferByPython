# -*- coding:utf-8 -*-
#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
#把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0.
class Solution:
    def NumberOf1(self, n):
        # write code here
        count=0
        if n<0:
            n=n& 0xffffffff
        while n:

            n=(n-1)&n
            count += 1
        return count

s=Solution()
print(s.NumberOf1(-2))