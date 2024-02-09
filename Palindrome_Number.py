class Solution(object):
    def isPalindrome(self, x):
        y = 0
        ans = x
        while x > 0:
            y = y*10 + (x%10)
            x = (x - (x%10))/10

        return y==ans
