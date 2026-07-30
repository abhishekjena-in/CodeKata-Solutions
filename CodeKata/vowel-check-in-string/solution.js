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