# How to Push This Project to GitHub

Follow these steps to get your project on GitHub:

## Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in to your account
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the repository details:
   - **Repository name**: `liverpool_game` (or any name you prefer)
   - **Description**: "Automated calendar for Liverpool FC and big European club matches"
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

## Step 2: Initialize Git in Your Local Project

Open your terminal and navigate to your project directory:

```bash
cd /Users/Mark/liverpool_game
```

Initialize git (if not already initialized):

```bash
git init
```

## Step 3: Add All Files to Git

Add all project files to git staging:

```bash
git add .
```

**Note**: The `.gitignore` file will automatically exclude:
- Virtual environment (`.venv/`)
- Generated calendar file (`football_schedule.ics`)
- Python cache files
- Other unnecessary files

## Step 4: Create Your First Commit

Commit the files with a descriptive message:

```bash
git commit -m "Initial commit: Liverpool FC calendar generator"
```

## Step 5: Connect to Your GitHub Repository

Add your GitHub repository as the remote origin. Replace `<your-username>` with your actual GitHub username:

```bash
git remote add origin https://github.com/<your-username>/liverpool_game.git
```

**Alternative (if using SSH):**
```bash
git remote add origin git@github.com:<your-username>/liverpool_game.git
```

## Step 6: Push to GitHub

Push your code to the main branch:

```bash
git branch -M main
git push -u origin main
```

You'll be prompted for your GitHub credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your GitHub password)

### If You Need a Personal Access Token:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click **"Generate new token (classic)"**
3. Give it a name (e.g., "liverpool_game")
4. Select scopes: at minimum check **"repo"**
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't see it again)
7. Use this token as your password when pushing

## Step 7: Verify

Go to your GitHub repository page and verify that all files are uploaded correctly.

## Future Updates

When you make changes to your code, use these commands to update GitHub:

```bash
# Stage your changes
git add .

# Commit with a message
git commit -m "Description of your changes"

# Push to GitHub
git push
```

## Troubleshooting

### If you get "remote origin already exists":
```bash
git remote remove origin
git remote add origin https://github.com/<your-username>/liverpool_game.git
```

### If you need to update the remote URL:
```bash
git remote set-url origin https://github.com/<your-username>/liverpool_game.git
```

### If you get authentication errors:
- Make sure you're using a Personal Access Token, not your GitHub password
- For SSH: ensure your SSH key is added to your GitHub account

## Quick Reference Commands

```bash
# Check status
git status

# See what files are tracked
git ls-files

# View commit history
git log

# View remote repository
git remote -v
```

---

**That's it!** Your project should now be live on GitHub. 🎉


