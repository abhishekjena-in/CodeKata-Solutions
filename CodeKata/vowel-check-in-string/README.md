<div align="center">

# 🧩 Vowel Check In String

[![Platform](https://img.shields.io/badge/GUVI-CodeKata-0284c7?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.guvi.in/code-kata/vowel-check-in-string/)
[![Language](https://img.shields.io/badge/Language-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](#solution)
[![Status](https://img.shields.io/badge/Status-Passed-16a34a?style=for-the-badge&logo=githubactions&logoColor=white)](#)

</div>

---

### 📌 Problem Overview

* **Problem Name:** `Vowel Check In String`
* **Platform:** GUVI CodeKata
* **Problem Link:** 🔗 [Open on CodeKata](https://www.guvi.in/code-kata/vowel-check-in-string/)

---

### ⏱️ Submission Details

| Metric | Details |
| :--- | :--- |
| **Status** | ✅ Solved & Passed All Testcases |
| **Language** | `PYTHON` |
| **Solved At** | `7/30/2026, 9:52:52 PM` |

---

### 💻 Solution

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

---

<div align="center">
<sub>Automated with ⚡ <b>CodeKata GitHub Sync</b></sub>
</div>
