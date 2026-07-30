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