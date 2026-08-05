# Playbook 02 — Impossible Travel

## Objective

Investigate authentication events that indicate geographically improbable travel.

## Investigation

1. Identify the user.
2. Compare authentication timestamps.
3. Compare source IP addresses.
4. Determine approximate locations.
5. Check device and browser information.
6. Determine whether VPN or corporate proxy infrastructure explains the activity.
7. Correlate with MFA events.
8. Review other suspicious activity.

## Decision

Classify the event as:

- Benign
- Suspicious
- Confirmed compromise

## Response

For confirmed compromise:

- Revoke sessions.
- Reset credentials.
- Review MFA configuration.
- Review privileged activity.
- Investigate associated IP addresses and devices.

## Evidence

Document the complete authentication timeline and supporting indicators.
