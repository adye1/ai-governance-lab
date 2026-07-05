# Git setup & secret-scanning workflow

This repo blocks secrets from ever being committed, using **gitleaks** wired into a **pre-commit hook**. Set it up once per clone.

## One-time setup

1. **Install gitleaks** (if not already):
   ```bash
   # check github.com/gitleaks/gitleaks/releases for the current version
   cd /tmp
   curl -sL https://github.com/gitleaks/gitleaks/releases/download/v8.28.0/gitleaks_8.28.0_linux_x64.tar.gz -o gitleaks.tar.gz
   tar xzf gitleaks.tar.gz gitleaks
   sudo mv gitleaks /usr/local/bin/ && gitleaks version
   ```

2. **Activate the hook** (points git at the version-controlled hooks directory, so the hook travels with the repo):
   ```bash
   git config core.hooksPath .githooks
   ```

3. **Confirm it's active** — this should now scan on every commit:
   ```bash
   git commit --allow-empty -m "chore: verify pre-commit hook"
   # you should see: [pre-commit] scanning staged changes for secrets...
   ```

## Everyday workflow

```bash
gitleaks detect --source . --no-git -v   # optional: scan whole tree anytime
git add <files>
git commit -m "feat: ..."                # hook auto-scans staged changes; blocks on a hit
git push
```

If the hook **blocks** a commit: remove the flagged value, replace it with a placeholder or move it to a `*.example` file, re-stage, and commit again. Only bypass with `git commit --no-verify` if you have **confirmed** it's a false positive — and prefer allowlisting it in `.gitleaks.toml` instead.

## Commit message convention

Use conventional prefixes so the history reads cleanly to reviewers:

| Prefix | Use for |
|--------|---------|
| `docs:` | documentation, README, methodology |
| `feat:` | new capability (a test suite, a control, an app) |
| `fix:` | corrections |
| `chore:` | tooling, config, housekeeping |

Commit **per meaningful unit of work**, as you build each phase — not one giant dump. The incremental history is itself part of what makes the repo credible.

## Optional next steps (recommended for a security portfolio)

- **Signed commits** — enable SSH or GPG commit signing for the "Verified" badge on GitHub.
- **gitleaks in CI** — add a GitHub Actions workflow that runs gitleaks on every push, so the repo shows a passing security check publicly.
