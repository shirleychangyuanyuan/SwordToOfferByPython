# -*- coding:utf-8 -*-
#一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。f(n）=2^(n-1)
#青蛙变态跳台阶。
#n=1,一种跳法
#n=2,一次跳一个跳两次，一次跳两个跳一次，两种跳法
#n>2,n个台阶，设有f(n)个跳法
#第一次选择跳一个台阶，剩下的n-1个台阶有f(n-1)种跳法；
#第一次选择跳两个台阶，剩下的n-2个台阶有f(n-1)种跳法。
#第一次选择跳三个台阶，剩下的n-3个台阶有f(n-3)种跳法。
#……
#第一次选择跳n个台阶，有1种跳法。
#所以当有n个台阶时，有f(n)=f(n-1)+f(n-2)+f(n-3)+……+f(1)种跳法。
#f(n-1)=f(n-2)+f(n-3)+f(1)
#两式相减，f(n)=2f(n-1)=2^2f(n-2)=……=2^(n-1)f(1)
class Solution:
    def jumpFloorII(self, number):
        # write code here
        ans=1
        if number>=2:
            for i in range(number-1):#for i in range(n)循环n次
                ans=ans*2
        return ans


s=Solution()
print(s.jumpFloorII(2))