class Solution:
    def countSubstrings(self, s: str) -> int:
        m_s = "*" + "".join(c + "*" for c in s)

        radii = [0] * len(m_s)

        center = 0
        right = 0

        for i in range(len(m_s)):

            # 1. Reuse mirror information if i is inside
            #    our currently known palindrome
            if i < right:
                mirror = 2 * center - i

                radii[i] = min(
                    radii[mirror],
                    right - i
                )

            # 2. Expand from where our known radius ends
            l = i - radii[i] - 1
            r = i + radii[i] + 1

            while (
                l >= 0
                and r < len(m_s)
                and m_s[l] == m_s[r]
            ):
                radii[i] += 1
                l -= 1
                r += 1

            # 3. Did this palindrome extend farther right?
            if i + radii[i] > right:
                center = i
                right = i + radii[i]

        # Convert transformed-string radii into
        # number of actual palindromic substrings
        return sum((radius + 1) // 2 for radius in radii)