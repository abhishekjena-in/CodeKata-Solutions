chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "SYNC_TO_GITHUB") {
    processSync(request.payload)
      .then(() => sendResponse({ status: "SUCCESS" }))
      .catch((err) => {
        console.error("❌ GitHub Sync Error:", err);
        sendResponse({ status: "ERROR", message: err.message });
      });
    return true;
  }
});

async function processSync(data) {
  const config = await chrome.storage.local.get(["github_user", "github_repo", "github_token"]);

  if (!config.github_token || !config.github_user || !config.github_repo) {
    console.error("⚠️ Credentials missing in Extension settings popup.");
    return;
  }

  // Format problem slug (e.g., "vowel-check-in-string")
  const cleanTitle = data.title
    .replace(/^\d+[\.\s-]*/, "")
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/[\s_]+/g, "-");

  const ext = getExtension(data.language);

  // Exact target repository paths
  const solutionFilePath = `CodeKata/${cleanTitle}/solution.${ext}`;
  const readmeFilePath   = `CodeKata/${cleanTitle}/README.md`;

  // Build CodeKata Problem URL
  const problemUrl = `https://www.guvi.in/code-kata/${cleanTitle}/`;

  // Safe Base64 Encoding
  const safeBase64Code = utf8ToBase64(data.code);

  // Generate Stunning README Markdown Template
  const readmeMarkdown = buildStunningReadme({
    slug: cleanTitle,
    title: formatTitle(cleanTitle),
    language: data.language,
    ext: ext,
    code: data.code,
    timestamp: new Date(data.timestamp).toLocaleString(),
    problemUrl: problemUrl
  });

  const safeBase64Readme = utf8ToBase64(readmeMarkdown);

  await commitFileToGitHub(config, solutionFilePath, safeBase64Code, `Add solution for ${cleanTitle}`);
  await commitFileToGitHub(config, readmeFilePath, safeBase64Readme, `Add README journal for ${cleanTitle}`);

  console.log(`🎉 Successfully pushed to CodeKata/${cleanTitle}/`);
}

// Generates modern, polished README Markdown
function buildStunningReadme({ slug, title, language, ext, code, timestamp, problemUrl }) {
  const langBadge = language.toLowerCase().includes("py") ? "Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" :
                    language.toLowerCase().includes("java") ? "Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" :
                    language.toLowerCase().includes("cpp") ? "C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" :
                    "Code-000000?style=for-the-badge&logo=github&logoColor=white";

  return `<div align="center">

# 🧩 ${title}

[![Platform](https://img.shields.io/badge/GUVI-CodeKata-0284c7?style=for-the-badge&logo=codeforces&logoColor=white)](${problemUrl})
[![Language](https://img.shields.io/badge/Language-${langBadge})](#solution)
[![Status](https://img.shields.io/badge/Status-Passed-16a34a?style=for-the-badge&logo=githubactions&logoColor=white)](#)

</div>

---

### 📌 Problem Overview

* **Problem Name:** \`${title}\`
* **Platform:** GUVI CodeKata
* **Problem Link:** 🔗 [Open on CodeKata](${problemUrl})

---

### ⏱️ Submission Details

| Metric | Details |
| :--- | :--- |
| **Status** | ✅ Solved & Passed All Testcases |
| **Language** | \`${language.toUpperCase()}\` |
| **Solved At** | \`${timestamp}\` |

---

### 💻 Solution

\`\`\`${ext}
${code}
\`\`\`

---

<div align="center">
<sub>Automated with ⚡ <b>CodeKata GitHub Sync</b></sub>
</div>
`;
}

// Converts "vowel-check-in-string" -> "Vowel Check In String"
function formatTitle(slug) {
  return slug
    .split("-")
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

async function commitFileToGitHub(config, path, base64Content, commitMessage) {
  const url = `https://api.github.com/repos/${config.github_user}/${config.github_repo}/contents/${path}`;

  let sha = null;
  try {
    const checkRes = await fetch(url, {
      headers: { "Authorization": `token ${config.github_token}` }
    });
    if (checkRes.ok) {
      const fileData = await checkRes.json();
      sha = fileData.sha;
    }
  } catch (e) {}

  const payload = {
    message: commitMessage,
    content: base64Content,
    ...(sha && { sha })
  };

  const response = await fetch(url, {
    method: "PUT",
    headers: {
      "Authorization": `token ${config.github_token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(`GitHub API Error (${response.status}): ${errorData.message}`);
  }
}

function utf8ToBase64(str) {
  return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, (match, p1) => {
    return String.fromCharCode("0x" + p1);
  }));
}

function getExtension(language) {
  const lang = language.toLowerCase();
  if (lang.includes("py") || lang.includes("python")) return "py";
  if (lang.includes("java") && !lang.includes("script")) return "java";
  if (lang.includes("cpp") || lang.includes("c++")) return "cpp";
  if (lang.includes("c") && !lang.includes("script")) return "c";
  if (lang.includes("js") || lang.includes("javascript")) return "js";
  return "txt";
}