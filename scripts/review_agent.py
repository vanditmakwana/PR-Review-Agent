import os
import requests
from .github_utils import get_pr_diff, post_comment
from .prompt import build_prompt

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
PR_NUMBER = os.environ["PR_NUMBER"]

def call_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "PR Review Agent"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    # 🔥 DEBUG (IMPORTANT)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]


def main():
    print("Fetching PR diff...")
    diff = get_pr_diff(REPO, PR_NUMBER, GITHUB_TOKEN)

    print("Generating review...")
    prompt = build_prompt(diff)
    review = call_openrouter(prompt)

    print("Posting comment...")
    post_comment(REPO, PR_NUMBER, review, GITHUB_TOKEN)

    print("✅ Done")


if __name__ == "__main__":
    main()