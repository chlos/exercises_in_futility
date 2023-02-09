# aka symmetry axis / symmetry line

# fyi:
# https://leetcode.com/problems/line-reflection/solutions/202760/bad-problem-description-come-and-read-what-it-really-means/
# https://leetcode.com/problems/line-reflection/solutions/3137429/python-o-n-solution-using-dict/
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True

        # count all points
        points_count = collections.defaultdict(int)
        # leftmost/rightmost points
        min_x, max_x = float('inf'), -float('inf')
        for x, y in points:
            # increment it if you'd like to count same coord points as different onesc
            points_count[(x, y)] = 1
            min_x = min(min_x, x)
            max_x = max(max_x, x)

        # symmetry line
        mid_x = (min_x + max_x) / 2

        # check if points have their mirror points
        for x, y in points:
            # mid - x + mid = 2*mid - x
            mirror_x = 2 * mid_x - x
            mirror_count = points_count.get((mirror_x, y))

            if mirror_count is not None:
                if mirror_count > 1:
                    points_count[(mirror_x, y)] -= 1
                else:
                    del points_count[mirror_x, y]

        # if hashmap is empty, all points have proper mirror points
        return not points_count