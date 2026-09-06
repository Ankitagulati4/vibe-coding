---
mode: agent
description: Security review of the current changes or selected code
---

Review the current changes (or the code I have open/selected) for:

- Hardcoded secrets, API keys, or credentials
- SQL injection or unsanitized input risks
- Missing input validation on new endpoints
- Dependencies added without a clear reason

Report findings as a checklist. Flag severity (low / medium / high) for each,
and suggest a concrete fix. If nothing is found, say so explicitly — don't
invent issues.
