# TTP -> Detection Rule Matrix (MITRE ATT&CK coverage)

| MITRE ATT&CK TTP | Technique | Detection rule | Data source | Severity |
|---|---|---|---|---|
| T1078.004 | Valid Accounts: Cloud | gcp_iam_abuse.yaral, azure_admin_activity.kql | Cloud audit logs | High |
| T1078 | Valid Accounts (stolen creds) | okta_impossible_travel.yaral, defender-identity.kql | Okta / Entra ID | High |
| T1110.001/004 | Brute Force / Credential Stuffing | wap_bruteforce.kql, nsg_bruteforce.kql, vpn_impossible_travel.kql | WAF, NSG flow logs, VPN | Medium |
| T1046 / T1040 | Network Service Scanning | firewall_port_scan.kql | Firewall denies | Low |
| T1567.002 | Exfil Over Web Service | sharepoint_bulk_download.kql | SharePoint audit | Critical |
| T1530 | Data from Cloud Storage | s3_public_access.kql, sharepoint_external_sharing.kql | CloudTrail / Purview | High |
| T1486 | Data Encrypted for Impact | guardduty_crypto.kql | GuardDuty | Critical |
| T1059.001 | PowerShell | endpoint-hunting.kql | Defender for Endpoint | High |
| T1190 | Exploit Public-Facing App | WAF 403/401 anomaly + wap_bruteforce.kql | WAF | High |
| T1098 | Account Manipulation | Entra AuditLogs query (Add member to role, Update user) | Entra ID | High |
| T1562.001 | Impair Defenses | DeviceEvents where ActionType == TamperProtectionDisable | MDE | Critical |
| T1021.001 | RDP/SSH Remote Services | nsg_bruteforce.kql | NSG flow logs | Medium |
| T1210 | Exploitation of Remote Services | known_exploited.kql | Nessus + CISA KEV | High |
| T1070 | Indicator Removal | Sysmon ID 23/26, DeviceFileEvents deletion bursts | Endpoint | Medium |
