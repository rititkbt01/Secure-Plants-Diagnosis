# Contributing to Secure-Plants_Diagnosis

Welcome, Group 31! This guide explains how to contribute code to this repository.
Following these rules ensures clean history, easy code review, and a professional
repository that your supervisor and evaluators can appreciate.

---

## 🌿 Branching Strategy

```
main              ← Protected. Production-ready code only. Never push directly here.
  └── develop     ← Integration branch. All features merge here first.
       ├── feature/backend-auth         (Ritik Budhathoki)
       ├── feature/backend-security     (Ritik Budhathoki)
       ├── feature/flutter-camera       (Jeshik Neupane)
       ├── feature/flutter-ui           (Jeshik Neupane)
       ├── feature/data-pipeline        (Rishi Kumar Kushwaha)
       ├── feature/model-optimization   (Rishav Dhakal)
       └── feature/deit-training        (Yashraj Shrestha)
```

### Rules
- **`main`** is protected — only merged from `develop` after full team review
- **`develop`** is the active integration branch — merge here when a feature is complete
- **Feature branches** are created per milestone/task
- **Never** commit directly to `main` or `develop`
- **Delete** your feature branch after it's merged

---

## 🔁 Workflow (Step-by-Step)

### 1. Always Start From the Latest `develop`
```bash
git checkout develop
git pull origin develop
```

### 2. Create Your Feature Branch
```bash
# Format: feature/<your-component>-<short-description>
git checkout -b feature/backend-auth
```

### 3. Make Your Changes
- Work only in your assigned domain folder
- Keep commits small and focused (1 logical change per commit)

### 4. Stage and Commit
```bash
git add .
git commit -m "feat(backend): add JWT authentication middleware"
```

### 5. Push Your Branch
```bash
git push origin feature/backend-auth
```

### 6. Open a Pull Request (PR)
- Base branch: `develop`
- Fill in the PR template completely
- Link to the relevant GitHub Issue
- Request review from at least 1 team member

### 7. After Review and Approval
- The reviewer merges the PR (not the author)
- Delete the feature branch after merge

---

## 📝 Commit Message Convention

We follow **Conventional Commits** format:

```
<type>(<scope>): <short description>

[optional body — explain WHY not WHAT]

[optional footer — e.g., Closes #12]
```

### Types
| Type | When to Use |
|------|------------|
| `feat` | Adding a new feature |
| `fix` | Fixing a bug |
| `docs` | Documentation only changes |
| `style` | Formatting, no logic change |
| `refactor` | Code restructuring, no feature change |
| `test` | Adding or updating tests |
| `chore` | Build process, config, dependencies |
| `data` | Dataset changes or additions |
| `model` | ML model architecture or training changes |

### Scope (your domain)
`backend` | `mobile` | `ml` | `data` | `docs` | `ci`

### Examples
```bash
feat(backend): add magic byte validation for image uploads
fix(mobile): correct image compression before upload
docs(ml): add training instructions to README
model(ml): configure DeiT-Tiny distillation token
data(ml): add augmentation pipeline for PlantVillage
test(backend): add JWT auth unit tests
chore(ci): update GitHub Actions Python version to 3.11
```

---

## 🔍 Pull Request Process

1. **Title** — follow commit convention: `feat(backend): add JWT auth`
2. **Description** — fill in the PR template (what changed, why, how tested)
3. **Link Issue** — every PR must reference a GitHub Issue (`Closes #N`)
4. **Tests** — all existing tests must pass; add new tests for new features
5. **Review** — at least **1 team member** must approve before merging
6. **No self-merge** — the PR author cannot approve their own PR

---

## 🏷️ Issue Labels

| Label | Meaning |
|-------|---------|
| `backend` | Backend/API related |
| `mobile` | Flutter app related |
| `ml` | Machine learning related |
| `data` | Dataset/pipeline related |
| `docs` | Documentation |
| `bug` | Something is broken |
| `enhancement` | New feature request |
| `sprint-task` | Assigned sprint task |
| `blocked` | Waiting on another task |

---

## 📁 Domain Ownership

| Team Member | Branch Prefix | Folder |
|-------------|--------------|--------|
| Ritik Budhathoki | `feature/backend-*` | `backend/` |
| Jeshik Neupane | `feature/flutter-*` | `mobile/` |
| Yashraj Shrestha | `feature/deit-*` | `ml/src/models/`, `ml/notebooks/` |
| Rishi Kumar Kushwaha | `feature/data-*` | `ml/src/data/`, `data/` |
| Rishav Dhakal | `feature/model-optimization-*` | `ml/src/evaluation/` |

---

## 📏 Code Style

### Python (Backend + ML)
- Follow **PEP 8** style guide
- Max line length: **88 characters** (Black formatter)
- Use **type hints** for all function signatures
- All functions must have **docstrings**
- Run before committing: `flake8 .` and `black .`

### Dart (Flutter)
- Follow **Dart style guide** and `flutter analyze`
- Use `const` constructors where possible
- All public classes/methods must have doc comments (`///`)
- Run before committing: `flutter analyze`

---

## 🧪 Testing

- **Backend:** `pytest backend/tests/`
- **ML:** `pytest ml/tests/`
- **Mobile:** `flutter test`
- CI will run all tests automatically on every push and PR

---

## ❓ Questions?

Ask in the **Google Chat** group or tag `@ritik` for project structure questions.
