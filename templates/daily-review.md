---
title: Daily Review — <% tp.date.now("YYYY-MM-DD") %>
type: daily-review
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
owner: Founder/CEO
tags:
  - daily-review
  - review
---
# Daily Review — <% tp.date.now("dddd, MMMM D, YYYY") %>

## Inbox Triage (≤ 15 min)

```dataview
TABLE file.ctime AS "Captured"
FROM "vault/00-inbox"
WHERE file.ctime >= date(today) - dur(1 day)
SORT file.ctime DESC
```

**Triage actions:**
- [ ] Promote relevant items to `01-intelligence/signals/`
- [ ] Archive noise
- [ ] Flag anything requiring a Decision Memo

## Today's Open Tasks

```tasks
not done
scheduled on <% tp.date.now("YYYY-MM-DD") %>
```

## Signals Review (new in last 24h)

```dataview
LIST
FROM "vault/01-intelligence/signals"
WHERE file.ctime >= date(today) - dur(1 day)
SORT file.ctime DESC
```

## 3 Priorities for Today
1. 
2. 
3. 

## End-of-Day Capture
**What was the most important thing I learned today?**

**Any new signals to log?**
