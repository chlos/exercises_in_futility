import collections


class Solution:
    # count frequencies for chars in the sliding window
    def lengthOfLongestSubstring_freq(self, s: str) -> int:
        result = 0
        chars_count = collections.defaultdict(int)

        left = 0
        for right in range(len(s)):
            chars_count[s[right]] += 1

            # repeating char; shrink the window from the left side
            while chars_count[s[right]] > 1:
                chars_count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result

    # track chars indexes
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        chars_index = {}

        left = 0
        for right in range(len(s)):
            # we've seen this char already at index chars_index[char]
            # so shrink the window to the chars_index[char]+1
            if s[right] in chars_index:
                left = max(left, chars_index[s[right]] + 1)
            # update char's last met index
            chars_index[s[right]] = right

            result = max(result, right - left + 1)

        return result