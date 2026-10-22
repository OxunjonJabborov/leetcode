class Solution:
    def isValid(self, s: str) -> bool:
        char = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                char.append(i)
            else:
                if not char:
                    return False
                if (i == ')' and char[-1] != '(') or (i == ']' and char[-1] != '[') or (i == '}' and char[-1] != '{'):
                    return False
                else:
                    char.pop()
        return len(char) == 0