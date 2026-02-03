# palindrome number
# using converted int to str ( same for words or letters)

# class Solution(object):
#    def isPalindrome(self, x):
        
#        x_str=str(x)
        
#        rev=""
#        for ch in x_str:
#            rev = ch + rev
                
#        if x_str == rev:
#            return True 
        
#        else:
#           return False


# using the number reverse method 

class Solution:
    def isPalindrome_num(self, x):
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10            
            reversed_num = reversed_num * 10 + digit
            x = x // 10             
        
        return original == reversed_num



if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome_num(121)) 

