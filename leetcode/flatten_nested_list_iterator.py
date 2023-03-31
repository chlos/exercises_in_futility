# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# recursive dfs + flat list
class NestedIterator_recurDFSFlatList:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested_list = nestedList

        self.flat_list = []
        self.__getFlatList(self.nested_list)

        self.curr_pos = 0

    def __getFlatList(self, curr_nested_list):
        for item in curr_nested_list:
            if item.isInteger():
                self.flat_list.append(item.getInteger())
            else:
                self.__getFlatList(item.getList())

    def next(self) -> int:
        val = self.flat_list[self.curr_pos]
        self.curr_pos += 1

        return val

    def hasNext(self) -> bool:
        return self.curr_pos < len(self.flat_list)

# recursive dfs + generator
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._generator = self.__getFlatList(nestedList)
        self._peeked = None

    def __getFlatList(self, curr_nested_list):
        for item in curr_nested_list:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.__getFlatList(item.getList())

    def next(self) -> int:
        # Check there are integers left, and if so, then this will
        # also put one into self._peeked.
        if not self.hasNext():
            return None
        # Return the value of self._peeked, also clearing it.
        next_integer, self._peeked = self._peeked, None
        return next_integer

    def hasNext(self) -> bool:
        if self._peeked is not None:
            return True
        try: # Get another integer out of the generator.
            self._peeked = next(self._generator)
            return True
        except: # The generator is finished so raised StopIteration.
            return False

# iterative dfs + stack
class NestedIterator_StackIterDFS:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def __updStackToTopInt(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(
                reversed(self.stack.pop().getList())
            )

    def next(self) -> int:
        self.__updStackToTopInt()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self.__updStackToTopInt()
        return len(self.stack) > 0