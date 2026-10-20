class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l = 0
        st = ""
        ans = ""
        for i in s:
            if i == "(":
                l -= 1
                # st += i
            elif i == ")":
                l += 1
            st += i
            if l == 0:
                ans += st[1: -1]
                st = ''
        return ans