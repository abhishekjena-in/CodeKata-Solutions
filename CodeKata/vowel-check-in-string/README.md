# vowel-check-in-string

- **Solved At:** 7/30/2026, 9:48:48 PM
- **Language:** javascript
- **Status:** ✅ Solved & Verified on GUVI CodeKata

## Solution
```js
let s = prompt();

let vowels = "aeiouAEIOU";
let found = false;

for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i])) {
        found = true;
        break;
    }
}

if (found)
    console.log("yes");
else
    console.log("no");
```
