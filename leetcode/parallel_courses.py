import collections


class Solution:
    # topological sort; Kahn's algorithm; BFS
    def minimumSemesters_topoSort(self, n: int, relations: List[List[int]]) -> int:
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

    # dfs; cycle detection; path length calculation
    def minimumSemesters_dfs(self, n: int, relations: List[List[int]]) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for parent_node, child_node in relations:
            graph[parent_node].append(child_node)

        # check cycles - naive, timeout
        # visited = [False] * (n + 1)
        # def has_cycle_dfs(node):
        #     if visited[node]:
        #         return True
        #     visited[node] = True
        #     for child_node in graph[node]:
        #         if has_cycle_dfs(child_node):
        #             return True
        #     visited[node] = False
        #     return False

        visited = {}
        IN_PROGRESS, VISITED = 1, 0

        def has_cycle_dfs(node: int):
            # return True if graph has a cycle
            if node in visited:
                return visited[node]
            else:
                # mark as visiting
                visited[node] = IN_PROGRESS
            for child_node in graph[node]:
                if has_cycle_dfs(child_node):
                    # we meet a cycle!
                    return True
            # mark as visited
            visited[node] = VISITED
            return False

        for node in range(1, n + 1):
            if has_cycle_dfs(node):
                return -1

        # calculate the longest path
        visited_len = {}

        def calc_path_len_dfs(node):
            if node in visited_len:
                return visited_len[node]

            max_len = 1
            for child_node in graph[node]:
                max_len = max(max_len, calc_path_len_dfs(child_node) + 1)
            visited_len[node] = max_len

            return max_len

        num_semesters = 0
        for node in range(1, n + 1):
            num_semesters = max(num_semesters, calc_path_len_dfs(node))

        return num_semesters

    # dfs; cycle detection; path length calculation -- shorter
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for parent_node, child_node in relations:
            graph[parent_node].append(child_node)

        # calculate max path len; detect cycles
        visited = {}  # node: max_path_len

        def has_cycle_dfs(node: int):
            # return path len or -1 if graph has a cycle
            if node in visited:
                return visited[node]
            else:
                # mark as visiting with a negative len
                visited[node] = -1

            max_len = 1
            for child_node in graph[node]:
                curr_len = has_cycle_dfs(child_node)
                if curr_len == -1:
                    # we meet a cycle!
                    return -1
                max_len = max(max_len, curr_len + 1)
            # mark as visited
            visited[node] = max_len

            return max_len

        max_len = -1
        for node in range(1, n + 1):
            curr_len = has_cycle_dfs(node)
            if curr_len == -1:
                return -1
            max_len = max(max_len, curr_len)

        return max_len
