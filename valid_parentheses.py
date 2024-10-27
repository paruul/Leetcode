class Solution(object):
    def isValid(self, s):
        """
        Time complexity: O(n)
        Space complexity: O(n) in the worst case, when it 
        keeps accumulating unmatched brackets
        Logic: First create a dictionary with closing brackets as key 
        -> check if the element is clsoing or opening bracket ->
        if its a closing bracket pop the top element from stack.
        If its empty it will be # -> Check if the top element of 
        stack is same as the opening bracket for the given closing 
        bracket using the dictionary. -> if not return False else 
        append the char in the stack -> In the end return True 
        if the stack is empty (because empty stack means all 
        the brackets were matched) 
        else retunr False   

        """
        bracket_pairs = {")": "(", '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in bracket_pairs:  # If it's a closing bracket
                top_element = stack.pop() if stack else "#"
                if bracket_pairs[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack




        