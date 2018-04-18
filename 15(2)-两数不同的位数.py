# -*- coding:utf-8 -*-
#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
#把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0.
#判断是不是2的整数次方。若是，只有有一个1，其余皆为0.所以只要判断经过一次减一再与自己的与远算之后是不是为0.
#判断两数不同的位数，只需要先异或，不同的则为真“1”,再统计1的个数。
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
    def NumberOf3(self, m,n):
        # write code here
        diff=m^n
        count=0
        while diff:
            count+=1
            diff=(diff-1)&diff
        return count

s=Solution()
print(s.NumberOf3(10,13))