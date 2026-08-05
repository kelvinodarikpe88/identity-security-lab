# Playbook 01 — Account Compromise
**Triggers:** Risky sign-in (high), Impossible travel, Okta takeover alert, Credential stuffing
**SLA:** Contain 30 min | Eradicate 4h | Recover 24h

## 1. Triage (5 min)
- [ ] Confirm alert in Sentinel (`SecurityIncident`), note Incident ID
- [ ] Verify user identity: `SigninLogs | where UserPrincipalName == "<user>" | where TimeGenerated > ago(2d) | order by TimeGenerated desc`
- [ ] Check user risk: `UserRiskEvents | where UserPrincipalName == "<user>"`
- [ ] Screenshot evidence -> attach to incident

## 2. Containment (15 min) — DO IN ORDER
- [ ] 1. Disable user: `Set-MgUser -UserId "<user>" -AccountEnabled:$false`
- [ ] 2. Revoke sessions: `Revoke-MgUserSignInSession -UserId "<user>"`
- [ ] 3. Reset password (random 24-char): `Reset-MgUserPassword`
- [ ] 4. Block source IP in firewall/CA: add to deny list
- [ ] 5. If MFA bypassed -> revoke MFA methods: `Get-MgUserAuthenticationMethod | Remove-MgUserAuthenticationMethod`

## 3. Investigation (30 min)
- [ ] Mail rules exfil: `Get-MailboxFolderStatistics` + `Get-InboxRule -Mailbox <user> | Where ForwardTo`
- [ ] OAuth app grants: Entra -> Enterprise apps -> check recent grants
- [ ] Data access: SharePoint/OneDrive audit for downloads after compromise time
- [ ] Lateral check: `IdentityLogonEvents | where AccountUpn == "<user>"`

## 4. Eradication (30 min)
- [ ] Delete malicious mail rules, revoke app consents
- [ ] Remove user from admin groups if added: `Get-MgUserMemberOf | Remove`
- [ ] Purge quarantine: `Search-Mailbox -Identity <user> -SearchQuery "hasattachment" -DeleteContent`

## 5. Recovery + Post-incident
- [ ] Re-enable user, force MFA re-registration, new token issuance
- [ ] Monitor 7 days: failed sign-ins, new risky events
- [ ] Lessons learned -> docs/lessons/YYYY-MM-DD-account-compromise.md
- [ ] Evidence bundle -> docs/evidence/ (for SOC 2 CC7.3)
