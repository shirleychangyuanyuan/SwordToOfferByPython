# -*- coding:utf-8 -*-
#操作先进后出的栈实现一个先进先出的队列
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # 往栈一压入元素
        self.stack1.append(node)

    def pop(self):
        if len(self.stack1)==0 and len(self.stack2)==0:
            return
        #如果栈二为空，把栈一的元素逐个弹出并压入栈二
        elif len(self.stack2)==0:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())