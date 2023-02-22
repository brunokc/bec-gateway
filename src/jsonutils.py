from datetime import date, datetime
import json
from typing import Any


class JSONEncoderWithDateTime(json.JSONEncoder):
    """Special JSON encoder to deal with date/datetime representation"""
    # Override the default method
    def default(self, obj: Any) -> str:
        # Since datetime derives from date, check for it first
        if isinstance(obj, datetime):
            return obj.isoformat(timespec="milliseconds").replace("+00:00", "Z")
        elif isinstance(obj, date):
            return obj.isoformat()
        return str(obj)


def clean_dict(d: Any) -> Any:
    if isinstance(d, dict):
        return {k: clean_dict(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [clean_dict(v) for v in d]
    else:
        return d


def dumps(data: Any, **kwargs: Any) -> str:
    return json.dumps(clean_dict(data), cls=JSONEncoderWithDateTime, **kwargs)
