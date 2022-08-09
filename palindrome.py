class Solution(object):
    def isPalindrome(self,x):
        if  list(str(x))[::-1]  ==  list(str(x)):
            return True
        else :
            return False
