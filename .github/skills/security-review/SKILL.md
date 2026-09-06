---
name: security-review
description: Use when reviewing code for security problems — secrets,
  injection risks, and missing input validation. The agent reaches for
  this automatically when a task involves auth, user input, or new endpoints.
---

# Security review

Work through this checklist against the code in scope:

## Secrets
- [ ] No hardcoded API keys, passwords, tokens, or connection strings
- [ ] Secrets read from environment variables or a secret manager
- [ ] No `.env` file staged for commit

## Injection & untrusted input
- [ ] SQL uses parameterized queries — never string concatenation
- [ ] Shell/OS commands don't interpolate raw user input
- [ ] User-supplied paths are validated (no `../` traversal)

## Validation
- [ ] Every new endpoint validates its input (Pydantic / schema)
- [ ] Output that reflects user input is escaped/encoded

## Dependencies
- [ ] Any newly added dependency has a clear reason and a trusted source

Report findings as a checklist. Flag a **severity** (low / medium / high)
for each issue, and suggest the fix.

## Demo prompts (say these to trigger this skill)
- "Review this login endpoint for security issues before I ship it."
- "Check my code for hardcoded secrets or API keys."
- "Is this database query safe from SQL injection?"
- "Audit this new endpoint — does it validate its input properly?"

Signal words that fire it: *security, review, safe, secrets, injection,
validate, audit, vulnerability, credentials*.
