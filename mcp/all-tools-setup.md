# MCP Setup — All AI Tools

Configs for all 6 tools. All four MCP servers are identical across tools — only the file format and install location differ.

**Prerequisites (run once):**
```bash
# 1. Install Obsidian Local REST API plugin
#    Obsidian → Settings → Community Plugins → "Local REST API" → Install → Enable
#    Copy the generated API key.

# 2. Get a Firecrawl API key
#    https://firecrawl.dev/

# 3. Create your shared .env
cat > /Users/pratiksh/Documents/work/decision-intelligence-os/mcp/.env << 'EOF'
OBSIDIAN_API_KEY=paste-your-obsidian-key-here
FIRECRAWL_API_KEY=paste-your-firecrawl-key-here
EOF
```

---

## Claude Desktop

**Config file:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```bash
cp mcp/claude-desktop-config.json \
   "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
```

Restart Claude Desktop. Test: ask Claude to "list active forecasts from the vault."

---

## Claude Code

**Config file:** `.mcp.json` in project root (already created — project-scoped, shared with teammates)

```bash
# Load env vars, then start a session
export $(grep -v '^#' mcp/.env | xargs)
claude

# Verify inside the session:
/mcp
```

Claude Code reads `.mcp.json` at startup. Approve the servers when prompted.

To register globally instead (all projects, just you):
```bash
claude mcp add --scope user filesystem -- \
  npx -y @modelcontextprotocol/server-filesystem \
  /Users/pratiksh/Documents/work/decision-intelligence-os

claude mcp add --scope user git -- \
  npx -y @modelcontextprotocol/server-git

claude mcp add --scope user obsidian -- \
  npx -y mcp-obsidian \
  --env OBSIDIAN_VAULT_PATH=/Users/pratiksh/Documents/work/decision-intelligence-os/vault \
  --env OBSIDIAN_API_KEY=${OBSIDIAN_API_KEY}

claude mcp add --scope user firecrawl -- \
  npx -y firecrawl-mcp \
  --env FIRECRAWL_API_KEY=${FIRECRAWL_API_KEY}
```

---

## Agy (Google Antigravity CLI / IDE)

**Config file:** `~/.gemini/config/mcp_config.json` (shared across Agy CLI and Agy IDE)

```bash
mkdir -p ~/.gemini/config
cp mcp/agy-mcp-config.json ~/.gemini/config/mcp_config.json
```

> **Known Agy limitation (as of May 2026):** Environment variable interpolation in `mcp_config.json` is broken.
> You must hard-code API keys directly in the file until Google fixes this.

```bash
# Substitute your actual keys into the installed copy:
sed -i '' \
  "s|\${OBSIDIAN_API_KEY}|$(grep OBSIDIAN_API_KEY mcp/.env | cut -d= -f2)|g" \
  ~/.gemini/config/mcp_config.json

sed -i '' \
  "s|\${FIRECRAWL_API_KEY}|$(grep FIRECRAWL_API_KEY mcp/.env | cut -d= -f2)|g" \
  ~/.gemini/config/mcp_config.json
```

Restart Agy CLI or IDE. Verify with `/mcp` in Agy CLI.

---

## Codex CLI (OpenAI)

**Config file:** `~/.codex/config.toml`

```bash
mkdir -p ~/.codex

# Append the MCP block to your existing config (or create it):
cat mcp/codex-config.toml >> ~/.codex/config.toml
```

Then export your keys before running codex:
```bash
export OBSIDIAN_API_KEY=$(grep OBSIDIAN_API_KEY mcp/.env | cut -d= -f2)
export FIRECRAWL_API_KEY=$(grep FIRECRAWL_API_KEY mcp/.env | cut -d= -f2)
codex
```

Or add them permanently to your shell profile (`~/.zshrc`):
```bash
echo 'export OBSIDIAN_API_KEY="your-key"' >> ~/.zshrc
echo 'export FIRECRAWL_API_KEY="your-key"' >> ~/.zshrc
```

Verify: `codex mcp list`

---

## GitHub Copilot (VS Code)

**Config file:** `.vscode/mcp.json` in project root (already created)

VS Code reads `.vscode/mcp.json` automatically. On first use, it prompts for API keys via its secure input UI — no keys are stored in the file.

1. Open VS Code in this project folder
2. Open any Copilot Chat pane
3. Run command: `MCP: List Servers` — you should see all 4 servers
4. VS Code prompts for `Obsidian Local REST API Key` and `Firecrawl API Key` on first use and stores them securely

To also enable globally (user profile):
- Run `MCP: Open User Configuration` from the command palette
- Paste the contents of `.vscode/mcp.json` there (replacing `${input:*}` with actual values or re-adding inputs)

---

## OpenCode (SST)

**Config file:** `opencode.json` in project root (already created)

```bash
# Load env vars, then start opencode
export $(grep -v '^#' mcp/.env | xargs)
opencode
```

OpenCode uses `{env:VAR_NAME}` interpolation, so keys are read from your shell environment — nothing is hard-coded.

Verify: `opencode mcp list`

---

## Summary Table

| Tool | Config File | Key Format | Env Var Support |
|---|---|---|---|
| Claude Desktop | `~/Library/Application Support/Claude/claude_desktop_config.json` | `mcpServers` JSON | `${VAR}` (via shell) |
| Claude Code | `.mcp.json` (project) or `~/.claude.json` (user) | `mcpServers` JSON | `${VAR}` (via shell) |
| Agy CLI/IDE | `~/.gemini/config/mcp_config.json` | `mcpServers` JSON | ⚠️ Broken — hard-code keys |
| Codex CLI | `~/.codex/config.toml` | TOML `[mcp_servers.*]` | `${VAR}` (via shell) |
| Copilot/VS Code | `.vscode/mcp.json` | `servers` JSON | `${input:id}` (secure prompt) |
| OpenCode | `opencode.json` | `mcp` JSON | `{env:VAR}` |

---

## Shared .env (never commit this)

```
mcp/.env     ← gitignored — your API keys live here
```

The `.gitignore` entry `mcp/.env` is already specified in `mcp/installation-guide.md`. Verify:
```bash
grep "mcp/.env" .gitignore || echo 'mcp/.env' >> .gitignore
```
