import jj
import httpx
from jj.mock import mocked
from jj_d42 import HistorySchema
from d42 import validate_or_fail


matcher = jj.match("*", "/users")
response = jj.Response(status=200, json=[])

with mocked(matcher, response) as mock:
    resp = httpx.get("http://localhost:8080/users", params={"user_id": 1})

assert validate_or_fail(
    HistorySchema % [
        {
            "request": {
                "method": "GET",
                "path": "/users",

                # equals (exact match)
                "params": {"user_id": "1"},

                # contains
                "headers": [
                    ...,
                    ["Host", "localhost:8080"],
                    ...
                ],
            }
        }
    ],
    mock.history
)
