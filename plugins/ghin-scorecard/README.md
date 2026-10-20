# GHIN Scorecard

Post a golf round to GHIN (the USGA's Golf Handicap Information Network) from a screenshot of your scorecard. Built for Garmin Golf screenshots; other scorecard images work through the same checks, less reliably.

## What it does

1. Warns you up front that you need to be signed in to ghin.com, then opens GHIN and checks that you actually are before doing anything else. If GHIN shows its sign-in page, it asks you to log in yourself and waits.
2. Reads the course, layout, tee, date, par row, and per-hole scores from the image, and checks every subtotal.
3. Shows you the extracted par and scores for all 18 holes as tables so you can check them against the image.
4. Asks only what the image can't answer: always the score type (Home, Away, or Competition), plus anything unreadable.
5. Picks the course and tee, sets the score type and date, and enters the hole scores.
6. Shows GHIN's values next to the image's, then stops and asks before clicking **Post Score**.
7. After you confirm, posts once and reports the score and differential from GHIN's round summary.

## Requirements

- **A browser Claude can control:** the Claude in Chrome extension (installed and connected), or the Claude desktop app's built-in browser.
- **A GHIN account with an active Handicap Index**, through a club or golf association that uses GHIN.
- **Signed in to ghin.com** in that browser. GHIN sessions expire, so you may need to sign in again. Claude checks this first and never types your GHIN password or clicks Log In, even when your browser has autofilled the form.
- **Site permission for ghin.com** when the browser extension asks.

## Install

Add the marketplace `benchi/claude-plugins` (claude.ai: Customize → Plugins → Add → Add marketplace), or in Claude Code:

```bash
claude plugin marketplace add benchi/claude-plugins
claude plugin install ghin-scorecard@benchi
```

## Usage

Attach a scorecard screenshot and say something like "post this round to GHIN", or run `/ghin-scorecard:post-scorecard-to-ghin`.

Best input: the Garmin Golf round detail screen (shows tee, date, and a par row). The orange Garmin share card works too, but has no tee or date, so Claude will ask for them.

## Safety

- Nothing is posted until you say yes in chat, and Claude clicks Post Score only once.
- GHIN applies the net double bogey adjustment itself; scores are entered exactly as played.
- If something goes wrong, GHIN's round summary page has a **Delete round** link.

## Limitations

- GHIN only (USGA). Other handicap systems aren't supported.
- Scores only; putts, fairways, and GIR aren't posted.
- GHIN's page layout can change. If it does, Claude adapts and tells you the skill may need updating.
