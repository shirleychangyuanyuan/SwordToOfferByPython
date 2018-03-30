# -*- coding:utf-8 -*-
# array=[[1,2,3],[4,5,6],[7,8,9],[9,10,12]]
# rownum=len(array)
# colnum=len(array[0])
# print(rownum)
# print(colnum)


#思路：这是一个查找过程：首先选取数组中右上角的数字，如果该数字大于要查找的数字，则剔除该数字所在的列；
# 如果该数字小于要查找的数字，则剔除该数字所在的行。
class Solution:
    def Find(self,array,target):
        rownum=len(array)#计算行数
        colnum=len(array[0])#计算列数

        i=0
        j=colnum-1
        while i<rownum and  j>=0:#注意这儿用的是逻辑运算and而不是位运算&
            if array[i][j] > target:
                j-=1#剔除列，也就是列数减一
            elif array[i][j] <target:
                i+=1 #剔除行，也就是行数加一
            else:
                return True
        return False

    def SearchTargetNum(self,matrix,target):#若存在target，计算target的个数
        rows=len(matrix)
        cols=len(matrix[0])

        row=0
        col=cols-1

        count=0
        while row<rows and col>=0:
            if matrix[row][col] >target:
                col-=1
            elif matrix[row][col] <target:
                row+=1
            else:
                count+=1
                col-=1
        return count






array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
findtarget=Solution()#创建一个实例
print(findtarget.Find(array,9))
print(findtarget.SearchTargetNum(array,9))
