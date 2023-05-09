import collections


class Solution:
    # topological sort; Kahn's algorithm; BFS
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # init incoming degrees counter
        # in some reason N could be > than len(all_courses_set) !!!???
        # so we need to init [1...N] courses
        in_degrees = {}
        for course in range(1, n + 1):
            in_degrees[course] = 0

        # build graph; count incoming degrees
        graph = collections.defaultdict(list)
        for parent_node, child_node in relations:
            graph[parent_node].append(child_node)
            in_degrees[child_node] += 1

        # build sources (nodes with 0 incoming degrees) queue
        sources = collections.deque()
        for node in in_degrees:
            if in_degrees[node] == 0:
                sources.append(node)

        # check if it's possible to finish courses at all
        curr_semester_courses_num = len(sources)
        if curr_semester_courses_num <= 0:
            return -1

        # topological sort, using only courses with finished pre-reqs (aka sources)
        num_semesters = 1
        courses_taken = []
        while sources:
            # we finished all courses available for the curr semester; start a new one
            if curr_semester_courses_num <= 0:
                num_semesters += 1
                curr_semester_courses_num = len(sources)

            # take this course to the current semester
            node = sources.popleft()
            curr_semester_courses_num -= 1
            courses_taken.append(node)
            # add courses ready for the current of upcoming semesters
            for child_node in graph[node]:
                in_degrees[child_node] -= 1
                if in_degrees[child_node] == 0:
                    sources.append(child_node)

        # check if there are unreachable courses
        if len(courses_taken) != n:
            return -1

        return num_semesters
