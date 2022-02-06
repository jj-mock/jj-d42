import jj
import httpx
from jj.mock import mocked
from jj_district42 import HistorySchema
from valera import validate_or_fail


matcher = jj.match("*", "/users")
response = jj.Response(status=200, json=[])

with mocked(matcher, response) as mock:
    resp = httpx.post("http://localhost:8080/users", json={
        "id": 1,
        "name": "Bob"
    })

assert validate_or_fail(
    HistorySchema % [
        {
            "request": {
                "method": "POST",
                "path": "/users",
                "body": {
                    "id": 1,
                    "name": "Bob"
                }
            }
        }
    ],
    mock.history
)
