class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        n = len(s)
        # Try every possible target character
        for target in set(s):
            left = 0
            count = 0  # Number of replacements used
            for right in range(n):
                if s[right] != target:
                    count += 1
                # If replacements exceed k, move left pointer
                while count > k:
                    if s[left] != target:
                        count -= 1
                    left += 1
                # Update max_len for this target character
                max_len = max(max_len, right - left + 1)
        return max_len      