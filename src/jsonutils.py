from datetime import date, datetime
import json
from typing import Any


class JSONEncoderWithDateTime(json.JSONEncoder):
    """Special JSON encoder to deal with date/datetime representation"""
    # Override the default method
    def default(self, obj: Any) -> str:
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return str(obj)


def clean_dict(d):
    if isinstance(d, dict):
        return {k: clean_dict(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [clean_dict(v) for v in d]
    else:
        return d


def dumps(data, **kargs):
    return json.dumps(clean_dict(data), cls=JSONEncoderWithDateTime, **kargs)
