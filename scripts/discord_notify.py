# -*- coding: utf-8 -*-
"""
discord_notify.py -- PM report sender to Discord via webhook
Setup: create scripts/.env with DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...

Usage:
  python scripts/discord_notify.py --message "PM Report: ..."
  python scripts/discord_notify.py --file pm/PM_LOG_001.md
"""

import argparse, os, sys
from pathlib import Path

def load_webhook_url() -> str:
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("DISCORD_WEBHOOK_URL="):
                return line.split("=", 1)[1].strip()
    url = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if not url:
        print("[ERROR] DISCORD_WEBHOOK_URL not set. Add to scripts/.env")
        print("  Example: DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxxx/yyyy")
        sys.exit(1)
    return url

def send(webhook_url: str, content: str):
    import urllib.request, json
    # Discord has 2000 char limit per message — split if needed
    chunks = [content[i:i+1900] for i in range(0, len(content), 1900)]
    for chunk in chunks:
        payload = json.dumps({"content": chunk}).encode("utf-8")
        req = urllib.request.Request(
            webhook_url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req) as resp:
            print(f"[discord] sent chunk ({len(chunk)} chars) -> HTTP {resp.status}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", default="", help="Message text to send")
    parser.add_argument("--file",    default="", help="Markdown file to send as message")
    args = parser.parse_args()

    webhook_url = load_webhook_url()

    if args.file:
        content = Path(args.file).read_text(encoding="utf-8")
    elif args.message:
        content = args.message
    else:
        print("[ERROR] Provide --message or --file")
        sys.exit(1)

    send(webhook_url, content)

if __name__ == "__main__":
    main()
