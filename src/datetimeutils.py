from datetime import datetime, timezone
from typing import Final

utcmin: Final = datetime.min.replace(tzinfo=timezone.utc)

def utcnow() -> datetime:
    return datetime.now(timezone.utc)

def to_iso_format(dt: datetime) -> str:
    return dt.isoformat(timespec="milliseconds").replace("+00:00", "Z")

def from_iso_format(dt: str) -> datetime:
    """Converts from a datetime in ISO 8601 format to a datetime object
    Note that datetime.fromisoformat() doesn't fully support ISO 8601 in Python 3.9
    (it seems Python 3.11 corrected this), so we have to drop the last "Z" from
    the string as a workaround
    """
    if dt.endswith("Z"):
        return datetime.fromisoformat(dt[:-1])
    else:
        return datetime.fromisoformat(dt)
