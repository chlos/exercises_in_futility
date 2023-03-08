"""
Реализовать функцию fuzzysearch как в редакторе sublime text 3 .
Для незнакомых с редактором и/или термином fuzzysearch (нечёткий поиск), можно упомянуть более формальное название — 
approximate string matching (нахождение приблизительного соответствия строк). 
По факту требуется проверить, является ли первая строка подпоследовательностью второй.

fuzzysearch('car', 'cartwheel');        // true
fuzzysearch('cwhl', 'cartwheel');       // true
fuzzysearch('cwhee', 'cartwheel');     // true
fuzzysearch('cartwheel', 'cartwheel');  // true
fuzzysearch('cwheeel', 'cartwheel');    // false
fuzzysearch('lw', 'cartwheel');         // false
"""

#('cl', 'cel')
#   ^      ^

def is_substring(pattern, text):
    if not pattern:
        return True

    p_idx = 0
    t_idx = 0
    while t_idx < len(text):
        if pattern[p_idx] == text[t_idx]:
            p_idx += 1
            t_idx += 1
        else:
            t_idx += 1

        if p_idx == len(pattern):
            return True

    return False





"""
Дан текст T и строка P. Требуется найти подстроку P' в T такую, 
что она совпадает с P с точностью до перестановки букв.

В качестве ответа стоит вернуть индекс первого вхождения,
 или -1, если такая подстрока P' не нашлась.

P       T
 'abc', 'bca' >> 0
 'abc', 'qqbcarabc'  >> 2
 'abc', 'qqbarab' >> -1
 'abc', 'qcqbarab' >> -1
"""

import collections
import copy


def get_first_substring_idx(pattern, text):
    if not pattern:
        return 0
    if not text:
        return -1

    pattern_counter_init = collections.Counter(pattern)
    pattern_count = copy.copy(pattern_counter_init)

    t_start_idx, t_end_idx = 0, 0
    while t_end_idx < len(text):
        curr_ch = text[t_end_idx]
        if curr_ch in pattern_count:
            pattern_count[curr_ch] -= 1
            if pattern_count[curr_ch] == 0:
                del pattern_count[curr_ch]
            t_end_idx += 1
        else:
            pattern_count = copy.copy(pattern_counter_init)
            t_start_idx, t_end_idx = t_end_idx + 1, t_end_idx + 1

        if not pattern_count:
            return t_start_idx

    return -1