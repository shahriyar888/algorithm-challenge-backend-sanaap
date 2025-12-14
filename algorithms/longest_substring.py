from time import time


def longest_unique_substring_length(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == "__main__":
    t = time()
    print(longest_unique_substring_length("ABCABCFKAB"))# 5
    print(f"elapse {time() - t}")
