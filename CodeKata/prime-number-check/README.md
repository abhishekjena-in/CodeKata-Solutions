<div align="center">

# 🧩 Prime Number Check

[![Platform](https://img.shields.io/badge/GUVI-CodeKata-0284c7?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.guvi.in/code-kata/prime-number-check/)
[![Language](https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](#solution)
[![Status](https://img.shields.io/badge/Status-Passed-16a34a?style=for-the-badge&logo=githubactions&logoColor=white)](#)

</div>

---

### 📌 Problem Overview

* **Problem Name:** `Prime Number Check`
* **Platform:** GUVI CodeKata
* **Problem Link:** 🔗 [Open on CodeKata](https://www.guvi.in/code-kata/prime-number-check/)

---

### ⏱️ Submission Details

| Metric | Details |
| :--- | :--- |
| **Status** | ✅ Solved & Passed All Testcases |
| **Language** | `JAVA` |
| **Solved At** | `7/30/2026, 10:05:59 PM` |

---

### 💻 Solution

```java
import java.util.Scanner;
public class Main {
    public boolean checkPrime(int num){
        if(num<=1) return false;
        
        for(int i=2; i*i<=num; i++)
        {
            if(num % i ==0) return false;
        }
        
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        Main obj = new Main();
        boolean res = obj.checkPrime(num);
        if(res) System.out.println("yes");
        else System.out.println("no");
    }
}
```

---

<div align="center">
<sub>Automated with ⚡ <b>CodeKata GitHub Sync</b></sub>
</div>
