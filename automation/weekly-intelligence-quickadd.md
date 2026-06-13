# Weekly Intelligence Report — QuickAdd & Automation

## QuickAdd Command: `New Weekly Report`

**Settings:**
- Template: `templates/weekly-intelligence-report.md`
- Output path: `vault/06-meta-intelligence/dashboards/weekly-reports/`
- File name: `{{DATE:YYYY-[W]WW}} Weekly Intelligence Report`
- Open after creation: ✅

**Periodic Notes integration:**
- Configure in Periodic Notes plugin as "Weekly Note"
- Template: `templates/weekly-intelligence-report.md`
- Folder: `vault/06-meta-intelligence/dashboards/weekly-reports/`

## Agent-Assisted Workflow

After creating the note, invoke the Chief of Staff agent with this prompt:

```
You are the Chief of Staff. Today is {{DATE}}.

Using the MCP vault access, populate the weekly intelligence report for {{WEEK}}.

Steps:
1. Search vault for signals, trends, competitor notes created in the last 7 days
2. Search for opportunities with status: researching or ready-for-review, sorted by composite_score
3. Search for decisions with status: draft or ready-for-review, sorted by review_date
4. Search for forecasts with deadline within 30 days
5. Search for risks with status: active and impact: high
6. Search for lessons created in the last 7 days

Populate each section of the report with factual findings from the vault.
Do not invent data. If a section is empty, write "Nothing new this week."
Add your synthesis in Section 7: What Changed, Biggest Unknown, and CEO Priority.
```

## Automation Triggers

| Trigger | Action |
|---|---|
| Every Monday 08:00 | Create new weekly report from template |
| Every Friday 17:00 | Remind to complete Section 7 synthesis |
| Report status = "draft" after 48h | Alert: incomplete report |

## Calendar Integration

Add to Obsidian Calendar plugin:
- Weekly notes linked to `vault/06-meta-intelligence/dashboards/weekly-reports/`
- Each week cell shows report status (draft / complete)
