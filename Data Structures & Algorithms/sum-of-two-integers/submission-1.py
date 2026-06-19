class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # Mask to get last 32 bits
        MASK = 0xFFFFFFFF
        
        while b != 0:
            # a ^ b handles addition without carry
            # (a & b) << 1 finds the carry
            # We apply & MASK to keep it within 32-bit bounds
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            
        # If a is within negative range, convert to Python's negative format
        return a if a <= MAX else ~(a ^ MASK)