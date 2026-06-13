# MCP Integration — Installation Guide & Security Model

## Architecture Overview

```
Claude / AI Agent
       │
       ▼
  MCP Protocol
  ┌────────────────────────────────────────────┐
  │  obsidian-mcp    filesystem-mcp            │
  │  git-mcp         firecrawl-mcp             │
  └────────────────────────────────────────────┘
       │
       ▼
  Decision Intelligence OS Vault
```

---

## 1. Prerequisites

```bash
# Node.js 18+ required
node --version

# Install Obsidian Local REST API plugin
# In Obsidian: Settings → Community Plugins → Search "Local REST API" → Install → Enable
# Copy the generated API key — you will need it below.
```

---

## 2. Environment Variables

Create `/Users/pratiksh/Documents/work/decision-intelligence-os/mcp/.env`:

```bash
OBSIDIAN_API_KEY=<paste-your-obsidian-rest-api-key-here>
FIRECRAWL_API_KEY=<paste-your-firecrawl-api-key-here>
```

**Never commit `.env` to git.** It is already listed in `.gitignore` (see Section 6).

---

## 3. Claude Desktop Configuration

Copy the generated config to Claude Desktop's config directory:

```bash
# macOS
cp mcp/claude-desktop-config.json \
   "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
```

Then restart Claude Desktop. The four MCP servers will appear in the tools panel.

---

## 4. MCP Server Capabilities

### obsidian-mcp
| Capability | Vault Path |
|---|---|
| Search notes | All layers |
| Read notes | All layers |
| Create notes | `00-inbox/` only (agents write here) |
| Update metadata | `02-decisions/`, `04-learning/` |
| List linked notes | All layers |

### filesystem-mcp
| Capability | Scope |
|---|---|
| Read markdown | `templates/`, `workflows/`, `advisors/` |
| Read exports | `reviews/`, `automation/` |
| List directory | Entire repo (read-only) |

### git-mcp
| Capability | Notes |
|---|---|
| Track changes | Full commit history |
| Compare revisions | Diff any note revision |
| Rollback decisions | Restore prior note state |

### firecrawl-mcp
| Capability | Use case |
|---|---|
| Web search / crawl | Market research, competitor moves |
| Page scrape | Scraping target URLs and documentation |
| Results piped to | `vault/00-inbox/` as raw signals |

---

## 5. Agent Access Model

```
Read Access:    All 6 vault layers + templates + workflows + advisors
Write Access:   vault/00-inbox/ (staging only)
Promote Access: Human-approved — move from inbox to target layer
Delete Access:  Disabled for all agents
Git Operations: Read + compare only (no force-push, no reset)
```

AI agents **must not** write directly to `02-decisions/` through `06-meta-intelligence/`.
All agent output lands in `00-inbox/` for human review and promotion.

---

## 6. Security Hardening

### .gitignore additions (append to repo root .gitignore)
```
mcp/.env
mcp/secrets/
*.key
*.pem
```

### Obsidian Local REST API
- Enable HTTPS in the plugin settings (self-signed cert is fine locally)
- Rotate the API key every 90 days
- The plugin listens on `127.0.0.1` only — not exposed to the network

### Filesystem MCP scope
The server is initialized with the repo root path. It cannot read outside that directory tree — no access to `~/.ssh`, `~/.aws`, or other sensitive paths.

---

## 7. Verifying the Integration

Open a new Claude conversation and run:

```
Use the obsidian MCP to search for notes with type: forecast that have status: active.
List their titles and deadlines.
```

Expected: Claude returns a table of active forecasts from `vault/02-decisions/forecasts/`.

---

## 8. Troubleshooting

| Symptom | Fix |
|---|---|
| "MCP server not found" | Restart Claude Desktop after saving config |
| "401 Unauthorized" | Check `OBSIDIAN_API_KEY` in `.env` |
| "Vault path not found" | Verify `OBSIDIAN_VAULT_PATH` points to `vault/` subfolder |
| Firecrawl fails | Confirm `FIRECRAWL_API_KEY` is valid at firecrawl.dev |
