# Deploy Runbook

## Pre-deploy
- Validate env vars from `.env.example`
- Run lint/format/tests

## Deploy
- Promote approved branch/tag
- Monitor logs and output integrity

## Rollback
- Revert to prior tag/commit
- Re-run with known-good env config
