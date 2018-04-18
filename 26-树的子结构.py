# -*- coding:utf-8 -*-
#输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
#第一步，先遍历树A找到与树B相同的根节点R，用递归的方法去遍历；
#第二步，判断树A中以R为根节点的子树是不是包含和树B一样的结构。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result=False
        if  pRoot1 !=None and  pRoot2 !=None:
            if pRoot1.val==pRoot2.val:#判断此时的结构是不是符合要求，不符合返回false.
                result=self.DoesTree1HaveTree2(pRoot1,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.right,pRoot2)
        return result

    def DoesTree1HaveTree2(self,pRoot1,pRoot2):
        if pRoot2==None:
            return True
        if pRoot1==None:
            return False
        if pRoot1.val!=pRoot2.val:
            return False
        return self.DoesTree1HaveTree2(pRoot1.left,pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right,pRoot2.right)

pRoot1=TreeNode(8)
pRoot2=TreeNode(8)
pRoot3=TreeNode(7)
pRoot4=TreeNode(9)
pRoot5=TreeNode(2)
pRoot6=TreeNode(4)
pRoot7=TreeNode(7)
pRoot1.left=pRoot2
pRoot1.right=pRoot3
pRoot2.left=pRoot4
pRoot2.right=pRoot5
pRoot5.left=pRoot6
pRoot5.right=pRoot7

pRoot8=TreeNode(8)
pRoot9=TreeNode(9)
pRoot10=TreeNode(2)
pRoot8.left=pRoot9
pRoot8.right=pRoot10

s=Solution()
print(s.HasSubtree(pRoot1,pRoot8))