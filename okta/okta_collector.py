#!/usr/bin/env python3
"""Okta System Log API -> Sentinel Custom Log (Okta_CL) via HTTP Data Collector API."""
import argparse, base64, datetime, hashlib, hmac, json, requests, time, urllib.parse

def build_signature(workspace_id, shared_key, date, content_length, method, content_type, resource):
    string_to_hash = f"{method}\n{content_length}\n{content_type}\nx-ms-date:{date}\n{resource}"
    decoded = base64.b64decode(shared_key)
    digest = hmac.new(decoded, string_to_hash.encode(), hashlib.sha256).digest()
    return f"SharedKey {workspace_id}:{base64.b64encode(digest).decode()}"

def send_to_sentinel(workspace_id, shared_key, log_type, records):
    if not records: return
    body = json.dumps(records).encode()
    date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    uri = "/api/logs?api-version=2016-04-01"
    url = f"https://{workspace_id}.ods.opinsights.azure.com{uri}"
    headers = {
        "Authorization": build_signature(workspace_id, shared_key, date, len(body), "POST", "application/json", uri),
        "Content-Type": "application/json", "x-ms-date": date, "Log-Type": log_type, "time-generated-field": "published",
    }
    r = requests.post(url, data=body, headers=headers)
    print(f"Sent {len(records)} events -> {log_type}: HTTP {r.status_code}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--okta-domain", required=True)
    p.add_argument("--api-token", required=True)
    p.add_argument("--workspace-id", required=True)
    p.add_argument("--shared-key", required=True)
    p.add_argument("--since-minutes", type=int, default=5)
    args = p.parse_args()

    since = datetime.datetime.utcnow() - datetime.timedelta(minutes=args.since_minutes)
    url = f"https://{args.okta_domain}/api/v1/logs?since={urllib.parse.quote(since.isoformat())}&limit=1000"
    headers = {"Authorization": f"SSWS {args.api_token}", "Accept": "application/json"}

    while url:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        events = r.json()
        if not events: break
        send_to_sentinel(args.workspace_id, args.shared_key, "Okta_CL", events)
        url = r.links.get("next", {}).get("url")
        time.sleep(1)

if __name__ == "__main__":
    main()
