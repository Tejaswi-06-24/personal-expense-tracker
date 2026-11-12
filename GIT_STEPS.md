# Git Steps

**Student 1 (owner):**
```bash
git init
git branch -M main
git add .
git commit -m "Add starter project"
git remote add origin https://github.com/YOUR_USERNAME/personal-expense-tracker.git
git push -u origin main
```
Create an **empty public** repository on GitHub *before* the remote/push commands; invite Student 2 as collaborator.

**Student 2:** accept invite, then run from a folder that does not contain the project:
```bash
git clone https://github.com/YOUR_USERNAME/personal-expense-tracker.git
cd personal-expense-tracker
git switch -c feature-member2
```

**Student 1:** in the original repository folder:
```bash
git switch -c feature-member1
```

**Both students:** independently complete the assigned functions and use a real commit for each meaningful change:
```bash
git status
git add .
git commit -m "Describe the real change"
```
Each student should make **4+ meaningful commits**. Then:
```bash
git push -u origin feature-member1
```
Student 2 instead pushes `feature-member2`.

**Pull requests:** On GitHub, each student opens a PR targeting `main`; the other student reviews it. Merge the two PRs. If `main.py` conflicts, carefully preserve both sets of changes.

**Merge-conflict exercise (do separately from feature PRs):**
1. After both feature PRs are merged, Student 1 creates `conflict-member1` from latest `main`, changes the *same* first heading line in `README.md` to `# Expense Tracker - Version A`, commits and pushes.
2. Student 2 creates `conflict-member2` from the *same old main commit* (before Student 1's conflict change), changes the line to `# Expense Tracker - Version B`, commits and pushes.
3. Merge `conflict-member1` into `main` through a PR.
4. On Student 2's computer, run `git fetch origin`, then `git switch conflict-member2` and `git merge origin/main`. Git should report a conflict in README.md. Capture a screenshot.
5. Edit README.md to one agreed title, remove `<<<<<<<`, `=======`, and `>>>>>>>` markers; then run `git add README.md` and `git commit -m "Resolve README merge conflict"`. Capture a screenshot.
6. Push the resolved branch and open its PR to main. Both students participate in review and conflict resolution (e.g. discuss and approve resolution in PR comments).

**Evidence:**
```bash
git log --oneline --graph --all
```
Take genuine screenshots of commits, branches, PRs, peer reviews, conflict markers, resolution, and the working program. Do not fabricate GitHub activity.
