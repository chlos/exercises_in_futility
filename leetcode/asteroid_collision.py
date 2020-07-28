#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] > -asteroid:
                    break
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break
                elif stack[-1] < -asteroid:
                    stack.pop()
                    continue
            else:
                stack.append(asteroid)

        return stack


if __name__ == "__main__":
    s = Solution()

    asteroids = [5, 10, -5]
    expected = [5, 10]
    result = s.asteroidCollision(asteroids)
    print('res: {}\nexp: {}'.format(result, expected))
    assert result == expected
    print('OK')