# Parallel Worlds: technical foundation

## Decision

Keep the game local-first and static. Ren'Py produces the browser build, GitHub
Pages serves it, and Ren'Py's save/persistent systems hold progress in the
player's browser. There is no application server or database in the critical
path.

This is the leanest zero-service architecture for the current product because
the game has no real account, payment, cross-device sync, multiplayer, or
leaderboard requirement. Koyeb or another Python host would add operational
work without making the story more playable.

## Runtime flow

1. GitHub Actions builds or publishes the generated web distribution.
2. The browser loads the Ren'Py WebAssembly runtime and game archives.
3. Story choices update Ren'Py variables and named memories.
4. Save slots and persistent unlocks remain on the device.
5. The centralized ending resolver maps the decisive route and accumulated
   relationships/traits to exactly six authored endings.

## What changed

- Removed the simulated email, referral, payment, narration-account, and
  chapter-paywall flows.
- Reconnected Chapter 1 to Acts 2-4 so a new game reaches the complete season.
- Added a local profile and one-time content notice.
- Centralized ending resolution and unlock persistence.
- Added a responsive end-of-season summary and records loop.
- Reworked dialogue positioning, mobile-safe controls, touch sizing, and the
  browser shell.
- Added a deliberate portrait orientation message; landscape remains the
  supported mobile play layout because dialogue and decisions need width.
- Enabled progressive web downloads for the generated build.

## When a backend becomes justified

Add a small API and managed database only when the product genuinely needs one
of these: authenticated cross-device saves, paid entitlements, shared/community
statistics, cloud moderation, or live content delivery. Until then, the static
deployment is the production architecture, not a placeholder.

## Release checklist

- Run Ren'Py lint.
- Produce a clean web build.
- Smoke-test desktop, mobile landscape, and mobile portrait handling.
- Play every decisive route and confirm all six endings unlock.
- Publish only after narrative and content review.
