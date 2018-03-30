# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
#折半查找（Binary Search)技术，又称为二分查找。前提是顺序存储。时间复杂度为O(logn)，考虑到具有n个节点的完全二叉树的深度为logn +1
#在二分查找中，两个指针分别指向第一个元素和最后一个元素。
#本题的思路就是用二分查找法的思路寻找这个最小的元素。

class Solution:
    def  minNumberInRotateArray(self,rotateArray):
        if len(rotateArray)==0:
            return 0
        low=0
        high=len(rotateArray)-1
        mid=0
        while rotateArray[low]>=rotateArray[high]:#前面的数组大于等于后面的数组
            if high-low==1:
                mid=high
                break
            mid=(low+high)/2
             #考虑到三值相等的情况
            if rotateArray[low] == rotateArray[high] and rotateArray[low] == rotateArray[mid]:
                return self.MinInOrder(rotateArray, low, mid)
            if rotateArray[low]<=rotateArray[mid]:
                low=mid
            elif rotateArray[mid]<=rotateArray[high]:
                high=mid

        return rotateArray[mid]


    def MinInOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end+1]:
            if i < result:
                result = i
        return result
s=Solution()
print(s.minNumberInRotateArray([3,4,5,1,2]))


