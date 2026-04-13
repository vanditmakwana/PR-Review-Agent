def build_prompt(diff: str) -> str:
    return f"""
You are a strict senior software engineer reviewing a pull request.

Analyze the code diff and provide:

1. Bugs
2. Code improvements
3. Security issues
4. Performance issues

Format:

### 🔍 Issues
- File:
- Problem:

### ✅ Suggestions
- Fix:

Be concise.

PR DIFF:
{diff}
"""