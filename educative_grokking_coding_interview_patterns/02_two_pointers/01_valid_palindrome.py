def is_palindrome(s):
  left, right = 0, len(s) - 1
  while left < len(s) / 2:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1

  return True