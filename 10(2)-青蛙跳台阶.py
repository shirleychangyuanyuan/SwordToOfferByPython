# -*- coding:utf-8 -*-
#一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#从斐波那契数列的第二项开始
#青蛙跳台阶。一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#n=1,一种跳法
#n=2,一次跳一个跳两次，一次跳两个跳一次，两种跳法
#n>2,n个台阶，设有f(n)个跳法
#第一次选择跳一个台阶，剩下的n-1个台阶有f(n-1)种跳法；
#第一次选择跳两个台阶，剩下的n-2个台阶有f(n-1)种跳法。
#所以当有n个台阶时，有f(n)=f(n-1)+f(n-2)种跳法。

class Solution:
    def jumpFloor(self, number):
        # write code here
        tempArray=[1,2]
        if number>=3:
            for i in range(3,number+1):
                tempArray[(i+1)%2]=tempArray[0]+tempArray[1]
        return tempArray[(number+1)%2]

s=Solution()
print(s.jumpFloor(2))