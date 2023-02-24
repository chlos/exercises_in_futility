from api import *

version_api = api(0)

def is_bad_version(v):
    return version_api.is_bad(v)

def first_bad_version(n):
# -- DO NOT CHANGE THIS SECTION
    version_api.n = n
# --
    api_calls_count = 0

    left, right = 1, n
    while left < right:
        mid = (left + right) // 2

        is_bad = is_bad_version(mid)
        api_calls_count += 1

        if is_bad:
            right = mid
        else:
            left = mid + 1


    return left, api_calls_count
