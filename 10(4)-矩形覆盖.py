# -*- coding:utf-8 -*-
#我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#将2*n的覆盖方法记为f(n)。
#用第一个2*1的矩形去覆盖大矩形的最左边时有两种选择：横着放和竖着放。
#横着放的时候，左下角必须横着放2*1小矩形，右边还剩下2*(n-2)的区域，有f(n-2)种覆盖方法；
#竖着放的时候，右边还剩下2*(n-1)的区域，有f(n-1)种覆盖方法。
#所以f(n)=f(n-1)+f(n-2)
class Solution:
    def rectCover(self, number):
        # write code here
        #考虑矩形不存在的情况
        if number==0:
            return 0
        tempArray=[1,2]
        if number>=3:
            for i in range(3,number+1):
                tempArray[(i+1)%2]=tempArray[0]+tempArray[1]
        return tempArray[(number+1)%2]