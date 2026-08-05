#!/usr/bin/env python3

"""
Okta System Log collector.

This starter collector is designed for security telemetry ingestion.
Configure authentication and destination handling through environment
variables rather than hard-coding credentials.
"""

import os
import sys
from urllib.request import Request, urlopen


OKTA_ORG_URL = os.getenv("OKTA_ORG_URL")
OKTA_API_TOKEN = os.getenv("OKTA_API_TOKEN")


def collect_logs(limit=100):
    """Collect a limited number of Okta System Log events."""
    if not OKTA_ORG_URL:
        raise RuntimeError("OKTA_ORG_URL is not configured")

    if not OKTA_API_TOKEN:
        raise RuntimeError("OKTA_API_TOKEN is not configured")

    url = f"{OKTA_ORG_URL.rstrip('/')}/api/v1/logs?limit={limit}"

    request = Request(
        url,
        headers={
            "Authorization": f"SSWS {OKTA_API_TOKEN}",
            "Accept": "application/json",
        },
    )

    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def main():
    try:
        print(collect_logs())
    except Exception as exc:
        print(f"Collector error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
