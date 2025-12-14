from time import time


def longest_unique_substring_length(s):
    max_length = 0
    for index, char in enumerate(s):
        sub = s[index +1 :]
        while char in sub:
            sub = sub[:len(sub) -1]
        max_length = max(max_length,len(sub)+1)



    return max_length


if __name__ == "__main__":
    t = time()
    print(longest_unique_substring_length("ABCABCFKAB"))# 5
    print(f"elapse {time() - t}")
