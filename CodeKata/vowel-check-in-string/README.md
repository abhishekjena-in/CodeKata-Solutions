<div align="center">

# 🧩 Vowel Check In String

[![Platform](https://img.shields.io/badge/GUVI-CodeKata-0284c7?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.guvi.in/code-kata/vowel-check-in-string/)
[![Language](https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](#solution)
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
| **Language** | `JAVA` |
| **Solved At** | `7/30/2026, 10:07:28 PM` |

---

### 💻 Solution

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        boolean flag = false;
        for(int i=0; i<s.length(); i++)
        {
            char ch = Character.toLowerCase(s.charAt(i));
            switch(ch){
                case 'a':
                    flag = true;
                    break;
                case 'b':
                    flag = true;
                    break;
                case 'i':
                    flag = true;
                    break;
                case 'o':
                    flag = true;
                    break;
                case 'u':
                    flag = true;
                    break;
                default:
                    continue;
            }
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
