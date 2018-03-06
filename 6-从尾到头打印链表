# -*- coding:utf-8 -*-
'''
输入一个链表，从尾到头打印链表每个节点的值。
'''
#思路：定义链表节点，
class ListNode:
    def __init__(self,x=None):#值初始化
        self.value=x
        self.next=None

class Solution:
    def PrintListFromTailToHead(self,ListNode):
        if ListNode.value==None:
            return #等价于return None
        l=[]
        head=ListNode
        while head:
            l.insert(0,head.value)#始终列表开头插入对象，这样先插入的对象就在后面，后插入的对象就在前面。
            head=head.next
        return l

node1=ListNode(11)
node2=ListNode(20)
node3=ListNode(34)
node1.next=node2
node2.next=node3


SingleNode=ListNode()
test=ListNode(33)
s=Solution()
print(s.PrintListFromTailToHead(node1))
print(s.PrintListFromTailToHead(SingleNode))
print(s.PrintListFromTailToHead(test))
