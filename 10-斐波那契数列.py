# -*- coding:utf-8 -*-
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''
#青蛙跳台阶。一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#n=1,一种跳法
#n=2,一次跳一个跳两次，一次跳两个跳一次，两种跳法
#n>2,n个台阶，设有f(n)个跳法
#第一次选择跳一个台阶，剩下的n-1个台阶有f(n-1)种跳法；
#第一次选择跳两个台阶，剩下的n-2个台阶有f(n-1)种跳法。
#所以当有n个台阶时，有f(n)=f(n-1)+f(n-2)种跳法。


class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]#初始的两值，之后一直更新这两值，后面一项等于前两项之和。
        if n >= 2:
            for i in range(2, n + 1):
                tempArray[i % 2] = tempArray[0] + tempArray[1]
        return tempArray[n % 2]


s=Solution()
print(s.Fibonacci(4))