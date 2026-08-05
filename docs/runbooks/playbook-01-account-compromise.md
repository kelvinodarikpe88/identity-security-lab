# Playbook 01 — Account Compromise

## Objective

Detect, investigate, contain, and recover from a suspected compromised identity.

## Detection Sources

- Microsoft Entra ID
- Okta
- Microsoft Defender
- SIEM
- Identity Protection

## Investigation Steps

1. Identify the affected account.
2. Review recent authentication activity.
3. Review source IP addresses and geolocation.
4. Check MFA changes.
5. Check password changes.
6. Check new devices and sessions.
7. Review privilege changes.
8. Identify suspicious applications or OAuth grants.

## Containment

- Revoke active sessions.
- Reset credentials.
- Require MFA re-registration where appropriate.
- Disable the account if active compromise is confirmed.
- Review privileged access.

## Evidence

Record:

- User
- Timestamp
- Source IP
- User agent
- Application
- Authentication result
- Risk level
- Actions taken

## Recovery

Restore normal access only after the account and authentication methods have been validated.

## Lessons Learned

Document root cause, indicators, timeline, containment actions, and detection improvements.
