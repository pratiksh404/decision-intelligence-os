# Review Automation Framework — QuickAdd & Periodic Notes

## QuickAdd Commands

Configure each as a QuickAdd Macro in Obsidian:

### 1. New Daily Review
- Template: `templates/daily-review.md`
- Output: `vault/06-meta-intelligence/dashboards/daily-reviews/{{DATE:YYYY-MM-DD}} Daily Review`
- Open after creation: ✅
- Trigger: Morning — or via Commander button in toolbar

### 2. New Weekly Report
- Template: `templates/weekly-intelligence-report.md`
- Output: `vault/06-meta-intelligence/dashboards/weekly-reports/{{DATE:YYYY-[W]WW}} Weekly Report`
- Open after creation: ✅

### 3. New Monthly Review
- Template: `templates/monthly-review.md`
- Output: `vault/06-meta-intelligence/dashboards/monthly-reviews/{{DATE:YYYY-MM}} Monthly Review`
- Open after creation: ✅

### 4. New Quarterly Review
- Template: `templates/quarterly-review.md`
- Output: `vault/06-meta-intelligence/dashboards/quarterly-reviews/{{DATE:YYYY}}-Q{{QUARTER}} Quarterly Review`
- Open after creation: ✅

---

## Periodic Notes Plugin Configuration

```
Daily:    templates/daily-review.md      → vault/06-meta-intelligence/dashboards/daily-reviews/
Weekly:   templates/weekly-intelligence-report.md → vault/06-meta-intelligence/dashboards/weekly-reports/
Monthly:  templates/monthly-review.md   → vault/06-meta-intelligence/dashboards/monthly-reviews/
Quarterly: templates/quarterly-review.md → vault/06-meta-intelligence/dashboards/quarterly-reviews/
```

---

## Review Cadence Summary

| Review | Frequency | Template | Focus |
|---|---|---|---|
| Daily | Every day | `daily-review.md` | Inbox, tasks, signals |
| Weekly | Every Monday | `weekly-intelligence-report.md` | Intelligence, opportunities, decisions, forecasts |
| Monthly | 1st of month | `monthly-review.md` | Calibration, bias, portfolio |
| Quarterly | Q start | `quarterly-review.md` | Strategy, resources, bets |

---

## Reminder Automation

Add these to your calendar or Obsidian Reminder plugin:

| Trigger | Action |
|---|---|
| Daily 07:30 | Open/create daily review |
| Monday 08:00 | Create weekly intelligence report |
| 1st of month | Create monthly review |
| Jan 1, Apr 1, Jul 1, Oct 1 | Create quarterly review |
| Any forecast deadline reached | Run forecast resolution workflow |
| Any assumption review_date passed | Open assumption for review |
