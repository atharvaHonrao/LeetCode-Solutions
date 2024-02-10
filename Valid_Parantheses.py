class Solution(object):
    def isValid(self, s):
        if s[0]==")" or s[0]=="]" or s[0]=="}":
            return False
        arr = []
        index = -1
        for i in s:
            if i=="(":
                arr.append(")")
                index+=1
            elif i=="[":
                arr.append("]")
                index+=1
            elif i=="{":
                arr.append("}")
                index+=1
            else:
                if index<0:
                    return False
                if arr[index] == i:
                    arr.pop()
                    index-=1
                else:
                    return False
        if arr == []:
            return True
