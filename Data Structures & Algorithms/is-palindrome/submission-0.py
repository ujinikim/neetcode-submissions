class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter: keep only letters and numbers
        filtered_s = "".join(char.lower() for char in s if char.isalnum())
        
        # Check if it equals its reverse using slicing
        return filtered_s == filtered_s[::-1]