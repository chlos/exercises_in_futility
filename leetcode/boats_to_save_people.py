class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort by weight
        people.sort()
        print(people)

        boats_num = 0
        lightest_idx, heaviest_idx = 0, len(people) - 1
        while lightest_idx <= heaviest_idx:
            boats_num += 1
            if people[lightest_idx] + people[heaviest_idx] <= limit:
                # take 2 persons if limit is ok, otherwise take only heavy person
                lightest_idx += 1
            heaviest_idx -= 1

        return boats_num