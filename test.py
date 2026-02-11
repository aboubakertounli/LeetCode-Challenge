class Solution:
    def isValid(self, s: str) -> bool:
        D={')':'(',']':'[','}':'{'}
        d=list(D.items())
        stack=[]
        for i in s:
            if i==d[0][1] or i==d[1][1] or i==d[2][1]:
                stack.append(i)
            elif stack and stack[-1]==D[i] :
                stack.pop()
            else:
                return False #  means the string is not valid because it has a closing bracket without a corresponding opening bracket or the brackets are not in the correct order
        if not stack : # means the list stack is empty
            return True
 # means the list stack is not empty , is it neccessary ? response : Yes, it is necessary to check if the stack is empty at the end of the function. If the stack is not empty, it means that there are unmatched opening brackets that were not closed properly, which would make the string invalid. Therefore, returning False in this case is important to ensure that the function correctly identifies invalid strings.
object=Solution()

print(object.isValid("(")) 
print(object.isValid("([)]")) #false
print(object.isValid("{[]}")) #true
print(object.isValid("()")) #true
print(object.isValid("()[]{}")) #true
print(object.isValid("((()))")) #true
print(object.isValid("((())")) #false
print(object.isValid("((())]")) #false
