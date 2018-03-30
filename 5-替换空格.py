# -*- coding:utf-8 -*-
'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''



# S="We are happy."
# L=list(S)
# print(L)

class Solution:#从字符串到列表再到字符串的过程
    def replaceSpace(self,s):
        stringlist=list(s)#把源字符串打散成一个列表
        stringReplace=[]#设置一个空列表，用append方法原地添加
        for item in stringlist:#列表解析
            if item ==' ':#注意引号里要空一格
                stringReplace.append('%20')
            else:
                stringReplace.append(item)
        return "".join(stringReplace)#把列表合成一个字符串

s=" Wearehappy."
replace=Solution()
print(replace.replaceSpace(s))
