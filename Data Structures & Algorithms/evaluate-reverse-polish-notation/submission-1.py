class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        experssions = deque()
        ops = {'+', '-', '*', '/'}
        for i in range(len(tokens)):
            ch = tokens[i]
            if ch in ops:
                r = int(experssions.pop())
                l = int(experssions.pop())
                res = 0
                if ch == '+':
                    res = l + r
                elif ch == '-':
                    res = l - r
                elif ch == '*':
                    res = l * r
                else:
                    res = int(l / r)
                experssions.append(res)
            else:
                experssions.append(int(ch))

        return experssions[0]