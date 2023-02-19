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


def dumps(data):
    return json.dumps(data, cls=JSONEncoderWithDateTime)
