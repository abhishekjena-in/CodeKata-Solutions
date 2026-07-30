# vowel-check-in-string

- **Solved At:** 7/30/2026, 9:50:04 PM
- **Language:** python
- **Status:** ✅ Solved & Verified on GUVI CodeKata

## Solution
```py
s = input()

vowels = "aeiouAEIOU"
found = False

for ch in s:
    if ch in vowels:
        found = True
        break

if found:
    print("yes")
else:
    print("no")
```
