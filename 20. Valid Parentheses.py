class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                my_stack.append(i)
            else:
                if len(my_stack) == 0:
                    return False
                elif i == ")":
                    if my_stack[-1] == "(":
                        my_stack.pop()
                    else:
                        return False
                elif i == "]":
                    if my_stack[-1] == "[":
                        my_stack.pop()
                    else:
                        return False
                elif i == "}":
                    if my_stack[-1] == "{":
                        my_stack.pop()
                    else:
                        return False
        if len(my_stack) == 0:
            return True
        else:
            return False
