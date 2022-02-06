import jj
import httpx
from jj.mock import mocked
from jj_district42 import HistorySchema
from valera import validate_or_fail


matcher = jj.match("*", "/users")
response = jj.Response(status=200, json=[])

with mocked(matcher, response) as mock:
    resp = httpx.get("http://localhost:8080/users", params=[
        ("user_id", "1"),
        ("user_id", "2")
    ])

assert validate_or_fail(
    HistorySchema % [
        {
            "request": {
                "method": "GET",
                "path": "/users",
                "params": [
                    ["user_id", "1"],
                    ["user_id", "2"]
                ]
            }
        }
    ],
    mock.history
)
