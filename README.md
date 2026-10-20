# Claude plugins by Laurent Benchimol

A plugin marketplace for Claude. Add it once to get every plugin listed here, and updates as they ship.

## Plugins

| Plugin | Version | What it does |
|---|---|---|
| [ghin-scorecard](plugins/ghin-scorecard) | 0.2.0 | Post a golf round to GHIN hole-by-hole from a scorecard screenshot (e.g. Garmin Golf). Shows the extracted scores for review and posts only after you confirm. |

## Install

**claude.ai, the Claude desktop app, or Cowork**

1. Go to **Customize → Plugins → Add → Add marketplace**.
2. Enter `benchi/claude-plugins`.
3. Find the plugin under Discover and select **Add**.

Plugins added this way are on your account, so they also load in Claude Code.

**Claude Code**

```bash
claude plugin marketplace add benchi/claude-plugins
claude plugin install ghin-scorecard@benchi
```

Or from inside a session: `/plugin install ghin-scorecard --marketplace benchi/claude-plugins`

To get new versions: `claude plugin update ghin-scorecard@benchi`

## Repository layout

```
.claude-plugin/marketplace.json   the marketplace catalog
plugins/<name>/                   one folder per plugin
  .claude-plugin/plugin.json      manifest, with an explicit version
  skills/…                        the plugin's skills
  README.md
scripts/check_versions.py         version check run by CI
```

## Versioning

Every plugin sets an explicit [semver](https://semver.org) `version` in its own `plugin.json`, and only there (not in `marketplace.json`).

- Bump the version in the same commit as any change to that plugin. Installed copies only update when the version changes.
- PATCH for fixes, MINOR for new behavior, MAJOR for changes that break how people use it.
- CI (`.github/workflows/validate.yml`) validates every plugin and fails a push or pull request that changes a plugin without bumping its version. Run the same check locally with `python3 scripts/check_versions.py origin/main`.

Never rename a published plugin: installs are recorded by name.

## License

[MIT](LICENSE)
