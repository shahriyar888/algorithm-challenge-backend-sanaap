# Git Flow Workflow

این پروژه با استفاده از **Git Flow** و با ساختار برنچ سفارشی زیر مدیریت می‌شود:

- برنچ اصلی (Production): `main`
- برنچ توسعه (Development): `development`

---

## 🌳 Branch Structure

| Branch | توضیح |
|------|------|
| `main` | نسخه پایدار و آماده Production |
| `development` | نسخه در حال توسعه و تست |
| `feature/*` | توسعه تسک‌ها و قابلیت‌ها |
| `release/*` | آماده‌سازی نسخه نهایی |
| `hotfix/*` | رفع باگ‌های فوری Production |

---

## 🔁 Development Workflow

### 1️⃣ ایجاد Feature Branch

```bash
git checkout development
git flow feature start algorithm-task-1
```

- برنچ ساخته می‌شود از `development`
- نام نمونه: `feature/algorithm-task-1`

---

### 2️⃣ ارسال Pull Request

```bash
git push origin feature/algorithm-task-1
```

در GitHub:
- base branch: `development`
- compare branch: `feature/algorithm-task-1`
- Code Review الزامی است

Merge Strategy:
- **Squash Merge** برای feature‌ها

---

## 🚀 Release Flow

```text
development → release/x.y.z → main
                        ↘︎ development
```

### مراحل:
```bash
git flow release start 1.0.0
```

پس از آماده‌سازی:
- PR از `release/1.0.0` به `main`
- PR دوم از `release/1.0.0` به `development`

Merge به `main` به‌صورت **Merge Commit** انجام می‌شود.

---

## 🔥 Hotfix Flow

```text
hotfix/fix-bug → main
              ↘︎ development
```

```bash
git flow hotfix start fix-critical-bug
```

---

## 🔒 Branch Protection Rules (GitHub)

### main
- No direct push
- Require Pull Request
- Require CI checks

### development
- No direct push
- Require Pull Request

---

## 🏷️ Commit Message Convention

```text
feat: implement algorithm task 1
fix: handle circular binary edge case
docs: update algorithm readme
```

---

## جمع‌بندی

- Git Flow برای کنترل حرفه‌ای توسعه استفاده شده
- تمام تغییرات از طریق Pull Request مدیریت می‌شوند
- ساختار برای توسعه تیمی و CI/CD آماده است

