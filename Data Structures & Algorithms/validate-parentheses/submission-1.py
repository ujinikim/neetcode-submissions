class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pair = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch not in pair.keys():
                st.append(ch)
            else:
                if not len(st):
                    return False
                
                if pair[ch] != st[-1]:
                    return False
                else:
                    st.pop()

        
        return False if len(st) else True