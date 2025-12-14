# نتایج حل مسئله طولانی‌ترین زیررشته بدون تکرار

## کدها

### 1️⃣ کد خودم
```python
def longest_unique_substring_length(s):
    max_length = 0
    for index, char in enumerate(s):
        sub = s[index +1 :]
        while char in sub:
            sub = sub[:len(sub) -1]
        max_length = max(max_length,len(sub)+1)
    return max_length
```
- درست است ولی کند (O(n²)) و حافظه زیاد مصرف می‌کند.

### 2️⃣ کد پیشنهادی با کمک AI
```python
def length_of_longest_substring(s: str) -> int:
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
```
- بهینه و سریع (O(n))، حافظه کم، و خوانایی بالا.

## دستاورد
- هر دو کد درست هستند.
- نسخه AI برای رشته‌های طولانی بهینه است.
- روش Sliding Window استاندارد و سریعتر است.

