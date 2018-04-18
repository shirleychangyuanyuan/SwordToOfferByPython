# -*- coding:utf-8 -*-
#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
#把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0.
#判断是不是2的整数次方。若是，只有有一个1，其余皆为0.所以只要判断经过一次减一再与自己的与远算之后是不是为0.
class Solution:
    def NumberOf2(self, n):
        # write code here
        count=0
        if n<0:
            return False
        if (n-1)&n==0:
            return True
        else:
            return False

s=Solution()
print(s.NumberOf2(3))