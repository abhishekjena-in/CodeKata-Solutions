<div align="center">

# 🧩 Palindrome Check

[![Platform](https://img.shields.io/badge/GUVI-CodeKata-0284c7?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.guvi.in/code-kata/palindrome-check/)
[![Language](https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](#solution)
[![Status](https://img.shields.io/badge/Status-Passed-16a34a?style=for-the-badge&logo=githubactions&logoColor=white)](#)

</div>

---

### 📌 Problem Overview

* **Problem Name:** `Palindrome Check`
* **Platform:** GUVI CodeKata
* **Problem Link:** 🔗 [Open on CodeKata](https://www.guvi.in/code-kata/palindrome-check/)

---

### ⏱️ Submission Details

| Metric | Details |
| :--- | :--- |
| **Status** | ✅ Solved & Passed All Testcases |
| **Language** | `JAVA` |
| **Solved At** | `7/30/2026, 10:07:07 PM` |

---

### 💻 Solution

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int i = 0;
        int j = s.length()-1;
        boolean flag = true;
        while(i<j)
        {
            if(s.charAt(i) != s.charAt(j)){
                flag=false;
                break;
            }
            i++;
            j--;
            
        }
        if(flag) System.out.println("yes");
        else System.out.println("no");
        
    }
}
```

---

<div align="center">
<sub>Automated with ⚡ <b>CodeKata GitHub Sync</b></sub>
</div>
