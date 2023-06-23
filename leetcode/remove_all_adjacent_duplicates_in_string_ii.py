from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    ch: str
    count: int


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack: List[Item] = []
        for ch in s:
            if stack and ch == stack[-1].ch:
                if stack[-1].count + 1 == k:
                    # remove k-1 dups from stack (and skip the curr ch)
                    # so k dups will be removed in total
                    for _ in range(k - 1):
                        stack.pop()
                    continue
                else:
                    stack.append(Item(ch, stack[-1].count + 1))
                    continue

            stack.append(Item(ch, 1))

        return "".join((item.ch for item in stack))
