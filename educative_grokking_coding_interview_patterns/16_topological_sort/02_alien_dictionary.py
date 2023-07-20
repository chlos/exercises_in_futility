import collections


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # adjacency list
        adj_list = collections.defaultdict(set)
        # count up how many incoming edges each letter has
        in_count = dict.fromkeys((ch for w in words for ch in w), 0)

        # build adjacency list + incoming edges list
        for word_i in range(len(words) - 1):
            word_1, word_2 = words[word_i], words[word_i + 1]
            for ch_1, ch_2 in zip(word_1, word_2):
                if ch_1 != ch_2:
                    if not ch_2 in adj_list[ch_1]:
                        # ch_1 < ch_2
                        adj_list[ch_1].add(ch_2)
                        in_count[ch_2] += 1
                    break
            else:
                # abcd -> ab: These cases will never result in a valid alphabet
                # (because in a valid alphabet, prefixes are always first)
                if len(word_1) > len(word_2):
                    return ''

        # BFS
        result = []
        queue = collections.deque(ch for ch, count in in_count.items() if count == 0)
        while queue:
            ch = queue.popleft()
            result.append(ch)
            for adj_ch in adj_list[ch]:
                in_count[adj_ch] -= 1
                if in_count[adj_ch] == 0:
                    queue.append(adj_ch)

        # not all chars in the result => 
        if len(result) < len(in_count):
            return ''
        return ''.join(result)