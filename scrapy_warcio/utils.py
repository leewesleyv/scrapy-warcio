from datetime import datetime, timezone


def warc_date() -> str:
    return datetime.now(timezone.utc).isoformat() + 'Z'
