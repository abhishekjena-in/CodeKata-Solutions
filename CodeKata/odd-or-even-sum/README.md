<div align="center">

# 🧩 Odd Or Even Sum

[![Platform](https://img.shields.io/badge/GUVI-CodeKata-0284c7?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.guvi.in/code-kata/odd-or-even-sum/)
[![Language](https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](#solution)
[![Status](https://img.shields.io/badge/Status-Passed-16a34a?style=for-the-badge&logo=githubactions&logoColor=white)](#)

</div>

---

### 📌 Problem Overview

* **Problem Name:** `Odd Or Even Sum`
* **Platform:** GUVI CodeKata
* **Problem Link:** 🔗 [Open on CodeKata](https://www.guvi.in/code-kata/odd-or-even-sum/)

---

### ⏱️ Submission Details

| Metric | Details |
| :--- | :--- |
| **Status** | ✅ Solved & Passed All Testcases |
| **Language** | `JAVA` |
| **Solved At** | `7/30/2026, 10:05:38 PM` |

---

### 💻 Solution

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        if( (N%2 == 0 && M%2 == 0) || (N%2 != 0 && M%2 != 0) ) System.out.println("even");
        else System.out.println("odd");
    }
}
```

---

<div align="center">
<sub>Automated with ⚡ <b>CodeKata GitHub Sync</b></sub>
</div>
