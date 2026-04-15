# 🚀 AI-Powered PR Review Agent

An automated **AI-based Pull Request Reviewer** that analyzes code changes and provides intelligent feedback directly on GitHub PRs — along with sending **beautiful email reports to your team**.

---

## 🧠 Overview

This project integrates **GitHub Actions + OpenRouter (LLM) + Email Notifications** to create a fully automated code review system.

Whenever a Pull Request is created or updated, the system:

1. 📥 Fetches the PR diff
2. 🤖 Sends it to an AI model
3. 🧠 Generates a structured review
4. 💬 Posts a comment on the PR
5. 📧 Sends a styled email to the team

---

## ⚙️ Architecture

```
Pull Request Created
        ↓
GitHub Actions Trigger
        ↓
Python Script Execution
        ↓
Fetch PR Diff (GitHub API)
        ↓
Send to OpenRouter AI
        ↓
Generate Review
        ↓
Post Comment on PR
        ↓
Send Styled Email to Team
```

---

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ai-review.yml       # GitHub Actions workflow
│
├── scripts/
│   ├── review_agent.py        # Main controller
│   ├── github_utils.py        # GitHub API helpers
│   ├── prompt.py              # AI prompt template
│   └── email_utils.py         # Email sender (SMTP)
│
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🚀 Features

* ✅ Automatic PR review on every pull request
* 🤖 AI-powered code analysis using OpenRouter
* 💬 Auto-comment on PR with feedback
* 📧 Styled HTML email notifications
* 🔐 Secure secret handling via GitHub Secrets
* ⚡ Fully serverless (runs on GitHub Actions)

---

## 🧰 Tech Stack

* 🐍 Python
* ⚙️ GitHub Actions
* 🌐 OpenRouter API (LLM)
* 📧 Gmail SMTP
* 🔗 GitHub REST API

---

## 🔧 Setup Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/PR-Review-Agent.git
cd PR-Review-Agent
```

---

### 2️⃣ Add GitHub Secrets

Go to:

**GitHub → Settings → Secrets → Actions**

Add the following:

| Secret Name          | Description        |
| -------------------- | ------------------ |
| `OPENROUTER_API_KEY` | OpenRouter API Key |
| `EMAIL_USER`         | Your Gmail address |
| `EMAIL_PASS`         | Gmail App Password |

---

### 3️⃣ Enable Gmail App Password

1. Enable **2-Step Verification**
2. Generate **App Password**
3. Use it in `EMAIL_PASS`

---

### 4️⃣ Workflow Configuration

File: `.github/workflows/ai-review.yml`

Triggers on:

```yaml
on:
  pull_request:
    types: [opened, synchronize]
```

---

### 5️⃣ Install Dependencies (for local testing)

```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

### 🔹 Step 1: PR Trigger

GitHub detects a pull request event.

### 🔹 Step 2: Workflow Runs

GitHub Actions spins up an **Ubuntu VM**.

### 🔹 Step 3: Script Execution

* Fetches PR diff using GitHub API
* Builds AI prompt

### 🔹 Step 4: AI Processing

* Sends data to OpenRouter
* Receives structured review

### 🔹 Step 5: Output

* 💬 Comment posted on PR
* 📧 Email sent to team

---

## 📧 Email Preview

* 🚀 PR Review Report
* 📦 Repository & PR Info
* 🔍 Issues & Suggestions
* 🔗 Direct PR Link
* 🎨 Styled HTML layout

---

## 🔐 Security

* No secrets stored in code
* Uses GitHub Secrets for:

  * API keys
  * Email credentials

---

## ⚠️ Limitations

* Large PRs may hit token limits
* AI output quality depends on prompt
* Gmail SMTP has sending limits

---

## 🚀 Future Improvements

* 💬 Inline PR comments (line-by-line review)
* 🧠 Multi-agent architecture
* 📊 PR scoring system
* 🛡️ Security vulnerability detection
* 📦 File-wise review support
* 💎 Advanced HTML email UI
* 🔔 Slack / Discord notifications

---

## 💡 Use Cases

* Automated code review
* Developer productivity tools
* CI/CD enhancement
* AI DevOps pipelines

---

## 🧑‍💻 Author

**Ved (v)**
AI & Backend Developer

---

## ⭐ Contribute

Feel free to fork this repo and improve it 🚀

---

## 📜 License

MIT License