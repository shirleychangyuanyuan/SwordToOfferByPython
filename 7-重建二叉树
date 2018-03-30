# -*- coding:utf-8 -*-
#前序遍历：根--左--右      第一个数字就是根节点的值
#中序遍历：左--根--右      在根节点的左边就是左子树的值，在右边就是右子树的值。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点,pre指的是前序遍历，tin是中序遍历
    def reConstructBinaryTree(self, pre, tin):
        #不写这一行，会报错list index out of range,可能出现了空列表,所以判断如果是空列表，返回None
        if not pre and not tin:
            return None
        #要考虑到只有一个元素的情况。
        if len(pre)==1:
            return TreeNode(pre[0])
        else:
        #根节点就是前序遍历的第一个值,定义一下根节点的值
            root=TreeNode(pre[0])
        #找一下根节点在中序遍历里的索引，
            i=tin.index(pre[0])
        #递归，左子树对应的前序和中序的序列
            root.left=self.reConstructBinaryTree(pre[1:i+1],tin[:i])
        #右子树对应的前序和中序的序列
            root.right=self.reConstructBinaryTree(pre[i+1:],tin[i+1:])

        return  root


pre = [1, 2, 4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

s = Solution()
newTree = s.reConstructBinaryTree(pre, tin)
