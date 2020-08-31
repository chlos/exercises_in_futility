#!/usr/bin/env python3

from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0

        chars_counter = Counter(chars)
        for word in words:
            word_is_good = True
            word_counter = Counter(word)
            for word_ch, word_ch_count in word_counter.items():
                if word_ch_count > chars_counter.get(word_ch, 0):
                    word_is_good = False
                    break
            if word_is_good:
                count += len(word)

        return count


if __name__ == "__main__":
    s = Solution()

    # The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
    assert s.countCharacters(['cat', 'bt', 'hat', 'tree'], 'atach') == 6

    # The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
    assert s.countCharacters(['hello', 'world', 'leetcode'], 'welldonehoneyr') == 10

    assert s.countCharacters(
        [
            "dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
            "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb",
            "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
            "boygirdlggnh",
            "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
            "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
            "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
            "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
            "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
            "oxgaskztzroxuntiwlfyufddl",
            "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
            "qnagrpfzlyrouolqquytwnwnsqnmuzphne",
            "eeilfdaookieawrrbvtnqfzcricvhpiv",
            "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
            "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
            "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
            "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo",
            "teyygdmmyadppuopvqdodaczob",
            "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
            "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"
        ],
        'usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp'
    ) == 0

    print('OK')