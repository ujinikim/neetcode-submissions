class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        score = 0
        for op in operations:
            if op == '+':
                score += st[-1] + st[-2]
                st.append(st[-1] + st[-2])
            elif op == 'D':
                score += st[-1] * 2
                st.append(st[-1] * 2)
            elif op == 'C':
                score -= st[-1]
                st.pop()
            else:
                score += int(op)
                st.append(int(op))
        return score
