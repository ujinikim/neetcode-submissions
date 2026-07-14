class Solution:
    def isHappy(self, n: int) -> bool:
        memory = set()
        pre = n
        while True:
            total = sum(int(x) ** 2 for x in str(pre))
            if total == 1:
                return True
            print(total)
            if total in memory:
                return False
            memory.add(total)

            pre = total
            

