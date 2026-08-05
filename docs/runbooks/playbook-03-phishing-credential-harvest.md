# Playbook 03 — Phishing / Credential Harvest
**Triggers:** User report, Defender Phishing alert, URL click + risky sign-in combo
**SLA:** Block 15 min | Remediate 2h | Notify 24h

## 1. Triage (5 min)
- [ ] Confirm email in M365 Defender (Threat Explorer), note Message-ID
- [ ] Extract: sender domain, URL(s), attachments (SHA-256), recipient list
- [ ] Check clicks: `EmailEvents | where ThreatTypes has "Phish" | where RecipientEmailAddress == "<user>"`

## 2. Containment (15 min)
- [ ] Purge mailbox: Get-MessageTrace | Where MessageID -eq "<id>" | Remove-Message -Confirm:$false
- [ ] Block sender domain in Exchange Online (Tenant Allow/Block List)
- [ ] Revoke user's refresh tokens: `Revoke-MgUserSignInSession -UserId "<user>"`
- [ ] Force MFA re-auth on next login

## 3. Investigation (30 min)
- [ ] Did user enter credentials? Check `SigninLogs` for post-click logins from new IP
- [ ] If yes -> escalate to Playbook 01 (Account Compromise)
- [ ] Check OAuth consent grants for malicious app names

## 4. Eradication + Notify
- [ ] Remove malicious inbox rules (email exfil)
- [ ] Reset password if creds were entered
- [ ] Notify affected users (template: docs/templates/notify-nis2.md)
- [ ] NIS2 timeline: early warning 24h / detailed 72h / final 1 month
